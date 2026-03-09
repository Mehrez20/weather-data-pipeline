import requests

API_KEY = "43086e247ae26bfee6ca5745ce4be509"

cities = ["New York", "Paris", "Tunis", "Tokyo"]

def fetch_weather():

    results = []

    for city in cities:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if "main" not in data:
            print("API error:", data)
            continue

        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        results.append(weather)

    return results