from datetime import datetime

import pyttsx3
from Services.event import EventObj


class TextToSpeechService:

    def __init__(self):
        self.engine = pyttsx3.init()

    def test(self):
        self.engine.say("Test to ensure working")
        self.engine.runAndWait()

    def tester(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def eventCreated(self, startdate : datetime, startime, eventname):
        self.engine.say("Event Successfully Created.")
        self.engine.say("Name: %s," % (eventname))
        self.engine.say("On %s," % (startdate))
        self.engine.say("At: %s" % (startime))
        self.engine.runAndWait()

    def listEventsToday(self, events: list[EventObj]):
        self.engine.say("There are %s Events Today" % (len(events)))
        for i in events:
            self.engine.say("%s: " % (i))
            self.engine.say("Name: %s," % (i.getSummary()))
            self.engine.say("On: %s," % (i.getStartDate()))
            self.engine.say("At: %s" % (i.getStartTime()))
            self.engine.runAndWait()

    def listEvents(self, events: list[EventObj]):
        self.engine.say("There are %s Events in the Calendar" % (len(events)))
        for i in events:
            self.engine.say("Name: %s," % (i.getSummary()))
            self.engine.say("On: %s," % (i.getStartDate()))
            self.engine.say("At: %s" % (i.getStartTime()))
            self.engine.runAndWait()

    def noEventsFound(self):
        self.engine.say("Sorry, no events found")
        self.engine.runAndWait()

    def eventError(self):
        self.engine.say("Error Occurred Creating Event, Please Try again!")
        self.engine.runAndWait()

    def speakCalendars(self, output):
        if output:
            self.engine.say("You have %i calendars: " % len(output))
            for c in output:
                self.engine.say(" Name: %-36s URL: %s" % (c.name, c.url))
        else:
            self.engine.say("You have no calendars, Create One!")
        self.engine.runAndWait()
