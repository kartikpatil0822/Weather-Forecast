import requests

MY_LAT = "18.520430"
MY_LON = "73.856743"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "Your Own API"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,
}

resp = requests.get(WEATHER_ENDPOINT, params=weather_params)
resp.raise_for_status()
weather_data = resp.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain = True

print("Take Umbrella with you while going out" if will_rain else "Happy Day")
