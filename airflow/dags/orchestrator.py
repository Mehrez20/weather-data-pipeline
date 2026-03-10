from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Permet d'importer les modules du projet
sys.path.append("/opt/airflow")

# Import de ta fonction principale
from api_request.insert_records import main as fetch_and_store_weather

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="weather_data_pipeline",
    default_args=default_args,
    description="Pipeline to fetch weather data and store it in PostgreSQL",
    schedule_interval="@hourly",
    catchup=False,
    tags=["weather", "etl", "api"],
) as dag:

    fetch_and_store_weather_task = PythonOperator(
        task_id="fetch_and_store_weather",
        python_callable=fetch_and_store_weather,
    )

    fetch_and_store_weather_task