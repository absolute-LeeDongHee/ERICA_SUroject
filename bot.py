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

client.run(token)
