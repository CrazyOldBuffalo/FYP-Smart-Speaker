from datetime import datetime
from calendarservices import calDAVServices
    

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
    #calParser.parseICS()
    #createEvent(calDAVService)
    #value = calDAVService.getCalendars()
    #ttsEngine.speakCalendars(value)
    #calendars = calDAVService.listCalendars()
    #print(calendars)
    #print(len(calDAVService.searchEventToday()))


 
main()