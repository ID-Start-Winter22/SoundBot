from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from . import spotify
import json

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_get_similar"

    def run(self, dispatcher, tracker, domain):
        search = tracker.get_slot("search")
        if search == None:
            dispatcher.utter_message("Das habe ich nicht erkannt")
        else:
            # result = json.loads(spotify.similar(search))
            result = spotify.similar(search)
            print(result)
            if "error" in result:
                print("FEHLER!!!!!!!!!!!!")
                dispatcher.utter_message("Sorry! Das habe ich nicht erkannt!")
            else:
                dispatcher.utter_message("Ich hätte das hier für dich gefunden: {}".format(result))

        return []

    #test
    #run()

