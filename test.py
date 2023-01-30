from calendarservices import calDAVServices

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")

    newcal = calDAVService.createCalendar()
    print(newcal)
    value = calDAVService.getCalendars()
    print(value)


main()