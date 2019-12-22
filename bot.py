import asyncio
import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

token = 'NjU4MTY4NDk3MzYwMzM4OTU0.Xf71aw.nALPIfO53FQHPYN5sSj_rYMYn2I'

@client.event
async def on_ready():
	print("봇이 작동합니다!")
	print(client.user.name)
	print(client.user.id)

@client. event
# 봇 무시
async def on_message(message):
	if message.author.bot:
		return None

	if message.content.startswith("!안녕"):
		channel = message.channel
		await channel.send('ㅎㅇㅎㅇ!')
	
	if message.content.startswith("!관전"):
		channel = message.channel
		await channel.send('https://www.op.gg/spectate/pro/')

	if message.content.startswith("!명령어"):
		channel = message.channel
		embed = discord.Embed(title="명령어 모음입니다!", color=0x00ff00)
		embed.add_field(name='!안녕', value = "인사합니다!", inline=False)
		embed.add_field(name='!관전',value = "실시간 프로게이머 관전 사이트를 알려줍니다.", inline=False)
		embed.add_field(name='!전적 닉네임',value = "검색한 닉네임 유저의 전적을 알려줍니다.", inline=False)
		embed.add_field(name='!시간 닉네임',value = "롤 플레이 시간을 알려줍니다.", inline=False)
		embed.add_field(name='!시간낭비 닉네임',value = "롤을 안 했더라면 할 수 있었던 일을 알려줍니다.", inline=False)
		embed.add_field(name='!랭킹 ',value = "롤 플레이 시간 랭킹을 확인할 수 있습니다.", inline=False)
		await channel.send(embed=embed)

	if message.content.startswith("!전적"):
		channel = message.channel
		Name = message.content[4:]
		SummonerName = ""
		TierUnranked = ""
		Tier = []
		LP = []
		Wins = []
		Losses = []
		Ratio = []
		url = 'https://www.op.gg/summoner/userName=' + Name
		hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
			'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
		req = requests.get(url, headers=hdr)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		for i in soup.select('div[class=SummonerName]'):
			SummonerName = i.text
		# 랭킹 크롤링
		for i in soup.select('span[class=ranking]'):
			Ranking = i.text
		# 언랭 판별용 티어 크롤링
		TierUnranked = soup.select('div.Cell')
		# 티어 크롤링
		for i in soup.select('div[class=Tier]'):
			Tier.append(i.text)
		# 리그 포인트 크롤링
		for i in soup.select('div[class=LP]'):
			LP.append(i.text)
		# 승리 패배 판수 크롤링
		for i in soup.select('span[class=Wins]'):
			Wins.append(i.text)
		for i in soup.select('span[class=Losses]'):
			Losses.append(i.text)
		# 승률 크롤링
		for i in soup.select('span[class=Ratio]'):
			Ratio.append(i.text)
		if SummonerName != "":
			if ('Unranked' in str(TierUnranked[0])):
				embed = discord.Embed(title="해당 소환사의 솔로 랭크 전적입니다.", color=0x00ff00)
				embed.add_field(name='솔랭 티어', value="언랭", inline=False)
				await channel.send(embed=embed)
			else:
				embed = discord.Embed(title="해당 소환사의 솔로 랭크 전적입니다.", color=0x00ff00)
				embed.add_field(name='솔랭 티어', value=Tier[0].strip('\n\t'), inline=False)
				embed.add_field(name='솔랭 LP', value=LP[0], inline=False)
				embed.add_field(name='솔랭 승/패', value=Wins[0] + " " + Losses[0], inline=False)
				embed.add_field(name='솔랭 승률', value=Ratio[0], inline=False)
				await channel.send(embed=embed)
			if 'Unranked' in str(TierUnranked[1]):
				embed = discord.Embed(title="해당 소환사의 자유 랭크 전적입니다.", color=0x00ff00)
				embed.add_field(name='자유랭 티어', value="언랭", inline=False)
				await channel.send(embed=embed)
			else:
				embed = discord.Embed(title="해당 소환사의 자유 랭크 전적입니다.", color=0x00ff00)
				embed.add_field(name='자유랭 티어', value=Tier[1].strip('\n\t'), inline=False)
				embed.add_field(name='자유랭 LP', value=LP[1], inline=False)
				embed.add_field(name='자유랭 승/패', value=Wins[1] + " " + Losses[0], inline=False)
				embed.add_field(name='자랭 승률', value=Ratio[1], inline = False)
				await channel.send(embed=embed)

		else:
			await channel.send("소환사 정보가 없습니다.")

	if message.content.startswith("!시간"):
		channel = message.channel
		Name = message.content[4:]
		play_time = []
		url = 'https://kr.wol.gg/stats/kr/' + Name + '/'
		hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
			'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
		req = requests.get(url, headers=hdr)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		# 플레이 타임 크롤링
		for i in soup.find_all('div', 'time center'):
			play_time.append(i)
		# 소환사 이름 크롤링
		summonername2 = soup.find(['h1'])
		if summonername2 != "":
			embed = discord.Embed(title="해당 소환사의 플레이 시간입니다.", color=0x00ff00)
			embed.add_field(name='Minute', value=play_time[0].get_text(), inline=False)
			embed.add_field(name='Hour', value=play_time[1].get_text(), inline=False)
			embed.add_field(name='Day', value=play_time[2].get_text(), inline=False)
			await channel.send(embed=embed)
		else:
			await channel.send("소환사 정보가 없습니다.")

	if message.content.startswith("!랭킹"):
		channel = message.channel
		Name = message.content[4:]
		rank = []
		url = 'https://kr.wol.gg/stats/kr/' + Name + '/'
		hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
			'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
		req = requests.get(url, headers=hdr)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		# 소환사 이름 크롤링
		summonername3 = soup.find(['h1'])
		for i in soup.find_all('div', 'rank center'):
			rank.append(i)
		if summonername3 != "":
			embed = discord.Embed(title="해당 소환사의 플레이 랭킹입니다. (랭킹 뒤의 영어는 해당 지역을 말합니다.)", color=0x00ff00)
			embed.add_field(name='국내 랭킹', value=rank[0].get_text(strip=True), inline=False)
			embed.add_field(name='세계 랭킹', value=rank[1].get_text(strip=True), inline=False)
			await channel.send(embed=embed)
		else:
			await channel.send("소환사 정보가 없습니다.")




client.run(token)
