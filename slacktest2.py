import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from flask import Flask, request, make_response
from pypapago import Translator

# 일반, 장학, 학사 공지 
generalNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230'
scholarshipNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231'
bachelorNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'

# 글 번호, 글 제목
test = '#form1 > div:nth-child(3) > table > tr:nth-child(2) > td:nth-child(2) > table > tr'

class NoticeCrawler :
    def __init__(self, soup, slack):
        self.soup = soup 
        self.slack = slack
        self.Message = ''
        self.selector = None
    
    def crawling(self) :
        self.selector = self.soup.select(test)
        for i in self.selector :
            break
        
            
    def getAnswer(self) :
        if self.selector == None :
            self.crawling()

        notice = ''
        for instance in self.selector:
            notice += instance.text

        return notice

slack = None
with open('config.json') as json_file:
    token = json.load(json_file)["Bot Token"]
    slack = Slacker(token)

req = requests.get('http://220.68.79.34/EZ5500/SEAT/ROOMSTATUS.ASPX')

html = req.text

soup = BeautifulSoup(html, 'html.parser')
Notice = NoticeCrawler(soup, slack)
xx = Notice.getAnswer().replace('\n','').replace('1층','').replace('2층','').split(' ')

matrix = [[None for col in range(5)] for row in range(6)]
print(len(matrix[0]))

print(xx)

row, col = 0,0
for i in xx :
    if row == len(matrix) :
        break
    if '' == i or '%\r' == i :
        continue
    
    print(i)
    print(row,col)

    if matrix[row][col] == None :
        matrix[row][col] = i
        if col + 1 == len(matrix[0]) : 
            row += 1
            col = 0
        else :
            col += 1

    

print(matrix)

    