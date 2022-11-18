import requests
import json

MVG_STATION_URL = "https://www.mvg.de/api/fahrinfo/location/queryWeb"
MVG_ROUTING_URL = "https://www.mvg.de/api/fahrinfo/routing"

mvg_resp = requests.get(MVG_STATION_URL)
    
as_dict = mvg_resp.json()

as_dict = json.load("json-file") # where <json-file> is any valid JSON file

print(as_dict)