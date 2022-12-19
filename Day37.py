import requests
from datetime import datetime

USER_NAME = "punitmann9599"

# Creation of an user
USER_CREATION = "https://pixe.la/v1/users"
TOKEN = "fienfdneoej3nsndwndwn"
user_creation_params = {
    "token": TOKEN,
    "username": "punitmann9599",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url= USER_CREATION, json=user_creation_params)


# Creation of graphs using username
GRAPH_CREATION = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
user_graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url = GRAPH_CREATION, json=user_graph_params, headers=headers)

# Get the graph status---- https://pixe.la/v1/users/punitmann9599/graphs/graph1.html

# Add value to the graph
USER_DATE = datetime(year=2022, month=12, day=17)

DATE = USER_DATE.strftime("%Y%m%d")
GRAPH_ID = "graph1"
ADD_GRAPH_VALUE = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"
GRAPH_VALUE_CREATION = {
    "date": DATE,
    "quantity":"10"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
response = requests.post(url = ADD_GRAPH_VALUE, json=GRAPH_VALUE_CREATION, headers = headers)

# Update a pixel
GRAPH_ID = "graph1"
USER_DATE = datetime(year=2022, month=12, day=18)

DATE = USER_DATE.strftime("%Y%m%d")

UPDATE_GRAPH_VALUE = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"

UPDATION_VALUE = {
    "quantity":"20"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.put(url=UPDATE_GRAPH_VALUE, json=UPDATION_VALUE, headers=headers)


# Delete a pixel
GRAPH_ID = "graph1"
USER_DATE = datetime(year=2022, month=12, day=19)

DATE = USER_DATE.strftime("%Y%m%d")

DELETE_PIXEL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.delete(url=DELETE_PIXEL,headers=headers)