class queryBuilder:

    def __init__(self):
        self.data = []
    
    def itemToString(self, item):
        return str(item)
    
    def buildSentence(self):
        return " ".join(self.data)
    
    def eventCreated(self, eventname, date):
        self.data.append("Event Successfully Created, ", self.itemToString(eventname), ". At ", self.itemToString(date))
        return self.data

    def getEventsToday(self, events):
        for i in events:
            pass
    
