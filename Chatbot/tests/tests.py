import requests
import json
import string
import random

client_id = "ccc7b42e5a2c4b5c876ebd93641bbce6"
redirect_uri = "http://localhost:8888/callback"

state = "".join(random.choices(string.ascii_letters + string.digits, k=16))
# print("state:", state)
payload = {"response_type" : "code", "client_id" : client_id, "redirect_uri" : redirect_uri, "state" : state}

login = requests.get("https://accounts.spotify.com/authorize", payload)

print(login.status_code)
print("-"*20)
print(login)

#//////////////////////////////////////////////////////////////////////