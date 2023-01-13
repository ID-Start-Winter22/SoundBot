import requests
import markdown
import json

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
    info = str(info)[:str(info).find("</p>")].strip("<p>")

    #hier müsste der Text von HTML zu Markdown umgewandelt werden; Ich weiß noch nicht wie
    info = markdown.markdown(info, heading_style="ATX")
    return info

print(getInfo("Michael Jackson"))