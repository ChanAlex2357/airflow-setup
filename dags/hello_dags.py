from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='hello_dag',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    tache_1 = BashOperator(
        task_id='afficher_date',
        bash_command='date'
    )

    tache_2 = BashOperator(
        task_id='afficher_utilisateur',
        bash_command='whoami'
    )

    tache_1 >> tache_2  # tache_2 dépend de tache_1