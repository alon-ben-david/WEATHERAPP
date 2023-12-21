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
    resp = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={1}&appid={API_KEY}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def get_current_weather(lat, lon, API_KEY):
    try:
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


def main(city_name, state_name, country_name):
    lat, lon = get_lan_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    weather_data.sunrise = convert_utc_to_local(weather_data.sunrise)
    weather_data.sunset = convert_utc_to_local(weather_data.sunset)

    return weather_data


if __name__ == "__main__":
    pass
