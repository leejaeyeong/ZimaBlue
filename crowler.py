## parser.py
import json
import requests
from bs4 import BeautifulSoup
from slacker import Slacker

token = 'xoxb-944330254352-947046696531-tCEAJQLRa0PNLW7GyA0DGO2y'
slack = Slacker(token)

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


#foodType = [koreanFoodTag,specialFoodTag,onedishFoodTag,westernFoodTag,facultyFoodTag]
foodType = {0:koreanFoodTag, 1:specialFoodTag, 2:onedishFoodTag, 3:westernFoodTag, 4:facultyFoodTag}
kofoodType = {0:'한식', 1:'일품식', 2:'전골', 3:'양식', 4:'능수관'}

""" 
koreafood = []
specialfood = []
onedishfood = []
westernfood = []
facultyfood = []
arr = []

for _type in range(len(foodType)) :
    arr = [koreafood,specialfood,onedishfood,westernfood,facultyfood]
    for time in range(4,6+1) :
        selector = soup.select(foodType[_type].format(time))
        for instance in selector:
            x  = instance.text
            x = x.replace('\n','\r').replace('\r','\t').split('\t')
            
            for i in x :
                if i != '' :
                    arr[_type].append(i)
            arr[_type].append(i) if arr[_type][0] != '\xa0' else arr[_type].append('-')
            
                
                

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4]) """



width = 40
pprint = ''

for _type in range(len(foodType)) :
    whole = (width - len(kofoodType[_type])) // 2
    print('-'*whole+' ' + kofoodType[_type] +' '+'-'*whole)
    pprint += '\n' + '-'*whole+' ' + kofoodType[_type] +' '+'-'*whole
    for time in range(4,6+1) :
        selector = soup.select(foodType[_type].format(time))
    
        for instance in selector:
    
            x  = instance.text
            x = x.replace('\n','\r').replace('\r','\t').split('\t')
            menu = []
            for i in x :
                if i != '' :
                    menu.append(i)
            blankSize = (width - len('----------- xx -----------')) // 2
            if time == 4 :
                print(' '*(blankSize+1) + '----------- 아침 -----------')
                pprint += '\n' + ' '*(blankSize+1) + '----------- 아침 -----------'
            elif time == 5 :
                print(' '*(blankSize+1) + '----------- 점심 -----------')
                pprint += '\n' + ' '*(blankSize+1) + '----------- 점심 -----------'
            else :
                print(' '*(blankSize+1) + '----------- 저녁 -----------')
                pprint += '\n' + ' '*(blankSize+1) + '----------- 저녁 -----------'

            if menu[0] != '\xa0' :
                for m in menu :
                    if menu[-1] != m :
                        blankSize = (width - len(m)) // 2
                        print(' '*(blankSize) + m)
                        pprint += '\n' + ' '*(blankSize) + m
                    else :
                        m = m.split('kcal')
                        blankSize = (width - len(m[0])) // 2
                        print(' '*(blankSize) + m[0]+'kacl')
                        pprint += '\n' + ' '*(blankSize) + m[0]+'kacl'
                        if len(m) > 1 :
                            blankSize = (width - len(m[1])) // 2
                            print(' '*(blankSize+2) + m[1])
                            pprint += '\n' + ' '*(blankSize+2) + m[1]
            else :
                print('\n                     -\n')
                pprint += '\n' + '\n                     -\n'
print('--------------------------------------------')
pprint += '\n' + '--------------------------------------------'
        
        
slack.chat.post_message('#jbot_test', pprint)