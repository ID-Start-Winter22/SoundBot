import requests
import json

def getInfo(name: str):
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles={name}"
    res = requests.get(url=url).content
    json_data = json.loads(res)
    page = json_data["query"]["pages"]
    info = page
    return info

#print(getInfo("Eminem"))