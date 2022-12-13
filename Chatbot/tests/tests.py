# import requests
# import string
# import random

# client_id = "ccc7b42e5a2c4b5c876ebd93641bbce6"
# redirect_uri = "http://localhost:8888/callback"

# state = "".join(random.choices(string.ascii_letters + string.digits, k=16))
# # print("state:", state)
# payload = {"response_type" : "code", "client_id" : client_id, "redirect_uri" : redirect_uri, "state" : state}

# login = requests.get("https://accounts.spotify.com/authorize", payload)

# print(login.status_code)
# print("-"*20)
# print(login)

#//////////////////////////////////////////////////////////////////////

# import requests
# import base64

# client_id = "ccc7b42e5a2c4b5c876ebd93641bbce6"
# client_secret = "45ca423c757f4c69a736bbf22ae597e9"
# url = "https://accounts.spotify.com/api/token"

# plc = "Basic " + client_id + ':' + client_secret
# plc = base64.urlsafe_b64encode(plc.encode()).decode()

# authOpt = {"Authorization" : plc, "grant_type" : "client_credentials", "json" : True}

# login = requests.post(url, authOpt)

# print(login.status_code)
# print(login.text)

#//////////////////////////////////////////////////////////////////////

# SPOTIFY_TOKEN = "https://accounts.spotify.com/api/token"
# request_body = {
#     "grant_type": GRANT_TYPE,
#     "code": code,
#     "redirect_uri": REDIRECT_URI,
#     "client_id": client_id,
#     "client_secret": client_secret,
# }
# r = requests.post(url=SPOTIFY_TOKEN, data=request_body)
# resp = r.json()

#//////////////////////////////////////////////////////////////////////

# import requests
# import base64
# import json

# url = "https://accounts.spotify.com/api/token"
# clientId = "ccc7b42e5a2c4b5c876ebd93641bbce6"
# clientSecret = "45ca423c757f4c69a736bbf22ae597e9"
# headers = {}
# data = {}

# message = f"{clientId}:{clientSecret}"
# messageBytes = message.encode('ascii')
# base64Bytes = base64.b64encode(messageBytes)
# base64Message = base64Bytes.decode('ascii')


# headers['Authorization'] = f"Basic {base64Message}"
# data['grant_type'] = "client_credentials"

# r = requests.post(url, headers=headers, data=data)

# token = r.json()['access_token']

# print("Access Token:")
# print(token)

# search = "Miachael Jackson"
# searchUrl = f"https://api.spotify.com/v1/search?type=album&include_external=audio&q={search}"
# headers = {
#     "Authorization": "Bearer " + token
# }

# res = requests.get(url=searchUrl, headers=headers)

# print(json.dumps(res.json(), indent=2))