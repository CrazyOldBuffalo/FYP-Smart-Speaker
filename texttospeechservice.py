import pyttsx3
from ttsQueryBuilder import queryBuilder


class textToSpeechService:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.queryBuilder = queryBuilder()

    def test(self):
        self.engine.say("Test to ensure working")
        self.engine.runAndWait()

    def tester(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def eventCreated(self, startdate, eventname):
        test = queryBuilder.eventCreated(eventname, startdate)
        print(test)
        self.engine.say("Event Successfully Created")
        self.engine.say("Name: %s" % (eventname))
        self.engine.say("Time: %s" % (testdate))
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
