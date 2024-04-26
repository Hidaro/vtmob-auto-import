from datetime import datetime
import json

import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Supprimer le fichier tocken.pickel si modification de cette variable
SCOPES = ["https://www.googleapis.com/auth/calendar"]

CREDENTIALS_FILE = "./credentials/calendar_credentials.json"

def get_calendar_service():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Sauvegarde
        with open("token.pickle", "wb") as token:
           pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)
    return service

def list_event(service, calendarId : str):
    list_gcalendar_events = []
    result = service.events().list(
        calendarId=calendarId,
        singleEvents=True,
        orderBy="startTime"
    ).execute()
    for item in result.get("items"):
        list_gcalendar_events.append(
            {
                "TITLE" : item.get("summary"),
                "START" : item.get("start").get("dateTime"),
                "END" : item.get("end").get("dateTime"),
                "ID" : item.get("id"),
                "COLOR_ID" : item.get("colorId")
            }
        )
    return list_gcalendar_events

def add_event(service, calendarId : str, titre: str, date_start : str, date_end : str, location : str, description : str, color_id : str):
    service.events().insert(
        calendarId=calendarId,
        body={
            "summary": titre,
            "description": description,
            "start": {"dateTime": date_start, "timeZone": "Europe/Paris"},
            "end": {"dateTime": date_end, "timeZone": "Europe/Paris"},
            "location" : location,
            "colorId" : color_id
        }
    ).execute()
      
def remove_event(service, calendarId : str, eventId : str):
    service.events().delete(
        calendarId=calendarId,
        eventId=eventId,
        sendUpdates="none"
    ).execute()

def main_event(event_array : list, calendarId : str):
    service = get_calendar_service()
    gcalendar_events = list_event(service, calendarId)

    index_gcalendar_delete = []
    index_ical_delete = []
    for i in range(len(gcalendar_events)): # LISTE DES EVENEMENT GOOGLE CALENDAR
        for j in range(len(event_array)): # LISTE DES EVENEMENT UPHF
            if(
                (gcalendar_events[i]["START"] == event_array[j]["START"]) 
                and (gcalendar_events[i]["END"] == event_array[j]["END"]) 
                and (gcalendar_events[i]["TITLE"] == event_array[j]["TITLE"])
                and (gcalendar_events[i]["COLOR_ID"] == event_array[j]["COLOR_ID"])
            ):
                index_gcalendar_delete.append(i)
                index_ical_delete.append(j)
                break

    to_del : None
    while len(index_gcalendar_delete) > 0:
        to_del = index_gcalendar_delete[0]
        del gcalendar_events[to_del]
        del index_gcalendar_delete[0]
        for i in range(len(index_gcalendar_delete)):
            index_gcalendar_delete[i] = index_gcalendar_delete[i] - 1


    to_del : None
    while len(index_ical_delete) > 0:
        to_del = index_ical_delete[0]
        del event_array[to_del]
        del index_ical_delete[0]
        for i in range(len(index_ical_delete)):
            index_ical_delete[i] = index_ical_delete[i] - 1


    # Supression des évènements Google Calendar en trop
    gcalendar_to_del = len(gcalendar_events)
    if gcalendar_to_del != 0:
        print(f"{gcalendar_to_del} will be deleted from Google Calendar !")
        for event_gcalendar in gcalendar_events:
            remove_event(service, calendarId, event_gcalendar["ID"])
        print(f"Succesfully deleted {gcalendar_to_del} events.")
    else:
        print("No events to delete.")
    

    # Ajout des évènements provenant du .ics manquants
    ical_to_del = len(event_array)
    if ical_to_del != 0:
        print(f"{ical_to_del} will be added to Google Calendar !")
        for event_ical in event_array:
            add_event(service, calendarId, event_ical["TITLE"], event_ical["START"], event_ical["END"], event_ical["LOCATION"], event_ical["DESCRIPTION"], event_ical["COLOR_ID"])
        print(f"Succesfully added {ical_to_del} events.")
    else:
        print("No events to add.")

    
