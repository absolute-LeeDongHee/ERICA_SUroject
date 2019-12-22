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
#플레이 시간  크롤링
def Check_Time():
	slt = input("해당 플레이어의 총 플레이 시간을 보시겠습니까?(y/n 대소 구분O)")
	if (slt == 'y'):
		for i in soup.find_all('div', 'time center'):
			print(i.get_text())
	else:
		print("올바르지 않은 입력입니다. 프로그램을 종료합니다.")
#랭킹 크롤링
def ranking():
	slt2 = input("해당 플레이어의 국내 랭킹을 원하시면 국내, 세계 랭킹을 원하시면 세계를 입력해주세요.: ")
	rank = soup.find_all('div', 'rank center')
	if (slt2 == '국내'):
		print('해당 플레이어의 국내 랭킹은', rank[0].get_text())
	elif (slt2 == '세계'):
		print('해당 플레이어의 세계 랭킹은 ' + rank[1])
	else:
		print('올바르지 않은 입력입니다! 실행을 종료합니다.')
ranking()
