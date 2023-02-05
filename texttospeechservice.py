import pyttsx3


class textToSpeechService:

    def __init__(self):
        self.engine = pyttsx3.init()

    def test(self):
        self.engine.say("Test to ensure working")
        self.engine.runAndWait()

    def tester(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


    def speakCalendars(self, output):
        if output:
            self.engine.say("You have %i calendars: " % len(output))
            for c in output:
                self.engine.say(" Name: %-36s URL: %s" % (c.name, c.url))
        else:
            self.engine.say("You have no calendars, Create One!")
        self.engine.runAndWait()