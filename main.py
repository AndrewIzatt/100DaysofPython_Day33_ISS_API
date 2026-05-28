import requests
from datetime import datetime as dt

MY_LAT = 40.346401
MY_LONG =-111.910072

MY_PARAMS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

current_time = dt.now()
print(current_time)

response = requests.get("https://api.sunrise-sunset.org/json", params=MY_PARAMS)
response.raise_for_status()
data = response.json()
# Sunrise
sunrise_data = data["results"]["sunrise"]
sunrise = sunrise_data.split("T")
sunrise_day = sunrise[0]
sunrise_time = sunrise[1]
sunrise_hour = sunrise_time.split(":")[0]
print(sunrise_hour)
# Sunset
sunset_data = data["results"]["sunset"]
sunset = sunset_data.split("T")
sunset_day = sunset[0]
sunset_time = sunset[1]
sunset_hour = sunset_time.split(":")[0]
print(sunset_hour)
# print(sunset)