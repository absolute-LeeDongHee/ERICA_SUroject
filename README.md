# 2019055014 소프트웨어학부 김민수

## league of legends에 관한 잡다한 기능이 있는 디스코드 챗봇!


## 1. 현재 프로그램 구현 기능
1. 전적 검색 기능
2. 유저의 게임 총 플레이 시간을 알려줍니다. (분, 시간, 일)
3. 롤 할 시간으로 할 수 있었던 일 출력
4. 실시간 관전 사이트 알려줌

## 2. 빌드 방법
1. sudo apt-get update
2. sudo apt-get install python3를 터미널에 입력하여 파이썬을 깔자!
3. sudo apt-get install python3-pip 파이썬으로 작성된 패키지의 설치와 관리를 위해 설치하자!
4. sudo pip3 install --upgrade pip 업그레이드!
5. pip install requests
6. pip install beautifulsoup4
7. pip install discord 5,6,7번은 봇을 구동하기 위해서 반드시 필요한 모듈이다!
8. https://discordapp.com/developers/applications/ <<<< 들어간다.
9. New Application 선택
10. 좌측 상단 막대기 3개를 누르면 메뉴창이 열리는데 거기서 bot을 선택한다.
11. Add bot 클릭
12. 홈페이지 밑에 보면 Bot Permissons가 있다. 거기서 Send Messages와 Read Message History를 선택한다. 그리고 Token이라고 써있는 부분에서 Token을 복사한다.(나중에 봇을 관리할 키!)
13. 다시 메뉴창에 들어가 OAuth2를 누르고 창을 밑으로 내려 scopes라는 박스 안에 있는 bot을 체크한다.
14. 그러면 더 밑으로 내려 갈 수 있는데 12번과 같은 녀석들을 체크해주자
15. scopes라는 박스 맨 아래에 있는 주소로 들어간다.
16. 추가하고 싶은 디스코드 채널에 넣는다.
17. 이제 에디터로 bot.py를 연다.
18. 'Input your Token'을 '복사한 토큰'으로 바꾸어주자.
19. bot.py를 실행한다.
20. 디스코드 채널을 보면 봇이 온라인 상태가 된다. 이제 명령어를 통해 명령을 내리면 답한다!


+ !명령어를 입력하면 내릴 수 있는 명령어들이 출력된다.

개발일지는 report.txt
커뮤니티 보고서는 https://github.com/absolute-LeeDongHee/ERICA-OSS-report
