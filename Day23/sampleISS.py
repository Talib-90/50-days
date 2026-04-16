import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
parameters = {
    "lat": 24.860735,
    "lng": 67.001137,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
print(sunrise)