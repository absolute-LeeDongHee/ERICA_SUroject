import requests
from bs4 import BeautifulSoup

Name = input("검색하실 닉네임을 입력하세요!")
SummonerName = ""
Ranking = ""
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

#닉네임 크롤링======================================================
for i in soup.select('div[class=SummonerName]'):
	SummonerName = i.text
#랭킹 크롤링========================================================
for i in soup.select('span[class=ranking]'):
	Ranking = i.text
#당신은 언랭?=======================================================
Tier_Unranked = soup.select('div.cell')
#속한 리그 크롤링===================================================
for i in soup.select('div[class=LeagueType]'):
	LeagueType.append(i.text)
# 티어 크롤링=======================================================
for i in soup.select('div[class=Tier]'):
	Tier.append(i.text)
