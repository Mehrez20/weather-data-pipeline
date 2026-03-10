import pandas as pd
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Connexion PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="airflow",
    user="airflow",
    password="airflow",
    port="5432"
)

print("Connected to database")

# Charger les données météo
query = """
SELECT temperature, humidity, latitude
FROM weather_data
"""

df = pd.read_sql(query, conn)

print("Data loaded from database")

# Créer la cible (température suivante)
df["target"] = df["temperature"].shift(-1)

# Supprimer lignes vides
df = df.dropna()

# Features
X = df[["temperature", "humidity", "latitude"]]

# Target
y = df["target"]

# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modèle IA
model = LinearRegression()

# Entraînement
model.fit(X_train, y_train)

print("Model trained successfully")

# Sauvegarde du modèle
joblib.dump(model, "weather_model.pkl")

print("Model saved as weather_model.pkl")