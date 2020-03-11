import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from flask import Flask, request, make_response
from collections import OrderedDict

# 일반, 장학, 학사 공지 
generalNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230'
scholarshipNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231'
bachelorNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'

# 글 번호, 글 제목
noticeTitleTag = '#board-wrap > div.board-list-wrap > table > tbody > tr'

baseUrl = 'https://www.koreatech.ac.kr/'

class NoticeCrawler :
    def __init__(self, soup, slack):
        self.soup = soup 
        self.slack = slack
        self.Message = ''
        self.postList = []
        self.selector = None
    
    def crawling(self) :
        self.selector = self.soup.select(noticeTitleTag)
        for i in self.selector :
            #print(i)
            post_num = i.find('td').text
            post_title = i.find('span')['title']
            post_link = baseUrl + str(i.find('a')['href'])
            self.postList.append([post_link, post_num, post_title])
        return self

    def getAnswer(self) :
        jsonData = OrderedDict()
        jsonData['blocks'] = []
        post = ''
        for i in range(len(self.postList)) :
            post += '<{}|{}>\n'.format(self.postList[i][0],self.postList[i][2])
        jsonData['blocks'].append({'type' :'section','text' : {'type' :'mrkdwn','text' : post }})
        return jsonData


