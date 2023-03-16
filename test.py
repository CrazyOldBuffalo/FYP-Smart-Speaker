from datetime import datetime
from Services.calendarservices import calDAVServices
    
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
    menu = True
    while menu:
        mode = input("Press A for creating, B for events today")
        match mode:
            case 'A':
                menu = False
                createEvent(calDAVService)
            case 'B':
                menu = False
                eventToday(calDAVService)
 
main()