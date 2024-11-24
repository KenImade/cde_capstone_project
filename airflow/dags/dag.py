from datetime import timedelta

from includes.get_country_data import get_country_data
from includes.process_data import _process_data

import airflow

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


default_args = {
    'owner': 'kenneth',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'params': {
        'raw_data_path': 'opt/airflow/data/raw',
        'processed_data_path': 'opt/airflow/data/processed',
        'api_url': "https://restcountries.com/v3.1/all"
    }
}

with DAG(
    dag_id='travel_agency_dag',
    default_args=default_args,
    description='A dag to download data about countries in the world',
    schedule_interval=None
) as dag:
    start = DummyOperator(
        task_id='start'
    )

    download_data = PythonOperator(
        task_id='download_data',
        python_callable=get_country_data
    )

    process_data = PythonOperator(
        task_id='process_data',
        python_callable=_process_data
    )

    # upload_data = PythonOperator()

    start >> download_data >> process_data
