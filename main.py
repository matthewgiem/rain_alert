from apikey import api_key
import requests
import json


# use to imoprt weather data from openweathermap so as to not use up all my free api calls
# OMW_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
#
# parameters = {
#     "lat": 13.87719,
#     "lon": 100.71991,
#     "appid": api_key,
# }
#
# response = requests.get(OMW_Endpoint, params=parameters)
# weather_data = response.json()
#
# json_object = json.dumps(weather_data, indent=4)
#
# with open("weather_data.json", "w") as outfile:
#     outfile.write(json_object)

# Open JSON file and save to local variable

weather_json = open('weather_data.json')

weather_dict = json.load(weather_json)

weather_json.close()

# print(weather_dict["hourly"][0]["weather"][0]["id"])

# for x in range(10):
#     print(weather_dict["hourly"][x]["weather"][0]["id"])

hourly = weather_dict["hourly"][0:11]
for x in hourly:
    if x["weather"][0]["id"] > 99 and x["weather"][0]["id"] < 1000:
        if x["weather"][0]["id"] > 199 and x["weather"][0]["id"] < 300:
            print("Thunderstorm")
        elif x["weather"][0]["id"] > 299 and x["weather"][0]["id"] < 400:
            print("Drizzle")
        elif x["weather"][0]["id"] > 499 and x["weather"][0]["id"] <600:
            print("Rain")
        elif x["weather"][0]["id"] > 599 and x["weather"][0]["id"] < 700:
            print("Snow")
        elif x["weather"][0]["id"] > 699 and x["weather"][0]["id"] < 800:
            print("Haze")
        elif x["weather"][0]["id"] == 800:
            print("Clear")
        elif x["weather"][0]["id"] > 800 and x["weather"][0]["id"] < 900:
            print("Cloudy")




