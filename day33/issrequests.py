import requests
from datetime import datetime
import smtplib
iss_location_api_url = "http://api.open-notify.org/iss-now.json"

# 1xx hold on
# 2xx success
# 3xx no permission
# 4xx you screwed up
# 5xx server screwed up

response = requests.get(url=iss_location_api_url)
response.raise_for_status()

# iss_longitude = response.json()["iss_position"]["longitude"]
# iss_latitude = response.json()["iss_position"]["latitude"]


iss_latitude = 45
iss_longitude = -80

MY_LAT = 43.706270
MY_LONG = -79.394360

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()

sun_rise = sun_response.json()["results"]["sunrise"]
sun_set = sun_response.json()["results"]["sunset"]

sunrise_split = sun_rise.split("T")[1].split(":")[0]
sunset_split = sun_set.split("T")[1].split(":")[0]

time_now = datetime.now()

print((MY_LAT, MY_LONG), (iss_latitude, iss_longitude))

print(MY_LAT - iss_latitude)
print(MY_LONG - float(iss_longitude))

#if the iss is close to my position within +5 or -5 degrees
# and it is currently dark
#then send me an email

if ((MY_LAT - float(iss_latitude) <= 5 and MY_LAT - float(iss_latitude) >= -5) and (MY_LONG - float(iss_longitude) <= 5 and MY_LONG - float(iss_longitude) >= -5)):
    if(int(time_now.hour) >= int(20)):
        print("its close and dark, time to send an email")
