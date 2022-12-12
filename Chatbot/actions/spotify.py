import requests
import json
import base64
import random

random.seed()

def authToken():
    url = "https://accounts.spotify.com/api/token"
    clientId = "ccc7b42e5a2c4b5c876ebd93641bbce6"
    clientSecret = "45ca423c757f4c69a736bbf22ae597e9"
    headers = {}
    data = {}

    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')


    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)

    token = r.json()['access_token']

    return token

# def name_to_artist(name: str, as_dict):
#     print(as_dict)

#     musician = None
#     try:
#         for art in range(len(as_dict["artists"]["items"])):
#             if name in as_dict["artists"]["items"][art]:
#                 musician = as_dict["artists"]["items"][art]
#     except:
#         if "No token provided" in as_dict["error"]["message"]:
#             return "No token provided"

#     return musician

# #Test
# #print(name_to_artist("Michael Jackson"))

# def name_to_song(name: str, as_dict):

#     print(as_dict)

#     song = None
#     try:
#         for track in range(len(as_dict["tracks"]["items"])):
#             if name in as_dict["tracks"]["items"][track]:
#                 song = as_dict["tracks"]["items"][track]
#     except:
#         if "No token provided" in as_dict["error"]["message"]:
#             return "No token provided"

#     return song

# def search(name: str, as_dict):
#     state = ""
#     loc_list = ["tracks", "artists", "albums"]

#     end = False
#     print(len(as_dict))

#     for loc in range(len(as_dict)):
#         if name in as_dict[int(loc)]:
#             state = str(as_dict[loc_list[loc]])
#             end = True
#             print(state)

#         if end:
#             if state == str(as_dict[loc]): return name_to_song(name, as_dict)
#             elif state == str(as_dict["artists"]): return name_to_artist(name, as_dict)
#             else: return "Not Found"

# # Test
# # print(search("Michael Jackson"))

# def similar(name):
#     token = authToken()
#     searchUrl = f"https://api.spotify.com/v1/search?type=album&include_external=audio&q={name}"
#     headers = {"Authorization": "Bearer " + token}

#     res = requests.get(url=searchUrl, headers=headers)

#     as_dict = json.dumps(res.json(), indent=2)
#     searched = search(name, as_dict)

#     if searched != "Not Found":
#         print("Checking for similarities to " + str(searched))
#     else:
#         return json.dumps({"error": searched})

#     if searched in as_dict["tracks"]: return "WIP"
#     elif searched in as_dict["artists"]["items"]:
#         return as_dict["artists"]["name"]
#     else:
#         print("status: No similarities")
#         return "No similarities found"

# Test
#similar("Michael Jackson")

def artistNameToId(name):
    token = authToken()
    url = f"https://api.spotify.com/v1/search?type=artist&q={name}"
    headers = {"Authorization": "Bearer " + token}

    res = requests.get(url=url, headers=headers).content
    json_data = json.loads(res)
    artists = json_data["artists"]
    artId = artists["items"][1]["id"]
    return artId

def getRelatedArtist(name):
    token = authToken()
    id = artistNameToId(name)
    url = f"https://api.spotify.com/v1/artists/{id}/related-artists"
    headers = {"Authorization": "Bearer " + token}

    res = requests.get(url=url, headers=headers).content
    json_data = json.loads(res)
    rel_art = json_data["artists"][random.randint(0, len(json_data["artists"]))]["name"]
    return rel_art

#Test
#print(getRelatedArtist("Michael Jackson"))