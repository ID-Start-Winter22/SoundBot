#########################################################
#                                                       #
# Query public transportation info from MVG.            #
#                                                       #
#                                                       #
# Author: Michael Eggers, michael.eggers@hm.edu         #
#########################################################


import requests
import json

MVG_STATION_URL = "https://www.mvg.de/api/fahrinfo/location/queryWeb"
MVG_ROUTING_URL = "https://www.mvg.de/api/fahrinfo/routing"

def name_to_station(name: str):
    mvg_resp = requests.get(MVG_STATION_URL, params={"q": name})
    
    if mvg_resp.status_code != requests.codes.ok:
        return None
    
    as_dict = mvg_resp.json()

    station = None
    for location in as_dict["locations"]:
        if location["type"] == "station":
            station = { "id": location["id"], "name": location["name"] }
            break

    return station

# Returns travel time in minutes
def get_travel_time_for_stationIDs(station_a, station_b):
    mvg_resp = requests.get(MVG_ROUTING_URL, params={ "fromStation": station_a, "toStation": station_b })

    if mvg_resp.status_code != requests.codes.ok:
        return None

    as_dict = mvg_resp.json()

    travel_time = None
    for connection in as_dict["connectionList"]:
        departure_time = connection["departure"]
        arrival_time   = connection["arrival"]
        delta_time_ms = arrival_time - departure_time
        travel_time   = (delta_time_ms / 1000.0) / 60.0
        break

    return travel_time

def handle_route(start, destination):
    from_station  = name_to_station(start)
    to_station    = name_to_station(destination)

    if from_station and to_station:
        print("Checking route from " + from_station["name"], from_station["id"] + " to " + to_station["name"], to_station["id"])
    else:
        error = "At least one unknown station!"
        return json.dumps({"error": error})
    
    travel_time = get_travel_time_for_stationIDs(from_station["id"], to_station["id"])
    if travel_time:
        result = {
            "from": from_station["name"],
            "to": to_station["name"],
            "time_needed": travel_time
        }
        return json.dumps(result)        

    else:
        return json.dumps({"error": "could not calculate travel time for those stations!"})

# Test
# result = handle_route("Holzapfelkreuth", "Holzapfelkreuth")
# print(result)