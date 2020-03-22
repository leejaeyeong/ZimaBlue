
import datetime
from collections import OrderedDict
tag = '#intercity-timetable > div > table:nth-child(1) > tbody > tr:nth-child({}) > td:nth-child(1)'

# 표정 이미지 https://medibang.com/picture/d11801050948336930001071938/

class BusInformation :
    def __init__(self, soup) :
        self.soup = soup
        self.busTimeTable = []
        self.selector = None
        self.strNow = None
        self.target = -1
    
    # 버스 시간표를 읽어옴
    def crawling(self) :
        for i in range(16) :
            selector = self.soup.select(tag.format(i+1))
            self.busTimeTable.append(selector[0].text)
        return self
    
    # 가장 빠르게 출발하는 버스를 식별함, 
    def getNextBus(self) :
        if self.selector == None :
            self.crawling()
        self.strNow = datetime.datetime.now().strftime('%H:%M')
        timeNow = datetime.datetime.strptime(self.strNow, '%H:%M')
        self.target = -1 
        for i in range(len(self.busTimeTable)) :
            time = datetime.datetime.strptime(self.busTimeTable[i], '%H:%M')
            if time > timeNow :
                self.target = i 
                break
            if self.busTimeTable[i] == self.busTimeTable[-1] :
                self.target = 0
        return self.busTimeTable[self.target]
    
    def convertTimetoEmoji(self) :
        numberEmoji = [':zero:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']
        emoji = ''
        for i in self.busTimeTable[self.target] :
            emoji += ' : ' if i == ':' else numberEmoji[int(i)] + ' '
        return emoji
        
    def getOtherBus(self) :
        return self.busTimeTable[(self.target+1)%len(self.busTimeTable)],self.busTimeTable[(self.target+2)%len(self.busTimeTable)]
    
    # 도착하기 까지 남은 시간
    def getTimeToArrive(self) : 
        if self.strNow == None :
            self.getNextBus()
        nowHour = int(self.strNow.split(':')[0])
        nowMinute = int(self.strNow.split(':')[1])
        targetHour =  int(self.busTimeTable[self.target].split(':')[0])
        targetMinute = int(self.busTimeTable[self.target].split(':')[1])

        totalMinute = (targetHour*60+targetMinute) - (nowHour*60+nowMinute) if nowHour <= targetHour else ((24+targetHour)*60+targetMinute) - (nowHour*60+nowMinute)
        if totalMinute > 59 :
            return str(totalMinute // 60) + '시간' + str(totalMinute % 60) +'분'
        else :
            return str(totalMinute) + '분'
            
    def getAnswer(self) :
        self.getNextBus()
        jsonData = OrderedDict()
        jsonData['color'] = '#2398cf'
        jsonData['blocks'] = []
        jsonData['blocks'].append({'type' : 'section','text' : {"type": "mrkdwn","text": "*[대성고속] 부릉부릉 버스 곧 출발합니다. :oncoming_bus:*\n *곧 출발하는 버스 시간은* {}".format(self.convertTimetoEmoji())}})
        jsonData['blocks'].append({"type": "divider"})
        field = []
        field.append({"type": "mrkdwn","text": "*어디로?*\n`한기대 -> 야우리`"})
        field.append({"type": "mrkdwn","text": "*남은 시간*\n `{}`".format(self.getTimeToArrive())})
        field.append({"type": "mrkdwn","text": "*다음 버스*\n _{}_".format(self.getOtherBus()[0])})
        field.append({"type": "mrkdwn","text": "*그 다음 버스*\n _{}_".format(self.getOtherBus()[1])})
        field.append({"type": "mrkdwn","text": '*전체 버스 시간표*\n<{}|{}>'.format('https://hantalk.io/bus','보기')})
        jsonData['blocks'].append({'type' : 'section','fields' : field})
        #jsonData['blocks'].append({'type' : 'section','fields' : field, 'accessory' : {"type": "image","image_url": "https://raw.githubusercontent.com/leejaeyeong/ZimaBlue/master/reading_room_status.png","alt_text": "emotion"}})
        return jsonData



# businfo json example
""" 
bus = {
	"color" : '#2398cf',
    "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*[대성고속] 부릉부릉 버스 곧 출발합니다. :oncoming_bus:*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*어디로?*\n`한기대 -> 야우리`"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*남은 시간*\n `{}` 분".format(50)
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*다음 버스*\n{}".format('_07:00_')
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*그 다음 버스*\n{}".format('_08:20_')
                    },
					{
                        "type": "mrkdwn",
                        "text": '*전체 버스 시간표*\n<{}|{}>'.format('https://hantalk.io/bus','보기')
                    }

					
                ],
				"accessory": {
				"type": "image",
				"image_url": "https://raw.githubusercontent.com/leejaeyeong/ZimaBlue/master/reading_room_status.png"
                "alt_text": "Haunted hotel image"
			}
		}
    ]
}
 """