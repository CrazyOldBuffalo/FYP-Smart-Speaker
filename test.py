from calendarservices import calDAVServices

def main():
    calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")

    value = calDAVService.getCalendars()
    print(value)


main()