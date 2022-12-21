import requests
import json
import base64
import random

#Maximale Anzahl von Versuchen für das auswählen von Vorschlägen
maxTries = 15
alreadyRecommendedList = []

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

def artistNameToId(name):
    token = authToken()
    url = f"https://api.spotify.com/v1/search?type=artist&q={name}"
    headers = {"Authorization": "Bearer " + token}

    res = requests.get(url=url, headers=headers).content
    json_data = json.loads(res)
    artists = json_data["artists"]
    try:
        artId = artists["items"][0]["id"]
        return artId
    except:
        return "Not Found"

def alreadyRecommended(aRL: list, rel_art) -> bool:
    for num in range(len(aRL)):
        if rel_art in aRL[num]: return True
    return False

def chooseNewArt(json_data, aRL):
    stop = 0

    if len(json_data["artists"])-1 == 0:
        rel_art = json_data["artists"][0]["name"]
        return rel_art
    elif len(json_data["artists"])-1 < 0:
        rel_art = "No similar"
        return rel_art

    rel_art = json_data["artists"][random.randint(0, len(json_data["artists"])-1)]["name"]
    alreadyRec = alreadyRecommended(aRL, rel_art)
    while alreadyRec:
        rel_art = json_data["artists"][random.randint(0, len(json_data["artists"])-1)]["name"]
        alreadyRec = alreadyRecommended(aRL, rel_art)
        if stop == maxTries:
            alreadyRec = False
            rel_art = ""
        stop += 1
    
    return rel_art

def getRelatedArtist(name):
    token = authToken()
    id = artistNameToId(name)
    if id == "Not Found":
        return "error", "", "", "", "", ""

    url = f"https://api.spotify.com/v1/artists/{id}/related-artists"
    headers = {"Authorization": "Bearer " + token}

    try:
        res = requests.get(url=url, headers=headers).content
        json_data = json.loads(res)
    except:
        return "error", "error", "error", "error", "error", "error"

    rel_art1 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art1)

    if rel_art1 == "No similar":
        return "No similar", "", "", "", "", ""

    rel_art2 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art2)

    rel_art3 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art3)

    rel_art4 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art4)

    rel_art5 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art5)

    rel_art6 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art6)

    return rel_art1, rel_art2, rel_art3, rel_art4, rel_art5, rel_art6

#Tests
#print(authToken())
#print(artistNameToId("Michael Jackson"))
#print(getRelatedArtist("Michael Jackson"))
#print(getRelatedArtist("Metallica"))
#print(getRelatedArtist("Lorna Shore"))
#print(getRelatedArtist("Frost Clad"))
#print(artistNameToId("1111111111111111"))