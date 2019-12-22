import asyncio
import discord

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
		embed.add_field(name='!전적',value = "검색한 닉네임 유저의 전적을 알려줍니다.", inline=False)
		embed.add_field(name='!플레이 시간',value = "롤 플레이 시간을 알려줍니다.", inline=False)
		embed.add_field(name='!시간낭비',value = "롤을 안 했더라면 할 수 있었던 일을 알려줍니다.", inline=False)
		embed.add_field(name='!플레이 시간 랭킹',value = "롤 플레이 시간 랭킹을 확인할 수 있습니다.", inline=False)
		await channel.send(embed=embed)


client.run(token)
