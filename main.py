import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import time
import smtplib

load_dotenv()

HOSTNAME = os.environ["SMTP_HOSTNAME"]
PORT = int(os.environ["SMTP_PORT"])
USERNAME = os.environ["SMTP_USERNAME"]
PASSWORD = os.environ["SMTP_PASSWORD"]
TEST_EMAIL_1 = os.environ["TEST_EMAIL_1"]
TEST_EMAIL_2 = os.environ["TEST_EMAIL_2"]

# My Latitude/Longitude
MY_LAT = 40.346401 # Real
# MY_LAT = -50.4584 # Testing

MY_LONG = -111.910072 # Real
# MY_LONG = 71.4625 # Testing
while True:

    # ISS Position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"]) # Real
    iss_longitude = float(data["iss_position"]["longitude"]) # Real

    # iss_latitude = -51.4584 # Testing
    # iss_longitude = 70.4625 # Testing
    print(f"The iss_latitude is {iss_latitude}")
    print(f"The iss_longitude is {iss_longitude}")

    #Your position is within +5 or -5 degrees of the ISS position.
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    print(f"The sunset hour is {sunset}")
    print(f"The current hour is {time_now.hour}")

    #If the ISS is close to my current position
    if ((MY_LAT <= iss_latitude + 5) and (MY_LAT >= iss_latitude - 5)) and ((MY_LONG <= iss_longitude + 5) and (MY_LONG >= iss_longitude - 5)):
        if time_now.hour >= sunset:
            print("True")
            with smtplib.SMTP(HOSTNAME, PORT) as connection:
                connection.starttls()
                connection.login(user=USERNAME, password=PASSWORD)
                connection.sendmail(from_addr=USERNAME, to_addrs=TEST_EMAIL_1, msg="Subject: ISS Passing By!\n\nLook up! The ISS is passing overhead!")
    else:
        print("False")
    time.sleep(60)




