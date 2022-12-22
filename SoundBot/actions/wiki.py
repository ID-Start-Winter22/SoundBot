import requests
import markdown
import json

def getInfo(name: str):
    url = f"https://de.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles={name}"
    res = requests.get(url=url).content
    json_data = json.loads(res)
    page = json_data["query"]["pages"]
    pageId = list(dict(page).keys())[0]
    info = page[str(pageId)]["extract"]
    info = str(info)[:str(info).find("</p>")].strip("<p>")
    info = markdown.markdown(info, heading_style="ATX")
    return info

print(getInfo("Michael Jackson"))