# ZimaBlue  
![zima](https://img.shields.io/github/languages/top/leejaeyeong/ZimaBlue)

<!-- ![zimablue](https://66.media.tumblr.com/131505d5d4a45b16a82d904fceee23ca/748595656bbdae16-3e/s500x750/54a81d90c45f4a390a2c0c627c9c88a89fb4af00.jpg) -->

![zimablud_gif](https://raw.githubusercontent.com/leejaeyeong/ZimaBlue/master/img/zimablue.gif)

### 기능  
 - [x] 최근 공지사항 불러오기
   - [x] 일반 공지  
   - [x] 학사 공지  
   - [x] 장학 공지  
 - [x] 오늘의 학식 메뉴  
 - [x] 번역  
 - [x] 대성고속 배차 시간  
 - [ ] 열람실 현황 조회

### Library install
```
pip install -r requirements.txt
```

### config.json  
최상위 경로에 config.json 파일을 생성한 후 token을 입력해주세요.  
> 비밀 값들은 반드시 남이 알 수 없어야 한다. 이를 버전 컨트롤 시스템에 추가하면 코드 저장소에 접근할 수 있는 누구에게나 공개된다
```  
{
    "Bot Token" : "your token"
}  
```  

### 사용법

#### @ZimaBlue
slack 봇 이름을 언급하고 ```학사공지```, ```장학공지```, ```일반공지```, ```학식```, ```번역```, ```버스``` 키워드를 입력하면 해당 정보를 보여줍니다.  
번역 사용의 예)  
```@ZimaBlue 번역 hello world!```
