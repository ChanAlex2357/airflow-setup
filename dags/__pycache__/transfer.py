from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.task_group import TaskGroup
from datetime import datetime

MYSQL_DATA_SOURCE = ['categories', 'products', 'clients', 'sales', 'inventory']

def prepare_schema():
    '''
        Creation d'un schema temporaire pour le transfer de donnee
    '''
    hook = MySqlHook(mysql_conn_id='mysql_ops')

with DAG (
        dag_id="ops_to_raw",
        start_date=datetime(2025,5,28),
        schedule='@daily',
        catchup=False,
        tags={'raw','ops','ecommerce','dwh'},
) as dag:
    
    with TaskGroup(group_id="transfer_tables") as transfer_group:
        