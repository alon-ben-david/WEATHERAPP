import ssl
import certifi
import geopy
from geopy.geocoders import Nominatim
from functools import partial
from time import sleep


def extract_city_name(address):
    # Split the address by commas
    parts = address.split(',')

    # Check each part to see if it looks like a city name
    for part in parts:
        # You may need to customize these conditions based on your addresses
        if len(part.split()) <= 2 and part[0].isalpha():
            return part.strip()

    # If no suitable part is found, return the first part
    return parts[0].strip()

def get_location_info():
    user_agent = "WEATHERAPP/1.0"

    # Get the path to the CA certificates bundle from certifi
    cafile = certifi.where()

    # Configure geopy to use the specified CA certificates file
    geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=cafile)

    geolocator = Nominatim(user_agent=user_agent)

    reverse = partial(geolocator.reverse, language="en")




