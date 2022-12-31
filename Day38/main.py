# import requests
# from datetime import datetime

# APP_ID = "88adecf4"
# API_KEY = "a062dbd7d8d62f033ac5bd02ab8bd574"

# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# # sheet_endpoint = "https://api.sheety.co/2725c5ba490693b4441a87356481d880/api/sheet1"

# exercise_text = input("Tell me which exercises you did: ")
# # exercise_text = "lunges"
# GENDER = "Male"
# WEIGHT = "70"
# HEIGHT = "178"
# AGE = "22"

# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY
# }

# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT,
#     "height_cm": HEIGHT,
#     "age": AGE
# }

# response = requests.post(exercise_endpoint, parameters, headers=headers)
# result = response.json()
# print(result)

# # ##############################################################
# sheet_endpoint = "https://api.sheety.co/2725c5ba490693b4441a87356481d880/aaa/bbb"
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# for exercise in result["exercises"]:
# #     print(exercise)
# #     if exercise["description"] == None:
# #         exercise["description"] = "Nil"
    
# #     if exercise["benefits"] == None:
# #         exercise["benefits"] = "Nil"
    
#     sheet_inputs = {
#         "bbb": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

#     sheety_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

#     print("response.status_code =", response.status_code)
#     print("response.sheety_response =", sheety_response.json())


##############################################################
# Get api to fetch the data

# import requests
# Get_data = "https://api.sheety.co/2725c5ba490693b4441a87356481d880/aaa/bbb"
# response = requests.get(Get_data)
# resp = response.text

# print(resp)


##############################################################
# Put api to update the data

# import requests
# Id = int(input("Tell me the id on which you want the updation:"))+1
# SHEETY_ENDPOINT = f"https://api.sheety.co/2725c5ba490693b4441a87356481d880/aaa/bbb/{Id}"
# Edit_Calories_Entry = float(input("Tell me the editable calories value:"))
# sheet_inputs = {
#         "bbb": {
#             "calories": Edit_Calories_Entry,
#         }
#     }
# # Id = 771
# # Edit_data = f"{SHEETY_ENDPOINT}/{id}"

# sheety_response = requests.put(url=SHEETY_ENDPOINT, json=sheet_inputs)
# print("response.status_code =", sheety_response.status_code)
# print("response.sheety_response =", sheety_response.json())


##############################################################
# To delete the data

# import requests
# import json
# Id = int(input("Tell me the id on which you want to delete:"))+1
# SHEETY_ENDPOINT = f"https://api.sheety.co/2725c5ba490693b4441a87356481d880/aaa/bbb/{Id}"

# sheety_response = requests.delete(url=SHEETY_ENDPOINT)
# print("response.status_code =", sheety_response.status_code)
# if sheety_response.status_code == 204:
#     print("Deleted Successfully")
