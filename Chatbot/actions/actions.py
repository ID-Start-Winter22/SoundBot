from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from . import spotify

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_get_similar_artist"

    def run(self, dispatcher, tracker, domain):
        search = tracker.get_slot("search")
        if search == None:
            dispatcher.utter_message("Das habe ich nicht erkannt")
        else:
            result1, result2, result3, result4, result5, result6 = spotify.getRelatedArtist(search)
            if "error" in result1:
                dispatcher.utter_message("Sorry! Das habe ich nicht erkannt!")
            else:
                dispatcher.utter_message(f"Ich hätte die hier für dich gefunden: {result1}, {result2}, {result3}, {result4}, {result5}, {result6}")

        return []

    #test
    #run()

