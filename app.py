from flask import Flask, render_template, request

import myLocation
from weather import main as get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    data = None
    city = None
    state = None
    country = None
    myLocation.get_location_info()
    if request.method == 'POST':
        if 'latitude' in request.form and 'longitude' in request.form:
            # If latitude and longitude are provided, use them directly
            latitude_str = request.form['latitude']
            longitude_str = request.form['longitude']


            if latitude_str and longitude_str:
                try:
                    # Convert latitude and longitude to floats
                    latitude = float(latitude_str)
                    longitude = float(longitude_str)


                    # Use the city, state, and country data
                    data = get_weather(city, state, country, latitude=latitude, longitude=longitude)
                    print(f"Latitude: {latitude}, Longitude: {longitude}")
                except ValueError as e:
                    print(f"Error converting latitude/longitude to float: {e}")
                    error_message = "Invalid latitude or longitude."
            else:
                print("Latitude or Longitude is empty.")
        else:
            city = request.form['cityName']
            state = request.form['stateName']
            country = request.form['countryName']

            # Use the city, state, and country data
            data = get_weather(city, state, country)

            # Check for error in the data
            if (not city or not country) or not data:
                error_message = "Invalid city or country name."

    return render_template('index.html', data=data, city=city, country=country, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)
