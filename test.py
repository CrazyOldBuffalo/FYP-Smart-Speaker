from datetime import datetime
from calendarservices import calDAVServices
from texttospeechservice import textToSpeechService
from calendarParser import CalendarParser

def createEvent(calDavService: calDAVServices, ttsEngine: textToSpeechService):
    startmonth = int(input("Enter Month:"))
    startday = int(input("Enter Day:"))
    startTimehour = int(input("What Hour?"))
    startTimeMin = int(input("What Min?"))
    eventStartTime = datetime(datetime.now().year, startmonth, startday, startTimehour, startTimeMin)
    eventname = input("Name of the event")
    returnevent = calDavService.createEventTest(eventStartTime, eventname)
    if not returnevent:
        ttsEngine.eventError()
    else:
        ttsEngine.eventCreated(eventStartTime, eventname)

    

def main():
    #calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
    ttsEngine = textToSpeechService()
    ttsEngine.tester()
    #createEvent(calDAVService)
    #value = calDAVService.getCalendars()
    #ttsEngine.speakCalendars(value)
    #print(value)
    #calendars = calDAVService.listCalendars()
    #print(calendars)
    #print(len(calDAVService.searchEventToday()))


 
main()