from calendarservices import calDAVServices

def main():
    calDavService = calDAVServices("http://localhost/dav.php", "test", "password")
    calDavService.getCalendars(calDavService.myprinciple)