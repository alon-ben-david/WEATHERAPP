from datetime import datetime
from app import *

mysql.init_app(app)


def save_search_history(user_id, city, state, country, latitude, longitude):
    if any([city, state, country, latitude, longitude]):
        cur = mysql.connection.cursor()
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        cur.execute(
            "INSERT INTO search_history (user_id, city, state, country, latitude, longitude, timestamp) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, city, state, country, latitude, longitude, timestamp)
        )

        mysql.connection.commit()
        cur.close()


def get_user_id_by_username(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM tbl_users WHERE username = %s", (username,))
    user_id = cur.fetchone()[0]
    cur.close()
    return user_id


def get_search_history(user_id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM search_history WHERE user_id = {user_id}")
    search_history_data = cur.fetchall()
    cur.close()
    print(search_history_data)  # Add this line to print the retrieved data

    return search_history_data
