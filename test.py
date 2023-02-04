from calendarservices import calDAVServices
from texttospeechservice import textToSpeechService

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
    ttsEngine = textToSpeechService()

    ttsEngine.test()
    
    value = calDAVService.getCalendars()
    ttsEngine.speakCalendars(value)
    #print(value)
    #calendars = calDAVService.listCalendars()
    #print(calendars)
    #print(len(calDAVService.searchEventToday()))

main()