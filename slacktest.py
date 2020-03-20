import json
import requests
from bs4 import BeautifulSoup
import datetime, time

req = requests.get('https://hantalk.io/bus')

tag = '#intercity-timetable > div > table:nth-child(1) > tbody > tr:nth-child({}) > td:nth-child(1)'

#intercity-timetable > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(1)
html = req.text
soup = BeautifulSoup(html, 'html.parser')


# strptime - 문자열을 datetime
# strftime - datetime 문자열로
busTimeTable = []
for i in range(16) :
    selector = soup.select(tag.format(i+1))
    busTimeTable.append(selector[0].text)
print(busTimeTable)

strNow = datetime.datetime.now().strftime('%H:%M')
timeNow = datetime.datetime.strptime(strNow, '%H:%M')

target = -1 
for i in range(len(busTimeTable)) :
    time = datetime.datetime.strptime(busTimeTable[i], '%H:%M')
    if time > timeNow :
        target = i
        break
    if busTimeTable[i] == busTimeTable[-1] :
        target = 0

#print(busTimeTable[target])

#print('다음 , 그 다음 버스는')
#print(busTimeTable[(target+1)%len(busTimeTable)],busTimeTable[(target+2)%len(busTimeTable)])

# 몇분인지 계산하는 함수
nowHour = int(strNow.split(':')[0])
nowMinute = int(strNow.split(':')[1])
targetHour =  int(busTimeTable[target].split(':')[0])
targetMinute = int(busTimeTable[target].split(':')[1])
print('now : {}, target : {}'.format(nowHour,targetHour))

# 24시 기준으로 다음 배차 시간이 현재 시간보다 크면 
totalMinute = (targetHour*60+targetMinute) - (nowHour*60+nowMinute) if nowHour <= targetHour else ((24+targetHour)*60+targetMinute) - (nowHour*60+nowMinute)
if totalMinute > 59 :
    print(str(totalMinute // 60) + '시간' + str(totalMinute % 60) +'분')
else :
    print(totalMinute + '분')