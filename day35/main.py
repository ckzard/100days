import os
import requests
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

f = open("../twiliodetails.txt", "r")
twil_details = f.readlines()

account_sid = twil_details[0]
auth_token = twil_details[1]




weather_api_key = twil_details[2]
lat = 43.653225
lon = -79.383186

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={weather_api_key}")

next_twelve_hours = weather_data.json()["hourly"][:12]
will_rain = False

for hour in next_twelve_hours:
    current_weather_id = hour["weather"][0]["id"]
    if current_weather_id < 700:
        will_rain = True

    
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It is going to rain today. Remember to bring an ☂️",
                        from_='+15714975854',
                        to='+16473080344'
                    )

    print(message.status)

#PYTHON ANYWHERE 