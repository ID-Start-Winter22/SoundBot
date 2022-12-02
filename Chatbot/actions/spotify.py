#########################################################
#                                                       #
# Query public transportation info from MVG.            #
#                                                       #
#                                                       #
# Author: Michael Eggers, michael.eggers@hm.edu         #
#########################################################


import requests
import json

SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search?type=album&include_external=audio"
# MVG_ROUTING_URL = "https://www.mvg.de/api/fahrinfo/routing"

def name_to_artist(name: str, as_dict):
    
    #if spotify_resp.status_code != requests.codes.ok:
    #    return None

    # as_dict = {"artists": {"items": ["Metallica", "Michael Jackson"]}}

    print(as_dict)

    musician = None
    try:
        for art in range(len(as_dict["artists"]["items"])):
            if name in as_dict["artists"]["items"][art]:
                musician = as_dict["artists"]["items"][art]
    except:
        if "No token provided" in as_dict["error"]["message"]:
            return "No token provided"

    return musician

#Test
#print(name_to_artist("Michael Jackson"))

def name_to_song(name: str, as_dict):

    # as_dict = {"artists": {"items": ["Metallica", "Michael Jackson"]}}

    print(as_dict)

    song = None
    try:
        for track in range(len(as_dict["tracks"]["items"])):
            if name in as_dict["tracks"]["items"][track]:
                song = as_dict["tracks"]["items"][track]
    except:
        if "No token provided" in as_dict["error"]["message"]:
            return "No token provided"

    return song

def search(name: str, as_dict):
    #if spotify_resp.status_code != requests.codes.ok:
    #    return None
    
    # as_dict = {"tracks": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20", "items": []}, "artists": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20", "items": ["Metallica", "Michael Jackson"]}}

    loc_list = ["tracks", "artists", "albums"]

    for loc in range(len(as_dict)):
        print(loc)
        if name in as_dict[loc_list[loc]]["items"]:
            state = str(as_dict[loc_list[loc]])
            print(loc)
            print(state)

    # if state == str(as_dict["artists"]): print(1)

    if state == str(as_dict["tracks"]): return name_to_song(name, as_dict)
    elif state == str(as_dict["artists"]): return name_to_artist(name, as_dict)
    else: return "Not Found"

# print(search("Michael Jackson"))

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

def similar(name):
    #spotify_resp = requests.get(SPOTIFY_SEARCH_URL, params={"q": name})

    #as_dict = spotify_resp.json()

    as_dict = {"tracks": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20", "items": []}, "artists": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20", "items": ["Metallica", "Michael Jackson"]}}

    searched = search(name, as_dict)

    if searched != "Not Found":
        print("Checking for similarities to " + searched)
    else:
        return json.dumps({"error": searched})

    if searched in as_dict["tracks"]: return "WIP"
    elif searched in as_dict["artists"]:
        #SPOTIFY_RELATED_ARTIST_URL = "https://api.spotify.com/v1/artists/" + name + "/related-artists"
        #sim_art = requests.get(SPOTIFY_RELATED_ARTIST_URL, params={"q": name})
        #sa_dict = sim_art.json()
        sa_dict = {"artists": {"name": "Jackson 5"}}
        return sa_dict["artists"]["name"]
    else:
        return "No similarities found"
    
    # travel_time = get_travel_time_for_stationIDs(from_station["id"], to_station["id"])
    # if travel_time:
    #     result = {
    #         "from": from_station["name"],
    #         "to": to_station["name"],
    #         "time_needed": travel_time
    #     }
    #     return json.dumps(result)        

    # else:
    #     return json.dumps({"error": "could not calculate travel time for those stations!"})

# Test
# result = handle_route("Holzapfelkreuth", "Holzapfelkreuth")
# print(result)