import requests
from bs4 import BeautifulSoup

Name = input("검색하실 닉네임을 입력하세요!")
Nickname = ""
Unranked = ""
LeagueType = [] #속한 리그 이름
Tier = [] #티어
LP = [] #리그 포인트
Wins = [] #승리 횟수
Losses = [] #패배 횟수
Ratio = [] #승률

url = 'https://www.op.gg/summoner/userName=' + Name
hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')} 
req = request.get(url, headers=hdr)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
