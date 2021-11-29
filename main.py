import requests

api_key = 'a5562bcf068078abc0381db8dfc12bd6'

latitude = 42.360081
longitude = -71.058884

parameters = {
    'lat': latitude,
    'lon': longitude,
    'appid': api_key
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()
print(data)
