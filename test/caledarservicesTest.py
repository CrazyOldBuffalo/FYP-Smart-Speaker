from Services.calendarservices import CalDAVServices
import unittest
import caldav
import datetime


class TestCalendarServices(unittest.TestCase):

    def testCalendarServicesConnection(self):
        url = "http://localhost/dav.php"
        username = "test"
        password = "password"
        cal_dav_service = CalDAVServices(url, username, password)
        self.assertIsInstance(cal_dav_service, caldav.Principal, "Connection Successful")
        self.assertEqual(cal_dav_service.get_url(), "http://localhost/dav.php", "URL Correct")
        self.assertEqual(cal_dav_service.get_username(), username, "Username Correct")
        self.assertEqual(cal_dav_service.get_password(), password, "Password Correct")
        self.assertIsNotNone(cal_dav_service.get_my_principle())

    def testGetCalendars(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        calendars = cal_dav_service.get_calendars()
        self.assertGreaterEqual(len(calendars), 1, "Calendars Retrieved")

    def testCreateCalendar(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        calendar_name = "Test Calendar"
        new_calendar = cal_dav_service.create_calendar("Test Calendar")
        self.assertIsInstance(new_calendar, caldav.Calendar, "Calendar Created")
        self.assertEqual(new_calendar.get, calendar_name, "Calendar Name Correct")

    def testCreateEvent(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        start_date = datetime.datetime.now()
        summary = "Test Event"
        new_event = cal_dav_service.create_event(start_date, summary)
        self.assertIsNotNone(new_event, "Event Created")
        self.assertEqual(new_event.icalendar_component.get('DTSTART').dt, start_date, "Event Date Correct")
        self.assertEqual(new_event.icalendar_component.get('SUMMARY'), summary, "Event Summary Correct")

    def testCreateEventEnd(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        new_event = cal_dav_service.create_event_end(datetime.datetime.now(),
                                                     datetime.datetime.now() + datetime.timedelta(hours=1),
                                                     "Test Event")
        self.assertIsInstance(new_event, caldav.Event, "Event Created")

    def testSearchEventToday(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        event = cal_dav_service.create_event(datetime.datetime.now(), "Test Event")
        events = cal_dav_service.search_event_today()
        self.assertGreaterEqual(len(events), 1, "Events Found")

    def testSearchAllEvents(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        event = cal_dav_service.create_event(datetime.datetime.now(), "Test Event")
        events = cal_dav_service.search_all_events()
        self.assertGreaterEqual(len(events), 1, "Events Found")

    def testSearchEventByDate(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        event = cal_dav_service.create_event(datetime.datetime.now(), "Test Event")
        events = cal_dav_service.search_event_by_date(datetime.datetime.now())
        self.assertGreaterEqual(len(events), 1, "Events Found")

    def testSearchEventByDateRange(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        event = cal_dav_service.create_event(datetime.datetime.today() + datetime.timedelta(days=1), "Test Event")
        events = cal_dav_service.search_event_by_date_range(datetime.datetime.now(),
                                                            datetime.datetime.now() + datetime.timedelta(days=3))


if __name__ == '__main__':
    unittest.main()
