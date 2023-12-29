## Description

This project is a Flask-based weather application that allows users to check the current weather conditions based on either city and country or geographic coordinates.
And in addition allows viewing the user's search history.

### Prerequisites

Make sure you have the following tools installed on your machine:

- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [requests](https://docs.python-requests.org/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)

Or install requirements.txt file with:

```bash
pip install -r requirements.txt
```


### To get started with the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alon-ben-david/flask-weather-app.git
   cd flask-weather-app

## Configuration

### MySQL

1. Make sure you have MySQL installed and running.
2. Create a database named `flask_users`.
3. Set up the necessary tables using the provided SQL scripts.

### Flask

1. Open the `app.py` file.
2. Update the MySQL configuration with your credentials.

## Usage

To run the application, execute the following command:

```bash
python app.py
Visit http://localhost:5000/ in your web browser to access the weather application.
```


