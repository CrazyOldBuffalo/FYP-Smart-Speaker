import pyttsx3


class textToSpeechService:

    def __init__(self):
        self.engine = pyttsx3.init()

    def test(self):
        self.engine.say("Test to ensure working")
        self.engine.runAndWait()
