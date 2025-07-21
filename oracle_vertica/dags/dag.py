import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id='oracle_vertica',
    start_date = datetime.datetime(2020, 1, 1),
    schedule_interval = '@daily',

):
    EmptyOperator(task_id='task')