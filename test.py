from datetime import datetime
from calendarservices import calDAVServices
from texttospeechservice import textToSpeechService
from calendarParser import CalendarParser
from datetime import datetime
from datetime import timedelta
    

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
    ttsEngine = textToSpeechService()
    ttsEngine.tester()
    calParser = CalendarParser()
    #calParser.parseICS()
    #createEvent(calDAVService)
    #value = calDAVService.getCalendars()
    #ttsEngine.speakCalendars(value)
    #calendars = calDAVService.listCalendars()
    #print(calendars)
    #print(len(calDAVService.searchEventToday()))


 
main()