from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import secrets
import myLocation
from weather import main as get_weather
from dotenv import load_dotenv
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)


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

    if 'username' in session:
        user_id = get_user_id_by_username(session['username'])
        save_search_history(user_id, city, state, country, latitude, longitude)
        return render_template('index.html', data=data, city=city, country=country, error_message=error_message,
                               username=session['username'])
    else:
        return render_template('index.html', data=data, city=city, country=country, error_message=error_message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT username, password FROM tbl_users WHERE username = '{username}'")
        user = cur.fetchone()

        cur.close()

        if user and password == user[1]:
            session['username'] = user[0]

            return redirect(url_for('index'))

        return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO tbl_users (username, email, password) VALUES ('{username}', '{email}', '{password}')")
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
