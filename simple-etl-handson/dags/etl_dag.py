from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv

INPUT_FILE = "/opt/airflow/data/input.csv"
OUTPUT_FILE = "/opt/airflow/data/output.csv"


def extract():
    data = []
    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def transform(ti):
    data = ti.xcom_pull(task_ids="extract")

    # simple transformation: filter age >= 18
    transformed = [row for row in data if int(row["age"]) >= 18]
    
    # to upper case and strip name
    transformed = [
        {**row, "name": row["name"].strip().upper()}
        for row in transformed
        if row["name"].strip()
    ]

    return transformed


def load(ti):
    data = ti.xcom_pull(task_ids="transform")

    with open(OUTPUT_FILE, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age"])
        writer.writeheader()
        writer.writerows(data)


with DAG(
    dag_id="simple_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task