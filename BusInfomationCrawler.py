
import datetime
tag = '#intercity-timetable > div > table:nth-child(1) > tbody > tr:nth-child({}) > td:nth-child(1)'

# 표정 이미지 https://medibang.com/picture/d11801050948336930001071938/

class BusInformation :
    def __init__(self, soup, slack) :
        self.soup = soup 
        self.slack = slack
        self.Message = ''
        self.busTimeTable = []
        self.selector = None
    
    def Crawling(self) :
        for i in range(16) :
            selector = self.soup.select(tag.format(i+1))
            self.busTimeTable.append(selector[0].text)
        return self
    
    def getNextBus(self) :
        if self.selector == None :
            self.crawling()
        now = datetime.datetime.now().strftime('%H:%M')
        now = datetime.datetime.strptime(now, '%H:%M')
        target = -1 
        for i in self.busTimeTable :
            time = datetime.datetime.strptime(i, '%H:%M')
            if time > now :
                target = i 
                break
            if i == self.busTimeTable[-1] :
                target = self.busTimeTable[0]
        return target
    
    def getOtherBus(self) :
        




