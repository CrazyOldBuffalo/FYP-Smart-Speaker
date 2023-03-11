# Install and setup the imports from external Libs.
# Done for the plugin to allow for interactions with the server.

import sys
from datetime import date
from datetime import datetime
from datetime import timedelta
from texttospeechservice import textToSpeechService
from calendarParser import CalendarParser

sys.path.insert(0, "..");
sys.path.insert(0, ".");

# Imports the caldav library from pip install
import caldav

# Class for the calDavServices
# Features all the functions for accessing the caldav server and manipulating events on it.
# Can be created in other classes as an object and interacted with from there.
class calDAVServices:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.myprinciple = self.clientConnection(self.url, self.username, self.password)
        self.ttsService = textToSpeechService()
        self.calParser = CalendarParser()

    # Getting All Calendar Information and Data
    def getCalendars(self):
        calendars = self.myprinciple.calendars()
        return calendars

    # Testing function
    def listCalendars(self):
        calendars = self.getCalendars();
        if calendars:
            print("You have %i calendars: " % len(calendars))
            for c in calendars:
                print(" Name: %-36s URL: %s" % (c.name, c.url))
        else:
            print("You have no calendars, Create One!")
    
    # Function for creating a calendar, Not used in project but there for testing
    def createCalendar(self, calendarName):
        new_calendar = self.myprinciple.make_calendar(name = calendarName)
        return new_calendar
    

    # Functions for creating events
    # Function for creating a generic event that lasts 1 hour
    def createEvent(self, startdate, title):
        calendars = self.getCalendars()
        new_event = calendars[0].save_event(
            dtstart = startdate,
            dtend = startdate + timedelta(hours=1),
            summary = title
        )
        event = self.calParser.parseICS(new_event)
        if(event is None):
            self.ttsService.eventError()
        else:
            self.ttsService.eventCreated(event.convertDTToString(event.getStartDate()), event.convertDTToString(event.getStartTime()), event.getSummary())

    # Function for creating a generic event with an endtime passed in
    def createEventEnd(self, startdate, enddate, title):
        calendars = self.getCalendars()
        new_event = calendars[0].save_event(
            dtstart = startdate,
            dtend = enddate,
            summary = title
        )
        event = self.calParser.parseICS(new_event)
        if(event is None):
            self.ttsService.eventError()
        else:
            self.ttsService.eventCreated(event.convertDTToString(event.getStartDate()), event.convertDTToString(event.getStartTime()), event.getSummary())

    # Functions for searching for events
    # Searches for an event today at current time for 24hrs later
    def searchEventToday(self):
        events = []
        calendar = self.getCalendars()
        search_results = calendar[0].search(
            start = datetime.today(),
            end = datetime.today() + timedelta(days=1),
            event=True,
            expand=False,
        )
        if(search_results is None):
            self.ttsService.searchEmpty()
        else:
            for i in search_results:
                ev = self.calParser.parseICS(i)
                events.append(ev)
            self.ttsService.listEventsToday(events)
    
    # Searches for all Events on the Calendar
    def searchAllEvent(self):
        events = []
        calendar = self.getCalendars()
        search_results = calendar[0].search(event=True, expand=False)
        if(search_results is None):
            self.ttsService.noEventsFound()
        else:
            for i in search_results:
                ev = self.calParser.parseICS(i)
                events.append(ev)
            self.ttsService.listEvents(events)
    
    # Searches for one event using the url
    def searchOneEvent(self, url):
        calendar = self.getCalendars()
        item = calendar[0].event_by_url(url)
        if(item is None):
            self.ttsService.noEventsFound()
        else:
            ev = self.calParser.parseICS(item)
            

    # Searches for an event from today to max setting for the summary
    def searchEventSummary(self, summary):
        calendar = self.getCalendars()
        starttime = datetime.today()
        search_results = calendar[0].search(
            event = True,
            expand = False,
            start = starttime,
            end = datetime.max(),
            summary = summary
        )
        return search_results
    
    # Functions for editing & deleting events - In Progress
    def editEvent(self, ics, summary, startDate, endDate):
        pass

    def deleteEvent(self, ics, summary):
        pass

    # Initial connection to CalDav Server via client
    def clientConnection(self, calDavUrl, uName, passW):
        with caldav.DAVClient(url=calDavUrl, username=uName, password=passW) as client:
            myprinciple = client.principal()
            return myprinciple