#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = os.environ.get("OWM_API_KEY")
# account_sid = "YOUR ACCOUNT SID"
# auth_token = os.environ.get("AUTH_TOKEN")

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "78d813e6a4de626bab69c176d3b90557"

account_sid = "ACd7a4513ac822c8c478da38fc384312bd"
auth_token = "05aa89ab5386eed2b67226d2afb59d20"

# weather_params = {
#     "lat": "19.0760°",
#     "lon": "77.216721",
#     "appid": api_key,
#     "exclude": "current,minutely,daily"
# }

weather_params = {
    "q" : "Delhi,IN",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
# weather_slice = weather_data["hourly"][:12]

will_rain = False

# for hour_data in weather_data:
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) > 700:
    will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19787057064",
        to="+917876002963"
    )
    print(message.status)

