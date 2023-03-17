from datetime import datetime
from Services.calendarservices import calDAVServices
from Services.sttTest import SpeechToText
    
def createEvent(calDAVService: calDAVServices):
    month = int(input("Enter Month as Number: \n"))
    day = int(input("Enter Day as Number \n"))
    hour = int(input("Enter Hour: \n"))
    minute = int(input("Enter minutes: \n"))
    summary = input("Enter Title \n")
    try:
        date = datetime(datetime.today().year, month, day, hour, minute)
        calDAVService.createEvent(date, summary)
    except (ValueError, TypeError):
        print("Error")

def eventToday(calDAVService: calDAVServices):
    calDAVService.searchEventToday()

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
    stt = SpeechToText(5)
    stt.run()
    
main()