from airflow import DAG
from airflow.operators.python import PythonOperator
from postgres_utils import PostgresOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta
import pandas as pd
import os

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def log_etl_status(table_name, rows, status, error=None):
    pg_hook = PostgresHook(postgres_conn_id='postgres_dwh')
    pg_hook.run(
        """INSERT INTO ecommerce_dwh.etl_log 
        (table_name, rows_processed, status, error_message) 
        VALUES (%s, %s, %s, %s)""",
        parameters=(table_name, rows, status, error)
    )

def transfer_table(mysql_table, postgres_table):
    try:
        mysql_hook = MySqlHook(mysql_conn_id='mysql_ecommerce')
        pg_hook = PostgresHook(postgres_conn_id='postgres_dwh')
        
        # 1. Extraction
        df = mysql_hook.get_pandas_df(f"SELECT * FROM {mysql_table}")
        
        # 2. Transformation
        df['_etl_loaded_at'] = datetime.now()
        
        # 3. Chargement
        csv_path = f"/tmp/{postgres_table}.csv"
        df.to_csv(csv_path, index=False)
        
        # TRUNCATE avant chargement
        pg_hook.run(f"TRUNCATE TABLE ecommerce_dwh.{postgres_table}")
        
        # COPY avec gestion d'erreurs
        pg_hook.copy_expert(
            sql=f"COPY ecommerce_dwh.{postgres_table} FROM STDIN WITH CSV HEADER",
            filename=csv_path
        )
        
        # Vérification
        pg_count = pg_hook.get_first(f"SELECT COUNT(*) FROM ecommerce_dwh.{postgres_table}")[0]
        log_etl_status(postgres_table, pg_count, 'success')
        
    except Exception as e:
        log_etl_status(postgres_table, 0, 'failed', str(e))
        raise
    finally:
        if os.path.exists(csv_path):
            os.remove(csv_path)

with DAG(
    dag_id='ecommerce_etl_robust',
    schedule='@daily',
    start_date=datetime(2023, 1, 1),
    default_args=default_args,
    catchup=False
) as dag:
    
    init_db = PostgresOperator(
        task_id='initialize_postgres',
        conn_id='postgres_dwh',
        sql='init_postgres.sql'
    )
    
    transfer_tasks = []
    tables_mapping = {
        'categories': 'categories',
        'clients': 'clients',
        'products': 'products',
        'inventory': 'inventory',
        'sales': 'sales',
        'payment_history': 'payment_history'
    }
    
    for mysql_table, pg_table in tables_mapping.items():
        task = PythonOperator(
            task_id=f'transfer_{pg_table}',
            python_callable=transfer_table,
            op_kwargs={
                'mysql_table': mysql_table,
                'postgres_table': pg_table
            }
        )
        transfer_tasks.append(task)
    
    verify_data = PostgresOperator(
        task_id='verify_data_integrity',
        conn_id='postgres_dwh',
        sql="""
        DO $$
        BEGIN
            IF (SELECT COUNT(*) FROM ecommerce_dwh.etl_log WHERE status = 'failed') > 0 THEN
                RAISE EXCEPTION 'Certaines tables n''ont pas été chargées correctement';
            END IF;
        END $$;
        """
    )
    
    init_db >> transfer_tasks >> verify_data

# Modelisation DWH