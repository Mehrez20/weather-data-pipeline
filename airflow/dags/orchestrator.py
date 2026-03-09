from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys
sys.path.append("/opt/airflow")

from api_request.insert_records import main

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="weather_data_pipeline",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    fetch_and_store_weather = PythonOperator(
        task_id="fetch_and_store_weather",
        python_callable=main,
    )