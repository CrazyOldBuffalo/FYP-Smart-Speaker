from datetime import datetime
from calendarservices import calDAVServices
from texttospeechservice import textToSpeechService

def createEvent(calDavService: calDAVServices):
    startmonth = int(input("Enter Month:"))
    startday = int(input("Enter Day:"))
    startTimehour = int(input("What Hour?"))
    startTimeMin = int(input("What Min?"))
    eventStartTime = datetime(datetime.now().year, startmonth, startday, startTimehour, startTimeMin)
    eventname = input("Name of the event")
    calDavService.createEventTest(eventStartTime, eventname)
    

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
    ttsEngine = textToSpeechService()

    ttsEngine.test()

    createEvent(calDAVService)
    #value = calDAVService.getCalendars()
    #ttsEngine.speakCalendars(value)
    #print(value)
    #calendars = calDAVService.listCalendars()
    #print(calendars)
    #print(len(calDAVService.searchEventToday()))


 
main()