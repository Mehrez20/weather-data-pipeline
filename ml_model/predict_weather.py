import psycopg2
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load("weather_model.pkl")

# Connexion PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="airflow",
    user="airflow",
    password="airflow",
    port="5432"
)

print("Connected to database")

# Lire la dernière donnée météo
query = """
SELECT temperature, humidity, latitude
FROM weather_data
ORDER BY timestamp DESC
LIMIT 1
"""

df = pd.read_sql(query, conn)

print("Latest weather data:")
print(df)

# Faire la prédiction
prediction = model.predict(df)

print("Predicted next temperature:", prediction[0])