# 일반, 장학, 학사 공지 
generalNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230'
scholarshipNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231'
bachelorNoticUrl = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'

# 글 번호, 글 제목
noticeNumTag = '#board-wrap > div.board-list-wrap > table > tbody > tr:nth-child(2) > td.num'
noticeTitleTag = '#board-wrap > div.board-list-wrap > table > tbody > tr > td.subject > a > span'

class NoticeCrawler :
    def __init__(self, soup, slack):
        self.soup = soup 
        self.slack = slack
        self.Message = ''
        self.selector = None
    
    def crawling(self) :
        self.selector = self.soup.select(noticeTitleTag)

    def getAnswer(self) :
        if self.selector == None :
            self.crawling()

        notice = ''
        for instance in self.selector:
            notice += instance.text + '\n'

        return notice




