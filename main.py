import json
import os

from code.uphf.get_login_token import main_token
from code.uphf.get_and_save_calendar import main_calendar
from code.ics_conversion.ics_to_dict import ics_to_dict
from code.gcalendar.sync_events import main_event

def main(calendarId : str):
    # Step 0 : Get credentials to log in to UPHF
    if not os.path.exists("./credentials/uphf_credentials.json"):
        os.mkdir("./credentials")
        with open("./credentials/uphf_credentials.json", "w") as credentials_file:
            credentials_file.write(json.dumps({
                "username" : input("Enter UPHF username : "),
                "password" : input("Enter password : ")
            }))
    

    with open("./credentials/uphf_credentials.json", "r") as credentials_file:
        credentials : dict = json.load(credentials_file)
    
    username : str = credentials.get("username")
    password : str = credentials.get("password")

    print(f"""Credentials from user {username} fetched !""")
    
    # Step 1 : Get token from logging in
    user_token : str = main_token(username, password)
    print(f"Token obtained : {user_token}")

    # Step 2 : Get the .ics calendar and save in ../result folder
    ics_calendar_path : str = main_calendar(user_token)
    print(f"Calendar fetched and succesfully saved at {ics_calendar_path} !")

    # Step 3 : Ask user if the program should auto-import to Google Calendar
    while True:
        choice : str = input("Auto-import to Google Calendar ? [Y/N] : ")
        if choice.upper() == "Y":
            break
        elif choice.upper() == "N":
            return 0
        else:
            print("Please answer by Y or N to continue or Ctrl+C to force exit")
    
    # Step 4 : Convert .ics file to an array of objects containing events information
    event_array : list = ics_to_dict(ics_calendar_path)
    print("Events converted to an array !")

    # Step 5 : Sync events to GCalendar
    if not os.path.exists("./credentials/calendar_credentials.json"):
        print("Please follow the documentation (documentation/help_credentials) in order to import to Google Calendar.")
        return 0
    else:
        main_event(event_array, calendarId)
        print("Google Calendar is now synchronized !")


if __name__ == "__main__":
    calendarId = "" # Calendar ID
    main(calendarId)