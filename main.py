import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.7753,
    "longitude": 6.0839,
    "current_weather": True,
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.json())
