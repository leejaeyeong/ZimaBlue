## parser.py
import json
import requests
from bs4 import BeautifulSoup

""" # 일반, 장학, 학사 공지 
generalNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230'
scholarshipNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231'
bachelorNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'

# 글 번호, 글 제목
noticeNumTag = '#board-wrap > div.board-list-wrap > table > tbody > tr:nth-child(2) > td.num'
noticeTitleTag = '#board-wrap > div.board-list-wrap > table > tbody > tr > td.subject > a > span'

req = requests.get(generalNoticUrl)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

selector = soup.select(noticeTitleTag)
for instance in selector:
    print(instance.text) """
    


req = requests.get('https://coop.koreatech.ac.kr/dining/menu.php')
html = req.text

soup = BeautifulSoup(req.content.decode('euc-kr','replace'),'html.parser')
#print(soup)
#body > div > div:nth-child(2) > table:nth-child(2) > tbody > tr:nth-child(4) > td:nth-child(2)


koreanFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(2)'
specialFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(3)'
onedishFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(4)'
westernFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(5)'
facultyFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(6)'


foodType = [koreanFoodTag,specialFoodTag,onedishFoodTag,westernFoodTag,facultyFoodTag]
kofoodType = {0:'한식', 1:'일품식', 2:'전골/뚝배기', 3:'양식', 4:'능수관'}

for _type in range(len(foodType)) :
    print('========== ' + kofoodType[_type] + ' ==========')
    for time in range(4,6+1) :
        selector = soup.select(foodType[_type].format(time))
    
        for instance in selector:
    
            x  = instance.text
            x = x.replace('\n','\r').replace('\r','\t').split('\t')
            menu = []
            for i in x :
                if i != '' :
                    menu.append(i)

            if time == 4 :
                print('----------- 아침 -----------')
            elif time == 5 :
                print('----------- 점심 -----------')
            else :
                print('----------- 저녁 -----------')

            if menu[0] != '\xa0' :
                for m in menu :
                    if menu[-1] != m :
                        print(m)
                    else :
                        m = m.split('kcal')
                        print(m[0]+'kacl')
                        if len(m) > 1 :
                            print(m[1])
            else :
                print('             -            ')
                
        
        
        