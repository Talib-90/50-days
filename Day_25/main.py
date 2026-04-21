import requests
from datetime import datetime

TOKEN = "klasdjnviewahvlkfdasjasdfqwe"
USERNAME = "talibilahi"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}


graph_config = {
    "id":"coding1",
    "name":"Coding graph",
    "unit":"hours",
    "type":"float",
    "color":"ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2026, month=4, day=19)

pixela_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"4"
}

# get_graph = f"{pixela_endpoint}/{USERNAME}/graphs/coding1"
# response = requests.post(url=get_graph, json=pixela_params, headers=headers)
# print(response.text)

# Update request
get_graph = f"{pixela_endpoint}/{USERNAME}/graphs/coding1/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity":"4"
}
# response = requests.put(url=get_graph, json=update_data, headers=headers)
# print(response.text)

# Delete request
response = requests.delete(url=get_graph, headers=headers)
print(response.text)