import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys
import json
import random

with open('jokes.json') as file:
	Jokes = json.load(file)
nrj = len(Jokes)


# setup Bot
client = Bot(description="Jokes by Guava", command_prefix=">", pm_help = False)

# open private key file
with open('./discord_key.txt', 'r') as key_file:
	if not key_file:
		print('File discord_key.txt can\'t be found')
		sys.exit(0)

	# read private key from file
	api_key = key_file.read().splitlines()[0]
if not api_key:
	print('No API key in discord_key.txt')
	sys.exit(0)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name)
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client.user.id))

@client.event
async def on_message(message):
	print(message.content)
	if message.content.lower().__contains__('these'):
		channel = message.channel
		await channel.send('Dees NUTS\n https://media.giphy.com/media/CYU3D3bQnlLIk/giphy.gif')
	if message.content.lower().startswith("<@&777086562936684545>"):
		channel = message.channel
		aut = message.author
		j = pickjoke(random.randint(0,nrj-1))

		await channel.send('{} Knock knock'.format(aut.mention))
		msg = await getM(aut, channel)
		if msg.content.lower().endswith('?'):
			await channel.send('{} {}'.format(aut.mention,j['re1']))

		msg = await getM(aut, channel)
		if msg.content.lower().endswith('?'):
			await channel.send('{} {}'.format(aut.mention,j['re2']))
	
	# daniel----------------------------------------------------------------------
	if message.content.lower().startswith("i'm "):
		channel = message.channel
		await channel.send(content='Hi {}, i\'m Dad'.format(message.content[4:]))

	if message.content.lower().startswith("where's "):
		channel = message.channel
		await channel.send(content='Buying cigarettes')
	#-----------------------------------------------------------------------------

async def getM(aut, channel):
	msg = await  channel.fetch_message(channel.last_message_id)
	while(msg.author != aut):
		msg = await channel.fetch_message(channel.last_message_id)
	return msg

def getjoke(joke):
	j = Jokes[joke]
	return j

def pickjoke(a):
	return getjoke('Joke{}'.format(a))

client.run(str(api_key)) # Send API key from opened file