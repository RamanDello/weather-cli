import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.7753,
    "longitude": 6.0839,
    "current_weather": True,
}

response = requests.get(url, params=params)
# 200 heißt erfolgreiche Anfrage
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    print(f"Temperatur: {weather['temperature']} °C")
    print(f"Wind: {weather['windspeed']} km/h")
else:
    print(f"Fehler: ___")
