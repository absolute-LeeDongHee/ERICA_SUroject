import requests
from bs4 import BeautifulSoup
Name = input("소환사명을 입력하세요: ")
level = ""
slt = ""
url='https://kr.wol.gg/stats/kr/' + Name + '/'
hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
req = requests.get(url, headers=hdr)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
#플레이 타임 크롤링
play_time = soup.find_all('div', 'time center')
#랭킹 크롤링
rank = soup.find_all('div', 'rank center')
#소환사 이름 크롤링
summonername = soup.find(['h1'])
def Check_Time():
	slt = input("해당 플레이어의 총 플레이 시간을 보시겠습니까?(y/n 대소 구분O)")
	if (slt == 'y'):
		print(summonername + "님의 총 플레이 시간은: ")
		for i in play_time:
			print(i.get_text())
	else:
		print("올바르지 않은 입력입니다. 프로그램을 종료합니다.")
def ranking():
	slt2 = input("해당 플레이어의 국내 랭킹을 원하시면 국내, 세계 랭킹을 원하시면 세계를 입력해주세요. ")
	if (slt2 == '국내'):
		print(str(summonername.get_text()) + '님의 국내 랭킹은', rank[0].get_text(strip=True))
	elif (slt2 == '세계'):
		print(str(summonername.get_text()) + '님의 세계 랭킹은', rank[1].get_text(strip=True))
	else:
		print('올바르지 않은 입력입니다! 실행을 종료합니다.')
