from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from . import spotify

class ActionArtist(Action):

    def name(self) -> Text:
        return "action_get_similar_artist"

    def run(self, dispatcher, tracker, domain):
        search = tracker.get_slot("search")
        if str(search).strip() == None:
            dispatcher.utter_message("Du hast doch noch garnichts eingegeben")
        else:
            result1, result2, result3, result4, result5, result6 = spotify.getRelatedArtist(search)

            answer = f"Ich hätte die hier für dich gefunden: {result1}"
            if result2 != "":
                answer = f"Ich hätte die hier für dich gefunden: {result1}, {result2}"
            if result3 != "":
                answer = f"Ich hätte die hier für dich gefunden: {result1}, {result2}, {result3}"
            if result4 != "":
                answer = f"Ich hätte die hier für dich gefunden: {result1}, {result2}, {result3}, {result4}"
            if result5 != "":
                answer = f"Ich hätte die hier für dich gefunden: {result1}, {result2}, {result3}, {result4}, {result5}"
            if result6 != "":
                answer = f"Ich hätte die hier für dich gefunden: {result1}, {result2}, {result3}, {result4}, {result5}, {result6}"
            
            if "error" in result1:
                dispatcher.utter_message("Sorry! Das habe ich nicht erkannt!")
            elif "No similar" in result1:
                dispatcher.utter_message("Ich kenne leider nichts ähnliches dazu")
            else:
                dispatcher.utter_message(answer)

        return []

class ActionTrack(Action):

    def name(self) -> Text:
        return "action_get_similar_track"

    def run(self, dispatcher, tracker, domain):
        search = tracker.get_slot("search")
        if str(search).strip() == None:
            dispatcher.utter_message("Du hast doch noch garnichts eingegeben")
        else:
            dispatcher.utter_message("Hier gibt es noch nichts zu sehen")

        return []

