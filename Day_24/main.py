import requests
from twilio.rest import Client

account_sid = "ACeca87e898f48a598a1d18e1c6f9c9fb2"
auth_token = "fb9c8962e3bf24d0865556c5a6b30d98"

API_KEY = "87d85b77fe2be0d451d7c527e6cbc6cf"
parameters = {
    "lat": 37.523449,
    "lon": 42.454289,
    "appid": API_KEY,
    "cnt": 4
}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()

weatherData = response.json()
# print(weatherData)
is_condition = False
for weatherId in weatherData["list"]:
    weatherCondition = weatherId['weather'][0]['id']
    if weatherCondition < 700:
        is_condition = True

if is_condition:
    # print("Bring an umbrella")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's is going to rain today. Remember to bring ☂️",
        from_="+13203612633",
        to="+923001701299"
    )

    print(message.status)
