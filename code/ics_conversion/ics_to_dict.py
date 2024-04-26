import datetime as dt
import json
import os

from pytz import timezone
from icalendar import Calendar, Event

def ics_to_dict(calendar_path : str):
    cal = Calendar.from_ical(open(calendar_path, "rb").read())
    event_list = []
    for component in cal.walk():
        if isinstance(component, Event):
            start_datetime = component.get("DTSTART").dt
            end_datetime = component.get("DTEND").dt

            start_paris = start_datetime.astimezone(timezone("Europe/Paris"))
            end_paris = end_datetime.astimezone(timezone("Europe/Paris"))

            event_list.append({
                "START" : str(start_paris),
                "END" : str(end_paris),
                "TITLE" : str(component.get("SUMMARY")),
                "LOCATION" : str(component.get("LOCATION")),
                "DESCRIPTION" : str(component.get("DESCRIPTION")),
                "COMMENTARY" : str(component.get("COMMENTAIRE")),
                "COLOR_ID" : "8"
            })

    return beautify_event_list(event_list)

def beautify_event_list(event_list : list) -> list:
    if not os.path.exists("./custom/color_custom.json") and not os.path.exists("./custom/title_custom.json"):
        os.mkdir("./custom/")
        f = open("./custom/color_custom.json", "x")
        f.close()
        f = open("./custom/title_custom.json", "x")
        f.close()

        

    colors : list
    with open("./custom/color_custom.json", "r") as color_file:
        buffer = color_file.read()
        if buffer != "":
            colors = json.loads(buffer).get("courses")
        else:
            colors = []
            print("Feel free to custom courses colors (custom/color_custom.json) !")

    titles : list 
    with open("./custom/title_custom.json", "r") as title_file:
        buffer = title_file.read()
        if buffer != "":
            titles = json.loads(buffer).get("courses")
        else:
            titles = []
            print("Feel free to custom courses title (custom/title_custom.json) !")

    for event in event_list:
        event["DESCRIPTION"] = event.get("DESCRIPTION").split("\n")[1]
        event["START"] = event.get("START").replace(" ", "T")
        event["END"] = event.get("END").replace(" ", "T")
        for course in colors:
            if course["course_code"] in event["TITLE"]:
                event["COLOR_ID"] = course["color_id"]
        for course in titles:
            if course["course_code"] in event["TITLE"]:
                event["TITLE"] = course["title"]
        if "Projet" in event["DESCRIPTION"] or "PROJET" in event["DESCRIPTION"] or "Projet" in event["DESCRIPTION"]:
            event["TITLE"] = "Projet"
            event["DESCRIPTION"] = "Projet"
            event["COLOR_ID"] = "6"
        if event["TITLE"] == "RES":
            event["TITLE"] = "Réservation"
            event["COLOR_ID"] = "11"
    return event_list

if __name__ == "__main__":
    ics_to_dict()