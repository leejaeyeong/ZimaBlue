koreanFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(2)'
specialFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(3)'
onedishFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(4)'
westernFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(5)'
facultyFoodTag = 'body > div > div > table > tr:nth-child({}) > td:nth-child(6)'
foodType = {0:koreanFoodTag, 1:specialFoodTag, 2:onedishFoodTag, 3:westernFoodTag, 4:facultyFoodTag}
foodTitle = {0:':rice: *한식* :rice:', 1:':curry: *일품식* :curry:', 2:':shallow_pan_of_food: *전골* :shallow_pan_of_food:', 3:':hamburger: *양식* :hamburger:', 4:':bento: *능수관* :bento:'}

class CafeteriaCrowler :
    
    def __init__(self,url, soup, slack):
        self.url = url 
        self.soup = soup 
        self.slack = slack
        self.todayDiet = []
        self.Message = ''

    def bringData(self) :
        koreafood = []
        specialfood = []
        onedishfood = []
        westernfood = []
        facultyfood = []
        for kind in range(len(foodType)) :
            self.todayDiet = [koreafood,specialfood,onedishfood,westernfood,facultyfood]
            for time in range(4,6+1) :
                selector = self.soup.select(foodType[kind].format(time))
                for instance in selector:
                    diet  = instance.text
                    diet = diet.replace('\n','\r').replace('\r','\t').split('\t')
            
                    for i in diet :
                        if i != '' :
                            self.todayDiet[kind].append(i)
                    if self.todayDiet[kind][0] != '\xa0':
                        self.todayDiet[kind].append(i)
        return self

    def formatData(self) :
        time = ['   ==== 아침 메뉴 ====','   ==== 점심 메뉴 ====','   ==== 저녁 메뉴 ====']

        for i in range(len(self.todayDiet)) :
            self.Message += foodTitle[i]
            self.Message += '\n' + '￣'*16

            if self.todayDiet[i][0] != '\xa0' : 
                self.Message += '\n' + time[0]

            nCnt, lunch, dinner = 0, False, False

            for j in self.todayDiet[i] :
                if j == '\xa0' :
                    nCnt += 1
                else :
                    if nCnt == 1 and j != '' and lunch == False :
                        self.Message += '\n' + time[1]
                        lunch = True
                    elif nCnt == 2 and j != '' and dinner == False:
                        self.Message += '\n' + time[2]
                        dinner = True
                if len(j) > 2:
                    self.Message += '\n'+' '*5 + j
            self.Message += '\n' + '￣'*16 + '\n\n'
        return self

        
    def sendData(self) :
        return self.slack.chat.post_message('#jbot_test', self.Message)




                


