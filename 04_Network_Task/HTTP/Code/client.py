import requests

#local host , port by default 5000, temprature page
URL = "http://127.0.0.1:5000/temperature"

#post requist to server to update temp value, json format
response_post = requests.post(URL, json={"value": 35})
#print this new value in terminal
print("POST response:", response_post.json())

#get reauist from server to pull the new value
response_get = requests.get(URL)
#print this value in termianl 
print("GET response:", response_get.json())

