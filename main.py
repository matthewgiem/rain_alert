from apikey import api_key
import requests

OMW_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 13.87719,
    "lon": 100.71991,
    "appid": api_key,
}

response = requests.get(OMW_Endpoint, params=parameters)
print(response.json())
