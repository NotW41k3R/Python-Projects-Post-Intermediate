import requests
import datetime as dt
import os

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")

GRAPH_ID = "graph" #Edit this for different graphs

# Creating User Account
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

# response = requests.post(url=pixela_url, json=parameters)
# print(response.text)


# Creating a new Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id' : GRAPH_ID,
    'name' : "Reading",
    'unit' : "Pages",
    'type' : "int",
    'color' : "sora",
    'startOnMonday' : True,
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Creating a new Pixel
today = dt.datetime.today()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    'date' : today.strftime("%Y%m%d"),
    'quantity' : input("How many pages did you read today? ")
}

response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)


# Code for Update and Delete
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "4.5"
# }
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)