import requests
from twilio.rest import Client

account_sid = "*******************"
auth_token = "***************"

API_KEY = "***************"
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
        to="************"
    )

    print(message.status)
