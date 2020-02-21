import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from NoticeCrowler import NoticeCrowler
from CafeteriaCrowler import CafeteriaCrowler


token = 'xoxb-944330254352-947046696531-jZ9DI3wdBReU2sMNk3SdsTtC'
slack = Slacker(token)

cafeteriaUrl = 'https://coop.koreatech.ac.kr/dining/menu.php'
generalNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230'
scholarshipNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231'
bachelorNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'



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

