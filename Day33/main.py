# HTTP Status Codes Glossary : https://www.webfx.com/web-development/glossary/http-status-codes/

# import requests

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# # print(response.status_code)
# # response.raise_for_status() #- returns an HTTPError object if an error has occurred during the process.  

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude, longitude)
# print(iss_position)


import requests
from datetime import datetime

parameters = {
    "lat":28.7041,
    "lng":77.1025,
    "formatted":0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print("sunrise", sunrise)
print("sunset", sunset)
print("present_time", datetime.now().hour)
# print(time_now.hour)
