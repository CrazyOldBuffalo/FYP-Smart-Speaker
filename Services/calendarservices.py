# Install and setup the imports from external Libs.
# Done for the plugin to allow for interactions with the server.
# Imports the caldav library from pip install

import caldav
import sys
from datetime import datetime
from datetime import timedelta

sys.path.insert(0, "..")
sys.path.insert(0, ".")


# Class for the calDavServices
# Features all the functions for accessing the caldav server and manipulating events on it.
# Can be created in other classes as an object and interacted with from there.
class CalDAVServices:

    def __init__(self, url: str, username: str, password: str) -> None:
        self.__url = url
        self.__username = username
        self.__password = password
        self.__my_principle = self.client_connection(self.__url, self.__username, self.__password)

    # Initial connection to CalDav Server via client
    @staticmethod
    def client_connection(caldav_url: str, username: str, password: str) -> caldav.DAVClient.principal:
        try:
            client = caldav.DAVClient(url=caldav_url, username=username, password=password)
            my_principle = client.principal()
            return my_principle
        except Exception:
            print("Connection Failed")
            return Exception

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_url(self) -> str:
        return self.__url

    def get_my_principle(self) -> caldav.DAVClient.principal:
        return self.__my_principle

    def set_username(self, username: str) -> None:
        self.__username = username

    def set_password(self, password: str) -> None:
        self.__password = password

    def set_url(self, url: str) -> None:
        self.__url = url

    # Functions for interacting with the calendars
    # Getting All Calendar Information and Data
    def get_calendars(self) -> list[caldav.DAVClient.calendar]:
        try:
            calendars = self.__my_principle.calendars()
            return calendars
        except Exception:
            print("Failed to Retrieve Calendars")

    # Function for creating a calendar, Not used in project but there for other Usage if Required
    def create_calendar(self, calendar_name: str) -> caldav.DAVClient.calendar:
        try:
            new_calendar = self.__my_principle.make_calendar(name=calendar_name)
            return new_calendar
        except Exception:
            print("Failed to Create Calendar")

    # Functions for creating events
    # Function for creating a generic event that lasts 1 hour
    def create_event(self, start_date: datetime, title: str) -> caldav.Event:
        try:
            calendars = self.get_calendars()
            new_event = calendars[0].save_event(
                dtstart=start_date,
                dtend=start_date + timedelta(hours=1),
                summary=title
            )
            return new_event
        except Exception:
            print("Failed to Create Event")

    # Function for creating a generic event with an end time passed in
    def create_event_end(self, start_date: datetime, end_date: datetime, title: str) -> caldav.Event:
        try:
            calendars = self.get_calendars()
            new_event = calendars[0].save_event(
                dtstart=start_date,
                dtend=end_date,
                summary=title
            )
            return new_event
        except Exception:
            print("Failed to Create Event")

    # Functions for searching for events
    # Searches for an event today at current time for 24hrs later
    def search_event_today(self) -> list[caldav.Event]:
        try:
            calendar = self.get_calendars()
            search_results = calendar[0].search(
                start=datetime.today(),
                end=datetime.today() + timedelta(days=1),
                event=True,
                expand=False,
            )
            return search_results
        except Exception:
            print("Failed to Search for Event")

    # Searches for all Events on the Calendar
    def search_all_events(self) -> list[caldav.Event]:
        try:
            calendar = self.get_calendars()
            search_results = calendar[0].search(event=True, expand=False)
            return search_results
        except Exception:
            print("Failed to Search for Event")

    def search_event_by_date(self, start_date: datetime) -> list[caldav.Event]:
        try:
            calendar = self.get_calendars()
            events = calendar[0].search(
                start=start_date,
                end=start_date + timedelta(days=1),
                event=True,
                expand=False,
            )
            return events
        except Exception:
            print("Failed to Search for Event")

    def search_event_by_date_range(self, start_date: datetime, end_date: datetime) -> list[caldav.Event]:
        try:
            calendar = self.get_calendars()
            events = calendar[0].search(
                start=start_date,
                end=end_date,
                event=True,
                expand=False,
            )
            return events
        except Exception:
            print("Failed to Search for Event")

    # Searches for one event using the url
    def search_one_event(self, url) -> caldav.Event:
        try:
            calendar = self.get_calendars()
            item = calendar[0].event_by_url(url)
            return item
        except Exception:
            print("Failed to Search for Event")

    # Searches for an event from today to max setting for the summary
    def search_event_summary(self, start_date: datetime, summary: str) -> list[caldav.Event]:
        try:
            calendar = self.get_calendars()
            start_date = datetime.today()
            search_results = calendar[0].search(
                event=True,
                expand=False,
                start=start_date,
                end=datetime.max,
                summary=summary
            )
            return search_results
        except Exception:
            print("Failed to Search for Event")

    # Functions for deleting events
    def delete_event(self, summary: str, search_date: datetime) -> None:
        try:
            calendar = self.get_calendars()
            search_results = self.search_event_summary(search_date, summary)
            if len(search_results) > 1:
                print("Multiple Events Found")
            elif len(search_results) == 1:
                event = self.search_one_event(search_results[0].url)
                event.delete()
            else:
                print("No Events Found")
        except Exception:
            print("Failed to Delete Event")

    def delete_all_events(self) -> None:
        try:
            calendar = self.get_calendars()
            search_results = self.search_all_events()
            for event in search_results:
                event.delete()
        except Exception:
            print("Failed to Delete Events")