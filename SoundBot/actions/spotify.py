import requests
import json
import base64
import random
import os

#####res ist die Antwort die von der API zurückgegeben wird mit Hilfe von requests
#####url ist die API-Adresse und headers sind die zusätze, die der Adresse hinzugefügt werden
#####.content gibt den Inhalt aus
"""res = requests.get(url=url, headers=headers).content"""
#####json_data ist die zu einer json-Datei umgewandelte Response
"""json_data = json.loads(res)"""
#####erg ist ein Auschnitt an der Stelle "erg" in json_data
"""erg = json_data["erg"]"""

#Maximale Anzahl von Versuchen für das auswählen von Vorschlägen
maxTries = 15
#Liste mit den bereits gestellten Vorschlägen
alreadyRecommendedList = []

def authToken():
    """Gibt ein Token zurück"""
    #Das ist die Funktion fürs Token; hier nichts ändern
    url = "https://accounts.spotify.com/api/token"
    # client = open('/chat-team-9/SoundBot/actions/client.txt', 'r')
    # lines = []
    # for line in client:
    #     line = line.removesuffix("\n")
    #     lines.append(line)

    # clientId = str(lines[0])
    # clientSecret = str(lines[1])

    clientId = os.environ.get("CLIENTID")
    clientSecret = os.environ.get("CLIENTSECRET")

    print(clientId, clientSecret)

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
    """Gibt für den gegeben Artist-Name eine ID zurück"""
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

def alreadyRecommended(aRL: list, rec) -> bool:
    """Überprüft ob rec schon einmal vorgeschlagen wurde"""
    if rec in aRL: return True
    return False

def chooseNewArt(json_data, aRL):
    """Wählt einen neuen Artist aus"""
    stop = 0

    #überprüft, ob es nur einen ähnlichen Artist gibt
    if len(json_data["artists"])-1 == 0:
        rel_art = json_data["artists"][0]["name"]
        return rel_art
    #überprüft, ob es keine ähnlichen Artists gibt
    elif len(json_data["artists"])-1 < 0:
        rel_art = "No similar"
        return rel_art

    #wählt einen zufälligen Artist aus json_data["artists"] aus und speichert den Namen in rel_art
    rel_art = json_data["artists"][random.randint(0, len(json_data["artists"])-1)]["name"]
    #überprüft, ob rel_art schon vorgeschlagen wurde
    alreadyRec = alreadyRecommended(aRL, rel_art)
    #wenn das der Fall ist, wird neu ausgewählt, bis ein Artist gefunden wurde, der noch nicht vorgeschlagen wurde oder die maximale Anzahl an versuchen überschritten wurde
    while alreadyRec:
        rel_art = json_data["artists"][random.randint(0, len(json_data["artists"])-1)]["name"]
        alreadyRec = alreadyRecommended(aRL, rel_art)
        if stop == maxTries:
            alreadyRec = False
            rel_art = ""
        stop += 1
    
    return rel_art

def getRelatedArtist(name):
    """Sucht nach ähnlichen Artists zu dem gegebenen Namen"""
    token = authToken()
    id = artistNameToId(name)
    if id == "Not Found":
        return "error", "", "", "", "", ""

    url = f"https://api.spotify.com/v1/artists/{id}/related-artists"
    headers = {"Authorization": "Bearer " + token}

    #versucht die Anfrage an die API zu stellen
    try:
        res = requests.get(url=url, headers=headers).content
        json_data = json.loads(res)
    except:
        return "error", "error", "error", "error", "error", "error"

    #wählt den ersten Vorschlag aus
    rel_art1 = chooseNewArt(json_data, alreadyRecommendedList)
    alreadyRecommendedList.append(rel_art1)

    #wenn es nichts ähnliches zur Eingabe gibt, wird dieser Fehler zurückgegeben
    if rel_art1 == "No similar":
        return "No similar", "", "", "", "", ""

    #wenn kein Fehler vorhanden ist, werden die restlichen Vorschläge ausgewählt
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
print(authToken())
#print(artistNameToId("Michael Jackson"))
#print(getRelatedArtist("Michael Jackson"))
#print(getRelatedArtist("Metallica"))
#print(getRelatedArtist("Lorna Shore"))
#print(getRelatedArtist("Frost Clad"))
#print(artistNameToId("1111111111111111"))