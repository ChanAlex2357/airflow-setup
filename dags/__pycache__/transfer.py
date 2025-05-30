from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.task_group import TaskGroup
from datetime import datetime

MYSQL_DATA_SOURCE = ['categories', 'products', 'clients', 'sales', 'inventory']

def prepare_table(table_name, hook):
        hook.run(f"TRUNCATE TABLE {table_name}")


def transfer_data(source_name):
    '''
        Creation d'un schema temporaire pour le transfer de donnee
    '''
    target_table = f"{source_name}_raw" # le nom de la table en raw
    
    mysql_hook = MySqlHook(mysql_conn_id='mysql_ops')
    psql_hook = PostgresHook(postgres_conn_id='dwh_raw')

    prepare_table(target_table, psql_hook) # nettoyer la table raw dans postgresql

    records = mysql_hook.get_records(f"SELECT * FROM {source_name}") # recuperer les lignes de donnees dans mysql 

    if records :
        psql_hook.insert_rows(table=target_table, rows=records) # inserer les lignes de mysql dans postgres



with DAG (
        dag_id="ops_to_raw",
        start_date=datetime(2025,5,28),
        schedule='@daily',
        catchup=False,
        tags={'raw','ops','ecommerce','dwh'},
) as dag:
    
    with TaskGroup(group_id="transfer_tables") as transfer_group:
        for table in MYSQL_DATA_SOURCE:
            PythonOperator (
                task_id=f"transfert_{table}",
                python_callable=transfer_data(table),
            )