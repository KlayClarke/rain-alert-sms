import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
api_key = os.environ.get('OWM_API_KEY')

latitude = 42.3601
longitude = 71.0589

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
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_=f'{from_number}',
        to=f'{to_number}'
    )
    print(message.status)

