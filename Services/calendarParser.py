from event import EventObj


class CalendarParser:

    def __init__(self):
        pass

    def parseICS(self, ics):
        title = ics.icalendar_component.get('SUMMARY')
        starttimestamp = ics.icalendar_component.get('DTSTART').dt
        endtimestamp = ics.icalendar_component.get("DTEND").dt
        startdate = starttimestamp.date()
        starttime = starttimestamp.time()
        enddate = endtimestamp.date()
        endtime = endtimestamp.time()
        event = EventObj(startdate, starttime, enddate, endtime, title)
        return event

