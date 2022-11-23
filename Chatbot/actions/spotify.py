#########################################################
#                                                       #
# Query public transportation info from MVG.            #
#                                                       #
#                                                       #
# Author: Michael Eggers, michael.eggers@hm.edu         #
#########################################################


import requests
import json

SPOTIFY_URL = "https://api.spotify.com/v1"
# MVG_ROUTING_URL = "https://www.mvg.de/api/fahrinfo/routing"

# def name_to_station(name: str):
#     spotify_resp = requests.get(SPOTIFY_URL, params={"q": name})
    
#     if spotify_resp.status_code != requests.codes.ok:
#         return None
    
#     as_dict = spotify_resp.json()

#     musician = None
#     for location in as_dict["locations"]:
#         if location["type"] == "station":
#             musician = { "id": location["id"], "name": location["name"] }
#             break

#     return musician

# # Returns travel time in minutes
# def get_travel_time_for_stationIDs(station_a, station_b):
#     spotify_resp = requests.get(MVG_ROUTING_URL, params={ "fromStation": station_a, "toStation": station_b })

#     if spotify_resp.status_code != requests.codes.ok:
#         return None

#     as_dict = spotify_resp.json()

#     travel_time = None
#     for connection in as_dict["connectionList"]:
#         departure_time = connection["departure"]
#         arrival_time   = connection["arrival"]
#         delta_time_ms = arrival_time - departure_time
#         travel_time   = (delta_time_ms / 1000.0) / 60.0
#         break

#     return travel_time

"""def get_similar_musician():"""


# def handle_route(start, destination):
#     from_station  = name_to_station(start)
#     to_station    = name_to_station(destination)

#     if from_station and to_station:
#         print("Checking route from " + from_station["name"], from_station["id"] + " to " + to_station["name"], to_station["id"])
#     else:
#         error = "At least one unknown station!"
#         return json.dumps({"error": error})
    
#     travel_time = get_travel_time_for_stationIDs(from_station["id"], to_station["id"])
#     if travel_time:
#         result = {
#             "from": from_station["name"],
#             "to": to_station["name"],
#             "time_needed": travel_time
#         }
#         return json.dumps(result)        

#     else:
#         return json.dumps({"error": "could not calculate travel time for those stations!"})

# # Test
# # result = handle_route("Holzapfelkreuth", "Holzapfelkreuth")
# # print(result)