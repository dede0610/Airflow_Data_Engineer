import requests
from datetime import datetime
import sqlite3


API_KEY = "a76e5cae92c52effbbfcb98d8001****" #I hide my key on purpose. To get your own key go on Openweathermap and create an account then find your key here : https://home.openweathermap.org/api_keys
CITY = "Melbourne"
DB_PATH = "./weather_data.db"


def get_store_weather_data():
    weather_data = extract_weather_data()
    print(weather_data)
    dict_data = transform_weather_data(weather_data=weather_data)
    print(dict_data)

    store_data_in_db(transformed_data=dict_data, db_path=DB_PATH)

    print("database successfully updated")


def extract_weather_data(city=CITY, Api_key=API_KEY):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    return weather_data


def transform_weather_data(weather_data):
    transformed_data = {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "temp_min": weather_data["main"]["temp_min"],
        "temp_max": weather_data["main"]["temp_max"],
        "humidity": weather_data["main"]["humidity"],
        "description": weather_data["weather"][0]["description"],
        "datetime": datetime.now().strftime("%d-%m-%Y %H:%M"),
    }
    # print(transformed_data)
    return transformed_data


def store_data_in_db(transformed_data, db_path=DB_PATH):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            temp_min REAL,
            temp_max REAL,
            humidity INTEGER,
            description TEXT,
            datetime TEXT
        )
        """
    )

    cursor.execute(
        """
    INSERT INTO weather (city, temperature, temp_min, temp_max, humidity, description, datetime) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            transformed_data["city"],
            transformed_data["temperature"],
            transformed_data["temp_min"],
            transformed_data["temp_max"],
            transformed_data["humidity"],
            transformed_data["description"],
            transformed_data["datetime"],
        ),
    )

    conn.commit()
    cursor.close()
    conn.close()


# # Insert data
# cursor.execute('''
#     INSERT INTO weather (city, temperature, humidity, description, datetime)
#     VALUES ('Melbourne', 20, 90, 'Cloudy', '02-11-2024 11:17:45')
#     ''')



get_store_weather_data()
