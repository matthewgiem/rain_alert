from apikey import api_key
import requests
import json

OMW_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 13.87719,
    "lon": 100.71991,
    "appid": api_key,
}

response = requests.get(OMW_Endpoint, params=parameters)
weather_data = response.json()

json_object = json.dumps(weather_data, indent=4)

with open("weather_data.json", "w") as outfile:
    outfile.write(json_object)

