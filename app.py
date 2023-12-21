from flask import Flask, render_template, request
from weather import main as get_weather
from processDateTime import *

app = Flask(__name__)

# Register the filter with Jinja2
app.jinja_env.filters['timestamp_to_datetime'] = timestamp_to_datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    city = None
    state = None

    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city, state, country)

    return render_template('index.html', data=data, city=city, country=country)


if __name__ == "__main__":
    app.run(debug=True)
