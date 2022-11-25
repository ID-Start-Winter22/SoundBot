# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from . import spotify
import json

# NOTE(Michael): We could use this action to store the name in
#                the TrackerStore (in memory database) or a persitent DB
#                such as MySQL. But we need to store a key-value pair 
#                to identify the user by id eg. (user_id, slotvalue)
class ActionStoreUserName(Action):

    def name(self) -> Text:
        return "action_store_name"
         
    def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        print("Sender ID: ", tracker.sender_id)

        return []


class ActionUserName(Action):

    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        if not username :
            dispatcher.utter_message(" Du hast mir Deinen Namen nicht gesagt.")
        else:
            dispatcher.utter_message(' Du bist {}'.format(username))

        return []

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_get_similar"

    def run(self, dispatcher, tracker, domain):
        search = tracker.get_slot("search")
        if search == None:
            dispatcher.utter_message("Das habe ich nicht erkannt")
        else:
            result = json.loads(spotify.similar(search))
            print(result)
            if "error" in result:
                print("FEHLER!!!!!!!!!!!!")
                dispatcher.utter_message("Sorry! Das habe ich nicht erkannt!")
            else:
                # dispatcher.utter_message("Du brauchst exakt: {} Minuten von {} nach {}. Gute Reise!".format(time_needed, origin, destination))
                dispatcher.utter_message("{}".format(result))

        return []

    #test
    #run()

