from datetime import datetime, timedelta


# Define the custom filter function
def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def convert_utc_to_local(utc_time):
    # Convert the timestamp to a string if it's an integer
    if isinstance(utc_time, int):
        utc_time = timestamp_to_datetime(utc_time)

    # Parse the UTC time string to a datetime object
    utc_datetime = datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S')

    # Set the local timezone offset to UTC+2
    local_timezone_offset = 2  # Adjust the offset as needed

    # Calculate the local time by adding the timezone offset
    local_datetime = utc_datetime + timedelta(hours=local_timezone_offset)

    return local_datetime
