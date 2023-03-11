from datetime import datetime

class EventObj:
    def __init__(self, startdate, startime, enddate, endtime, summary):
        self.startdate = startdate
        self.starttime = startime
        self.enddate = enddate
        self.endtime = endtime
        self.title = summary

    
    def getStartDate(self) -> datetime:
        return self.startdate
    
    def getStartTime(self) -> datetime:
        return self.starttime
    
    def getStartDateTime(self) -> datetime:
        startdatetime = datetime.combine(self.startdate, self.starttime)
        return startdatetime
    
    def getEndDate(self) -> datetime:
        return self.enddate

    def getEndTime(self) -> datetime:
        return self.endtime
    
    def getEndDateTime(self) -> datetime:
        enddatetime = datetime.combine(self.enddate, self.endtime)
        return enddatetime
    
    def getSummary(self) -> str:
        return self.title

    def convertDTToString(self, dt: datetime) -> str:
        return str(dt)
        