# Install and setup the imports from external Libs.
# Done for the plugin to allow for interactions with the server.

import sys
from datetime import date
from datetime import datetime

sys.path.insert(0, "..");
sys.path.insert(0, ".");

import caldav

class calDAVServices:
    myprinciple = 0

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        calDAVServices.myprinciple = self.clientConnection(self.username, self.password)
        
    def getCalendars(self, my_principle):
            calendars = my_principle.calendars(calendars)
            self.listCalendars(calendars);

    def listCalendars(calendars):
        if calendars:
            print("You have %i calendars: " % len(calendars))
            for c in calendars:
                print(" Name: %-36s URL: %s" % (c.name, c.url))
        else:
            print("You have no calendars, Create One!")
        
    def createCalendar():
        pass

    def clientConnection(url, username, password):
        with caldav.DAVClient(url=url, username=username, password=password) as client:
            my_principle = client.principal()