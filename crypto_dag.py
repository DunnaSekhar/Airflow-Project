from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from crypto import run_crypto_etl

default_args = {
    'owner': 'dunna-airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['dunnasekhar786@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'crypto_dag',                   # DAG Name display on airflow
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_crypto_etl',  # Task name will display on airflow
    python_callable=run_crypto_etl,
    dag=dag, 
)

run_etl