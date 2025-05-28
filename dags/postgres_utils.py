from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

class PostgresOperator(SQLExecuteQueryOperator):
    conn_type = 'postgres'