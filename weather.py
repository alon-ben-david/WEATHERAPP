import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

from processDateTime import *

load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    humidity: int
    sunrise: int
    sunset: int


def get_lan_lon(city_name, state_code, country_code, API_KEY):
    try:
        resp = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={1}&appid={API_KEY}').json()

        # Check if the response contains valid location data
        if resp and isinstance(resp, list) and len(resp) > 0:
            data = resp[0]
            lat, lon = data.get('lat'), data.get('lon')
            print(lat)
            print(lon)
            return lat, lon
        else:
            print("Invalid city or country name.")
            return None, None

    except Exception as e:
        print("Error fetching location data:", e)
        return None, None


def get_current_weather(lat, lon, API_KEY):
    try:
        if lat is None or lon is None:
            return None
        resp = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric').json()

        if 'main' in resp and 'weather' in resp:
            weather_data = WeatherData(
                main=resp['weather'][0]['main'],
                description=resp['weather'][0]['description'],
                icon=resp['weather'][0]['icon'],
                temperature=resp['main']['temp'],
                feels_like=resp['main']['feels_like'],
                temp_min=resp['main']['temp_min'],
                temp_max=resp['main']['temp_max'],
                humidity=resp['main']['humidity'],
                sunrise=resp['sys']['sunrise'],
                sunset=resp['sys']['sunset']
            )
            return weather_data
        else:
            print("Unexpected JSON structure:", resp)
            return None

    except Exception as e:
        print("Error fetching weather data:", e)
        return None


def main(city_name, state_name, country_name, latitude=None, longitude=None):
    if latitude is None or longitude is None:
        # If latitude and longitude are not provided, obtain them using the city, state, and country
        latitude, longitude = get_lan_lon(city_name, state_name, country_name, api_key)

    # Use the latitude and longitude to get weather data
    weather_data = get_current_weather(latitude, longitude, api_key)
    if weather_data == None:

        return weather_data
    weather_data.sunrise = convert_utc_to_local(weather_data.sunrise)
    weather_data.sunset = convert_utc_to_local(weather_data.sunset)
    print(weather_data.temp_max
          )
    return weather_data


if __name__ == "__main__":
    pass
