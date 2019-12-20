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
