import unittest
from Services.event import EventObj
from datetime import date, time, datetime


class TestEventObj(unittest.TestCase):
    def setUp(self):
        start_date_time = datetime(2023, 1, 1, 12, 0, 0)
        end_date_time = datetime(2023, 1, 2, 12, 0, 0)
        self.start_date = start_date_time.date()
        self.start_time = start_date_time.time()
        self.end_date = end_date_time.date()
        self.end_time = end_date_time.time()
        self.title = "Test Event"
        self.url = "https://www.google.com"

    def testEventObj(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        self.assertIsInstance(event, EventObj, "Event Created")
        self.assertEqual(event.get_start_date(), self.start_date, "Start Date Correct")
        self.assertEqual(event.get_start_time(), self.start_time, "Start Time Correct")
        self.assertEqual(event.get_end_date(), self.end_date, "End Date Correct")
        self.assertEqual(event.get_end_time(), self.end_time, "End Time Correct")
        self.assertEqual(event.get_summary(), self.title, "Title Correct")
        self.assertEqual(event.get_url(), self.url, "URL Correct")

    def testGetStartDayTime(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        self.assertEqual(event.get_start_date_time(), datetime.combine(self.start_date, self.start_time), "Start Day Time Correct")

    def testGetEndDayTime(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        self.assertEqual(event.get_end_date_time(), datetime.combine(self.end_date, self.end_time), "End Day Time Correct")

    def testConvertToString(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        obj = type(event.get_start_date_time())
        self.assertEqual(event.convert_dt_to_str(event.get_start_date_time()), str(datetime.combine(self.start_date, self.start_time)), "Event to String Correct")

    def testSetUrl(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        event.set_url("https://www.youtube.com")
        self.assertEqual(event.get_url(), "https://www.youtube.com", "URL Changed")

    def testSetStartDate(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        event.set_start_date(date(2023, 1, 2))
        self.assertEqual(event.get_start_date(), date(2023, 1, 2), "Start Date Changed")

    def testSetStartTime(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        event.set_start_time(time(12, 0, 0))
        self.assertEqual(event.get_start_time(), time(12, 0, 0), "Start Time Changed")

    def testSetEndDate(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        event.set_end_date(date(2023, 1, 3))
        self.assertEqual(event.get_end_date(), date(2023, 1, 3), "End Date Changed")

    def testSetEndTime(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        event.set_end_time(time(12, 0, 0))
        self.assertEqual(event.get_end_time(), time(12, 0, 0), "End Time Changed")

    def testSetSummary(self):
        event = EventObj(self.start_date, self.start_time, self.end_date, self.end_time, self.title, self.url)
        event.set_summary("New Title")
        self.assertEqual(event.get_summary(), "New Title", "Summary Changed")

if __name__ == '__main__':
    unittest.main()
