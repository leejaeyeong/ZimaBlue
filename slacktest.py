import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from flask import Flask, request, make_response
from NoticeCrawler import NoticeCrawler
from CafeteriaCrawler import CafeteriaCrawler
from pypapago import Translator
import datetime, time

req = requests.get('https://hantalk.io/bus')

tag = '#intercity-timetable > div > table:nth-child(1) > tbody > tr:nth-child({}) > td:nth-child(1)'

#intercity-timetable > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(1)
html = req.text
soup = BeautifulSoup(html, 'html.parser')



s = datetime.datetime.now()
x = '{}:{}'.format(s.hour,s.minute)
print(x)
time = []

for i in range(16) :
    selector = soup.select(tag.format(i+1))
    time.append(selector[0].text)
idx = 0
for i in range(len(time)) :
    if (int(time[i].split(':')[0]) - s.hour)*60 + (int(time[i].split(':')[1]) - s.minute) > 0 :   
        idx = i
        break
    if i == len(time) - 

Message = ''
for i in range(len(time)) :
    if idx != i :
        Message += '\n'+str(time[i])
    else : 
        Message += '\n*' + str(time[i])

print(Message)
#print(time)