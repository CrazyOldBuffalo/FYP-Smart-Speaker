import speech_recognition as speechRecognition
import time

class SpeechToText:

    def __init__(self, timeout):
        self.recognizer = speechRecognition.Recognizer()
        self.timeout = timeout

    def listen(self):
        with speechRecognition.Microphone() as source:
            print("listening now")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout = self.timeout)
            except speechRecognition.WaitTimeoutError:
                print("End of Speech Detected")
                return None

            return audio
    
    def recognize(self, audio):
        if audio is None:
            return None
        try:
            text = self.recognizer.recognize_google(audio)
            print("You Said: ", text)
        except speechRecognition.UnknownValueError:
            print("Could Not Understand")
        except speechRecognition.RequestError as e:
            print("Could Not get results")
    
    def run(self):
        while True:
            audio = self.listen()
            text = self.recognize(audio)

            if text is not None:
                print("Converted Text: ", text)
            time.sleep(self.timeout)
