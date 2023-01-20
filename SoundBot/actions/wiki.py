import requests
import markdownify
import json

def joinParts(parts: list) -> str:
    info = ""
    for i in range(len(parts)):
        info = info + parts[i]
    return info

def getInfo(name: str):
    """gibt Infos zu einem gegebenen Namen aus"""
    #res, wie in spotify.py erklärt
    url = f"https://de.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles={name}"
    res = requests.get(url=url).content
    json_data = json.loads(res)

    #filtern nach dem Infotext
    page = json_data["query"]["pages"]
    pageId = list(dict(page).keys())[0]
    info = page[str(pageId)]["extract"]
    info = str(info)[:str(info).find("</p>")]

    #hier müsste der Text von HTML zu Markdown umgewandelt werden; Ich weiß noch nicht wie
    info = markdownify.markdownify(info)

    infoParts = info.split("**")
    info = joinParts(infoParts)
    infoParts = info.split("\n")
    info = joinParts(infoParts)

    return info

#print(getInfo("Michael Jackson"))