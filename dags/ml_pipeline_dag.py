from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'mlops',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='ml_pipeline_dag',
    default_args=default_args,
    description='Pipeline to preprocess data and train ML model',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    preprocess_data = BashOperator(
        task_id='preprocess_data',
        bash_command='cd /opt/airflow && python src/etl/pre_processing.py'
    )

    train_model = BashOperator(
        task_id='train_model',
        bash_command='cd /opt/airflow && python src/modeling/linear_regression.py'
    )

    preprocess_data >> train_model
