import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from flask import Flask, request, make_response
from NoticeCrawler import NoticeCrawler
from CafeteriaCrawler import CafeteriaCrawler
from pypapago import Translator


slack = None
with open('config.json') as json_file:
    token = json.load(json_file)["Bot Token"]
    slack = Slacker(token)

cafeteriaUrl = 'https://coop.koreatech.ac.kr/dining/menu.php'
generalNoticeUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230' # 일반공지
scholarshipNoticeUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231' # 장학공지
bachelorNoticeUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233' # 학사공지

app = Flask(__name__)


# 이벤트 핸들하는 함수

def event_handler(event_type, slack_event):

    if event_type == "app_mention":

        channel = slack_event["event"]["channel"]

        userMessage = slack_event["event"]["blocks"][0]['elements'][0]['elements'][1]['text']

        attachments_dict = dict()

        if '공지' in userMessage :
            if '장학' in userMessage :
                req = requests.get(scholarshipNoticeUrl)
            elif '학사' in userMessage :
                req = requests.get(bachelorNoticeUrl)
            else :
                req = requests.get(generalNoticeUrl)

            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
    
            Notice = NoticeCrawler(soup, slack)
            attachments_dict = Notice.crawling().getAnswer()

        elif '학식' in userMessage :
            req = requests.get(cafeteriaUrl)
            html = req.text
            soup = BeautifulSoup(req.content.decode('euc-kr','replace'),'html.parser')

            Cafeteria = CafeteriaCrawler(soup, slack)
            attachments_dict['text'] = Cafeteria.crawling().formatData().getAnswer()
        
        elif '번역' in userMessage :
            pypapago = Translator()
            attachments_dict['pretext'] = '*[번역] 파파고는 말한다. *:penguin:'
            attachments_dict['text'] = '```'+pypapago.translate(userMessage[3:])+'```'
            attachments_dict['mrkdwn_in'] = ["text", "pretext"]

        elif '안녕' in userMessage :
            attachments_dict['text'] = '나는 *지마블루*:small_blue_diamond: 진리를 쫓아 이곳까지 왔죠. \n시간이 얼마 남지 않았습니다. *이 활동이 저의 마지막이 될 것 입니다.*'
        else :
            attachments_dict['text'] = '무슨 말인지 모르겠네요..'
            attachments_dict['file'] = './reading_room_status.png'

        """ attachments_dict = dict()
        attachments_dict['pretext'] = "attachments 블록 전에 나타나는 text"
        attachments_dict['title'] = "다른 텍스트 보다 크고 볼드되어서 보이는 title"
        attachments_dict['title_link'] = "https://corikachu.github.io"
        attachments_dict['fallback'] = "클라이언트에서 노티피케이션에 보이는 텍스트 입니다. attachment 블록에는 나타나지 않습니다"
        attachments_dict['text'] = "본문 텍스트! 5줄이 넘어가면 *show more*로 보이게 됩니다.\n1\n2\n3\n4\n5\n6\n7\n8\n9\n1\n2\n3\n4\n5\n6\n7\n8\n9"
        attachments_dict['mrkdwn_in'] = ["text", "pretext"]  # 마크다운을 적용시킬 인자들을 선택합니다.
        attachments = [attachments_dict] """
        #slack.chat.post_message(channel="#channel", text=None, attachments=attachments, as_user=True)


        slack.chat.post_message(channel, attachments=[attachments_dict],as_user= True)
       
        # Image attachments
        """ [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "text": "Optional text that appears within the attachment",
                "image_url": "https://mblogthumb-phinf.pstatic.net/MjAxNjEwMjJfNjAg/MDAxNDc3MTM5MDkzMTY5.nTQZS9VKPU3Y1P0J-nOcN4JMz75qU00n09XpQcGJZkAg.3fNACGwA3s_2TSRQxnY6sQDokClABM5fUumyIXAYdQUg.PNG.bugman1303/JW_T-Rex.png?type=w2"
            }
        ] """



        #return make_response("앱 멘션 메시지가 보내졌습니다.", 200, )

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
