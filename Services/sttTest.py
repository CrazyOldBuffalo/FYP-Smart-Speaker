import speech_recognition as speechRecognition
import time

class SpeechToText:

    def __init__(self, timeout) -> None:
        self.__recognizer = speechRecognition.Recognizer()
        self.__timeout = timeout
        self.__audioData = None
    
        
    def getRecognizer(self) -> speechRecognition.Recognizer:
        return self.__recognizer
        
    def getTimeout(self) -> int:
        return self.__timeout

    def setNewTimeout(self, newTimeout):
        self.__timeout = newTimeout
    
    def listen(self) -> speechRecognition.AudioData:
        with speechRecognition.Microphone as Source:
            self.__audioData = self.__recognizer.listen(timeout=self.__timeout)
        return self.__audioData
    
    def recognitionGoogle(self):
        data = self.listen()
        text = self.__recognizer.recognize_google(data)
        return text
    
    def recognitionPocketSphinx(self):
        data = self.listen()
        text = self.__recognizer.recognize_sphinx(data)
        return text

    def recognition(self):
        try:
            value = self.recognitionGoogle()
            return value
        except (speechRecognition.RequestError, speechRecognition.UnknownValueError):
            try:
                value = self.recognitionPocketSphinx()
                return value
            except speechRecognition.UnknownValueError:
                print("Unable to get Text")
            except speechRecognition.RequestError: 
                print("No services available for Recognition")


