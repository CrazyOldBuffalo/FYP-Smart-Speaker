from ics import Calendar, Event
from datetime import datetime
from event import EventObj

class CalendarParser:
    
    def __init__(self):
      pass

    def parseICS (self, ics):
       calEvents = Calendar(ics)
       events = []
       objid = 0
       for e in calEvents.events:
          event_date = e._begin.date()
          event_time = e.begin.time()
          event_enddate = e.end.date()
          event_endtime = e.end.time()
          event_url = e.url()
          event_summary = e.name()
          objid = EventObj(event_date, event_time, event_enddate, event_endtime, event_summary, event_url)
          events.append(objid)
          objid = objid+1
        return events
        
