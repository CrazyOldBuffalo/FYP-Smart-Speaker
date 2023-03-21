from Services.calendarservices import CalDAVServices
import unittest
import caldav
import datetime


class TestCalendarServices(unittest.TestCase):

    def setUp(self) -> None:
        self.start_date = datetime.datetime(2023, 1, 1, 12, 0, 0)
        self.end_date = self.start_date + datetime.timedelta(days=1)
        self.title = "Test Event"
        self.url = "http://localhost/dav.php"
        self.username = "test"
        self.password = "password"

    def cleanUp(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        cal_dav_service.delete_all_events()
    def testCalendarServicesConnection(self):
        url = "http://localhost/dav.php"
        username = "test"
        password = "password"
        cal_dav_service = CalDAVServices(url, username, password)
        self.assertIsInstance(cal_dav_service, CalDAVServices, "Connection Successful")
        self.assertEqual(cal_dav_service.get_url(), "http://localhost/dav.php", "URL Correct")
        self.assertEqual(cal_dav_service.get_username(), username, "Username Correct")
        self.assertEqual(cal_dav_service.get_password(), password, "Password Correct")
        self.assertIsInstance(cal_dav_service.get_my_principle(), caldav.Principal, "Principal Retrieved")

    def testGetCalendars(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        calendars = cal_dav_service.get_calendars()
        self.assertGreaterEqual(len(calendars), 1, "Calendars Retrieved")

    def testCreateCalendar(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        calendar_name = self.title
        new_calendar = cal_dav_service.create_calendar(self.title)
        self.assertIsInstance(new_calendar, caldav.Calendar, "Calendar Created")
        self.assertEqual(new_calendar.name, self.title, "Calendar Name Correct")

    def testCreateEvent(self):
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        start_date = self.start_date.replace(microsecond=0)
        new_event = cal_dav_service.create_event(start_date, self.title)
        event_without_timezone = new_event.icalendar_component.get('DTSTART').dt.replace(tzinfo=None)
        self.assertIsNotNone(new_event, "Event Created")
        self.assertEqual(event_without_timezone, start_date, "Event Date Correct")
        self.assertEqual(new_event.icalendar_component.get('SUMMARY'), self.title, "Event Summary Correct")
        self.cleanUp()

    def testCreateEventEnd(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        new_event = cal_dav_service.create_event_end(self.start_date,
                                                     self.end_date,
                                                     self.title)
        self.assertIsInstance(new_event, caldav.Event, "Event Created")
        self.cleanUp()

    def testSearchEventToday(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        event = cal_dav_service.create_event(self.start_date, self.title)
        events = cal_dav_service.search_event_today()
        self.assertGreaterEqual(len(events), 1, "Events Found")
        self.cleanUp()

    def testSearchAllEvents(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        event = cal_dav_service.create_event(self.start_date, self.title)
        events = cal_dav_service.search_all_events()
        self.assertGreaterEqual(len(events), 1, "Events Found")
        self.cleanUp()

    def testSearchEventByDate(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        event = cal_dav_service.create_event(self.start_date, self.title)
        events = cal_dav_service.search_event_by_date(datetime.datetime.now())
        self.assertGreaterEqual(len(events), 1, "Events Found")
        self.cleanUp()

    def testSearchEventByDateRange(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        event = cal_dav_service.create_event(self.start_date + datetime.timedelta(days=1), "Test Event")
        events = cal_dav_service.search_event_by_date_range(self.start_date,
                                                            self.end_date + datetime.timedelta(days=2))
        self.assertGreaterEqual(len(events), 1, "Events Found")
        self.cleanUp()

    def testSearchOneEvent(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        test_event = cal_dav_service.create_event(self.start_date, self.title)
        event = cal_dav_service.search_one_event(test_event.url)
        self.assertIsNotNone(event)
        self.cleanUp()

    def testSearchEventSummary(self):
        cal_dav_service = CalDAVServices(self.url, self.username, self.password)
        test_event = cal_dav_service.create_event(self.start_date, self.title)
        event = cal_dav_service.search_event_summary(self.start_date, self.title)
        self.assertIsNotNone(event)
        self.cleanUp()
    def testDeleteEvent(self):
        summary = "Test Event"
        start_date = datetime.datetime.now()
        cal_dav_service = CalDAVServices("http://localhost/dav.php", "test", "password")
        test_event = cal_dav_service.create_event(start_date, summary)
        event_list_before = cal_dav_service.search_all_events()
        cal_dav_service.delete_event(summary, start_date)
        event_list_after = cal_dav_service.search_all_events()
        self.assertGreater(len(event_list_before), len(event_list_after), "Event Deleted")

if __name__ == '__main__':
    unittest.main()
