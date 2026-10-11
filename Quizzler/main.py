import requests
from twilio.rest import Client

owm_endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_keys = "4bc4394991aab8f5f4be22eacc6e29ec"
account_sid = "AC0e0b6ee41a69b5c39c4f1f5b03cf26c5"
auth_token = "66QVR2ZAN1EM66XBKAH5KYZ5"

weather_parameter={
    "lat":11.454620,
    "lon":77.831001,
    "appid":api_keys,
    "cnt":4,
}

response = requests.get(owm_endpoint, params=weather_parameter)
response.raise_for_status()
weather_data=response.json()
for hour_data in weather_data["list"]:
    condition=hour_data["weather"][0]["id"]
    if int(condition)<700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
    )

print(message.status)