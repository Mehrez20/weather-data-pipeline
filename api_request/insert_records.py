import psycopg2
from api_request.fetch_weather import fetch_weather


def main():

    weather_list = fetch_weather()

    connection = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO weather_data (city, temperature, humidity, weather_description)
    VALUES (%s, %s, %s, %s)
    """

    for weather in weather_list:

        cursor.execute(
            insert_query,
            (
                weather["city"],
                weather["temperature"],
                weather["humidity"],
                weather["description"],
            ),
        )

    connection.commit()

    cursor.close()
    connection.close()