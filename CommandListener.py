import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from flask import Flask, request, make_response
from NoticeCrowler import NoticeCrowler
from CafeteriaCrowler import CafeteriaCrowler


token = ''
slack = Slacker(token)

cafeteriaUrl = 'https://coop.koreatech.ac.kr/dining/menu.php'
generalNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230'
scholarshipNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231'
bachelorNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'

app = Flask(__name__)

def get_answer():
    return "무슨 말인지 모르겠네요. "


# 이벤트 핸들하는 함수

def event_handler(event_type, slack_event):

    if event_type == "app_mention":

        channel = slack_event["event"]["channel"]

        userMessage = slack_event["event"]["blocks"][0]['elements'][0]['elements'][1]['text']

        text = get_answer()

        if '공지' in userMessage :
            req = requests.get(generalNoticUrl)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
    
            x = NoticeCrowler(generalNoticUrl, soup, slack)
            x.sendData()
        
        elif '학식' in userMessage :
            req = requests.get(cafeteriaUrl)
            html = req.text
            soup = BeautifulSoup(req.content.decode('euc-kr','replace'),'html.parser')

            x = CafeteriaCrowler(cafeteriaUrl, soup, slack)
            x.bringData().formatData().sendData()
            

        elif '안녕' in userMessage :
            text = '나는 *지마블루*. 진리를 쫓아 이곳까지 왔죠. \n시간이 얼마 남지 않았습니다. *이 활동이 저의 마지막이 될 것 입니다.*'
            slack.chat.post_message(channel, text)


        return make_response("앱 멘션 메시지가 보내졌습니다.", 200, )

    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다." % event_type

    return make_response(message, 200, {"X-Slack-No-Retry": 1})



@app.route("/slack", methods=["GET", "POST"])

def hears():

    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    if "event" in slack_event:

        event_type = slack_event["event"]["type"]

        return event_handler(event_type, slack_event)

    return make_response("슬랙 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)





""" 


print('명령 입력 : ', end = ' ')
command = input()

if command == '학식' :
    req = requests.get(cafeteriaUrl)
    html = req.text
    soup = BeautifulSoup(req.content.decode('euc-kr','replace'),'html.parser')

    x = CafeteriaCrowler(cafeteriaUrl, soup, slack)
    x.bringData().formatData().sendData()

elif command == '공지' :
    req = requests.get(generalNoticUrl)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    x = NoticeCrowler(generalNoticUrl, soup, slack)
    x.sendData()

else :
    pass

 """