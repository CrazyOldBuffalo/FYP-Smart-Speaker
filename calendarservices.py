# Install and setup the imports from external Libs.
# Done for the plugin to allow for interactions with the server.

import sys
from datetime import date
from datetime import datetime

sys.path.insert(0, "..");
sys.path.insert(0, ".");

import caldav

class calDAVServices:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.myprinciple = self.clientConnection(self.url, self.username, self.password);

    def getCalendars(self):
        calendars = self.myprinciple.calendars()
        self.listCalendars(calendars);

    def listCalendars(self, calendars):
        if calendars:
            print("You have %i calendars: " % len(calendars))
            for c in calendars:
                print(" Name: %-36s URL: %s" % (c.name, c.url))
        else:
            print("You have no calendars, Create One!")
    
    def createCalendar(self):
        new_calendar = self.myprinciple.make_calendar(name = "This is for Testing")
        return new_calendar

    def clientConnection(self, calDavUrl, uName, passW):
        with caldav.DAVClient(url=calDavUrl, username=uName, password=passW) as client:
            myprinciple = client.principal()
            return myprinciple