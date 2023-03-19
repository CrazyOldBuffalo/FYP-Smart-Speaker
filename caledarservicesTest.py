import requests
from Services.calendarservices import calDAVServices
import unittest
import caldav
class TestCalendarServices(unittest.TestCase):

    def testCalendarServicesConnection(self):
        try:
            calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
            self.assertIsInstance(calDAVService, calDAVServices, "Connected to CalDAV Server")
        except:
            self.fail("Connection Failed")
    
    def testCalendarServicesCreateEvent(self):
        try:
            calDAVService = calDAVServices("http://localhost/dav.php", "test", "password")
            calDAVService.createEvent(datetime.today(), "Test Event")
            self.assertTrue(True, "Event Created")
        except:
            self.fail("Event Creation Failed")
        
if __name__ == '__main__':
    unittest.main()

