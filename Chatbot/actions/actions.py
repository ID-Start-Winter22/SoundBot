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
        #search ist die Variable "search", die vom Bot übergeben wird; sie repräsentiert das, was der user suchen will
        search = tracker.latest_message["text"]
        start = str(search).find('"')
        end = str(search).find('"', start+1)
        search = str(search)[start:end].strip('"')

        print(search)

        if str(search).strip('"').strip() == None:
            #Antwort, wenn nichts eingegeben wurde
            dispatcher.utter_message("Du hast doch noch garnichts eingegeben") #Fehlermeldung, wenn nichts eingegeben wurde
        else:
            result1, result2, result3, result4, result5, result6 = spotify.getRelatedArtist(search)

            #--------------------------------------------
            #Antwort bei erfolgreicher Anfrage
            answer = f"Ich hätte die hier für dich gefunden:\n{result1}"
            if result2 != "":
                answer = f"Ich hätte die hier für dich gefunden:\n{result1}\n{result2}"
            if result3 != "":
                answer = f"Ich hätte die hier für dich gefunden:\n{result1}\n{result2}\n{result3}"
            if result4 != "":
                answer = f"Ich hätte die hier für dich gefunden:\n{result1}\n{result2}\n{result3}\n{result4}"
            if result5 != "":
                answer = f"Ich hätte die hier für dich gefunden:\n{result1}\n{result2}\n{result3}\n{result4}\n{result5}"
            if result6 != "":
                answer = f"Ich hätte die hier für dich gefunden:\n{result1}\n{result2}\n{result3}\n{result4}\n{result5}\n{result6}"
            #--------------------------------------------

            if "error" in result1:
                #Fehlermeldung, wenn Artist nicht existiert
                dispatcher.utter_message("Wow! Nicht einmal ich kenne den Artist :o Versuche bitte einen anderen Namen.")
            elif "No similar" in result1:
                #Fehlermeldung, wenn es nichts Ähnliches zur Suche gibt
                dispatcher.utter_message("Ich kenne leider nichts ähnliches dazu") 
            else:
                #Ausgabe der Antwort, wenn die Anfrage erfolgreich war
                dispatcher.utter_message(answer)

        return []

class ActionTrack(Action):

    def name(self) -> Text:
        return "action_get_similar_track"

    def run(self, dispatcher, tracker, domain):
        #search ist die Variable "search", die vom Bot übergeben wird; sie repräsentiert das, was der user suchen will
        search = tracker.get_slot("search")
        if str(search).strip() == None:
            #Antwort, wenn nichts eingegeben wurde
            dispatcher.utter_message("Du hast doch noch garnichts eingegeben")
        else:
            #Ausgabe der Antwort, wenn die Anfrage erfolgreich war
            dispatcher.utter_message("Hier gibt es noch nichts zu sehen")

        return []

