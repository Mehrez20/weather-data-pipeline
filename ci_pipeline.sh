#!/bin/bash

echo "Starting CI pipeline..."

echo "Step 1: Build Docker containers"
docker compose build

echo "Step 2: Start services"
docker compose up -d

echo "Step 3: Check Airflow DAGs"
docker exec airflow_weather airflow dags list

echo "Pipeline finished"
