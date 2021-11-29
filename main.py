import requests
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6441500d5adc9b8a0efb709d2d0a4c38'
auth_token = 'bed7adec29e116248d5f51f6e5119ca7'

api_key = 'a5562bcf068078abc0381db8dfc12bd6'

latitude = 42.360081
longitude = -71.058884

parameters = {
    'lat': latitude,
    'lon': longitude,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data['hourly']

weather_slice = hourly_data[:12]

half_day_hourly_condition = []

from_number = None
to_number = None

will_rain = False

for data in weather_slice:
    half_day_hourly_condition.append(data['weather'][0]['id'])
    if data['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_=f'{from_number}',
        to=f'{to_number}'
    )
    print(message.status)
