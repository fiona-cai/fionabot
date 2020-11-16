import discord
import requests
import asyncio
import json
from discord.ext.commands import Bot
from discord import Spotify
from discord.utils import get
from random import randint
import random
from discord.ext import commands
from platform import python_version
import configparser
import os
import platform
import html
import youtube_dl
import ffmpeg
from threading import Thread
import time
from colour import Color
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import enchant
from wiktionaryparser import WiktionaryParser

bprefix = ('fi ', 'fiona ', 'FI', 'Fiona', 'Fi')
token = 'NzM2MzcyMzMwNjQ0ODk3ODkz.Xxt2LA.Xy8A6gtOFulUKR3nZbdkRwAvAR4'
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
me = [511025033976741889]
blacklist = []
client = Bot(command_prefix=bprefix)
d = enchant.Dict("en_US")
config = configparser.RawConfigParser()
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f56564e80dd64d07b226e974db555581", client_secret="19334db40c9d4c1b99d804959712749a"))

pink = 0xFF8CC4
pinkstr = "FF8CC4"
red = 0xF43D38
redstr = "F43D38"



cola = red

async def status_task():
	while True:
		await client.change_presence(activity=discord.Game("fi help"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you guys"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you guys"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Game("with my status!"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{} servers".format(str(len(client.guilds)))))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Game("something"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="you"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Game("fi help"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Game("with my friends!"))
		await asyncio.sleep(30)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my parents"))
		await asyncio.sleep(30)

@client.event
async def on_ready():
	if not hasattr(client, 'appinfo'):
		client.appinfo = await client.application_info()
	client.loop.create_task(status_task())
	print('Logged in as ' + client.user.name)
	print("Discord.py API version:", discord.__version__)
	print("Python version:", platform.python_version())
	print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
	print('-------------------')

@client.command(name='info', pass_context=True)
async def info(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		e = discord.Embed(description="Here you go! Free information about me!", color=cola,title='**__Bot Information__**')
		e.set_thumbnail(url=client.appinfo.icon_url)
		e.add_field(name="Owner", value=client.appinfo.owner, inline=True)
		e.add_field(name="Prefix", value="fi ", inline=True)
		e.add_field(name="Python Version", value="{0}".format(python_version()), inline=True)
		e.add_field(name="Name", value=client.appinfo.name, inline=True)
		e.add_field(name="ID", value=client.appinfo.id, inline=True)
		e.add_field(name="Servers", value=str(len(client.guilds)), inline=True)
		e.add_field(name="Users", value=str(len(client.users)), inline=True)
		e.add_field(name="Public", value=client.appinfo.bot_public, inline=True)
		e.add_field(name="Require Code Grant", value=client.appinfo.bot_require_code_grant, inline=True)

		e.set_footer(text="Requested by {0}".format(context.message.author))
		await context.message.channel.send(embed=e)

@client.command(name='detailedinfo', pass_context=True)
async def detailedinfo(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('I sent you a private message! Go check your DMs')
		await context.message.author.send("Hello Hello! I'm Fiona, nice to meet you! I'm assuming you want to know how I came to life right? well... Get ready to hear my story.")
		await context.message.author.send("My creator, occona#9933 was inspired by a bot named President Pizza. She didn't really know coding all that well but, eh she decided to give it a try. Within 48 hours, her bot, (me!) came to life. It was truly a moment for her. Thanks to all her friends, this bot quickly grew and got more and more commands! How great that made her feel! But her main concern now is that no one wants to use her bot :( hopefully this won't last for long. I really want to be in more servers and help more people... :pleading_face:")
		await context.message.author.send("Oh! haha she just texted me and wanted me to remind you that you can always give suggestions to her by DMing her. Sigh, How could I almost forget to tell you that..")

@client.command(name='serverinfo', pass_context=True)
async def serverinfo(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		server = context.message.guild
		roles = [x.name for x in server.roles]
		role_length = len(roles)
		roles = ', '.join(roles)
		channels = len(server.channels)
		categories = len(server.categories)
		time = str(server.created_at)
		time = time.split(' ')
		time = time[0]
		em = discord.Embed(description='%s ' % (str(server)), title='**__Server Name:__**', color=cola)
		em.set_thumbnail(url=server.icon_url)
		em.add_field(name='Owner', value=str(server.owner), inline=True)
		em.add_field(name='Server ID', value=str(server.id), inline=True)
		em.add_field(name='Member Count', value='{} members'.format (server.member_count), inline=True)
		em.add_field(name='Categories', value='{} categories'.format (categories), inline=True)		
		em.add_field(name='Text/Voice Channels', value='{} channels'.format (channels), inline=True)
		em.add_field(name='Default Role', value=str(server.default_role), inline=True)
		em.add_field(name='Roles (%s)' % str(role_length), value=roles, inline=False)
		em.add_field(name='Verification Level', value=str(server.verification_level), inline=True)
		em.add_field(name='Explicit Content Filter', value=str(server.explicit_content_filter), inline=True)
		em.add_field(name='Date Created', value=(time), inline=True)
		await context.message.channel.send(embed=em)

@client.command(name='servers', pass_context=True)
async def servers(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send(client.guilds)

@client.command()
async def userinfo(ctx, *, member: discord.Member=None):
	if not member:
		member = ctx.message.author 
	avatar = member.avatar_url
	role = member.top_role
	nname = member.display_name
	joined = member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
	eb = discord.Embed(description=str(member), color=cola, title='**__User Information__**')
	eb.add_field(name="Displayed Name", value=str(nname), inline=True)
	eb.add_field(name="Date Joined Discord", value=str(joined), inline=False)
	eb.add_field(name="Top Role", value=str(role), inline=False)
	eb.set_thumbnail(url=avatar)
	eb.set_footer(text="Requested by {0}".format(ctx.message.author))
	await ctx.send(embed=eb)

@client.command(name='spotify', pass_context=True)
async def spotify(context, user: discord.Member=None):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		user = user or context.message.author
		for activity in user.activities:
			if isinstance(activity, Spotify):
					elb = discord.Embed(description=str(user), color=cola, title='**__Spotify__**')
					elb.add_field(name="Song Name", value=str(activity.title), inline=True)
					elb.add_field(name="Song Artist", value=str(activity.artist), inline=True)
					elb.add_field(name="Album", value=str(activity.album), inline=True)					
					elb.add_field(name="Duration", value=str(activity.duration), inline=True)
					elb.add_field(name="Start", value=str(activity.start(minute=1)), inline=True)
					elb.add_field(name="End", value=str(activity.end), inline=True)
					elb.set_thumbnail(url=activity.album_cover_url)
					elb.set_footer(text="Requested by {0}".format(context.message.author))
					await context.message.channel.send(embed=elb)
			else:
				await context.message.channel.send("Ahaha! Trying to trick me eh? Bruhh I'm not *that* stupid! Use spotify first or mention a person who is!! For example, fi spotify @myfriend")

@client.command(name='ping', pass_context=True)
async def ping(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(color=cola)
		embed.set_footer(text='Requested by {0}'.format(context.message.author))
		embed.add_field(name='Pong!', value="I'm ready :wink: {0}ms".format(round(client.latency*1000)), inline=True)
		await context.message.channel.send(embed=embed)

@client.command(pass_context=True)
async def plonk(ctx):
	await ctx.message.delete()
	before = time.monotonic()
	message = await ctx.send("Pong!")
	ping = (time.monotonic() - before) * 1000
	before = time.monotonic()
	await message.edit(content=f"Send:  `{int(ping)}ms`")
	edit = (time.monotonic() - before) * 1000
	await ctx.send(content=f"Edit:  `{int(edit)}ms`")
	print(f'Ping {int(ping)}ms')

@client.command(name='invite', pass_context=True)
async def invite(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('I sent you a private message! Go check your DMs')
		await context.message.author.send('Invite me by clicking here: https://discord.com/api/oauth2/authorize?client_id=736372330644897893&permissions=8&scope=bot')

@client.command(name='server', pass_context=True)
async def server(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('I sent you a private message! Go check your DMs')
		await context.message.author.send('Join my discord server by clicking here: https://discord.gg/x9h2MZq')

@client.command(name='poll', pass_context=True)
async def poll(context, *args, aliases=['poll1']):
	mesg = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		embed = discord.Embed(title='{0}'.format(mesg), description=' -- ', color=cola)
		embed.set_footer(text='Poll created by: {0} • React to vote!'.format(context.message.author))
		embed_message = await context.message.channel.send(embed=embed)
		await embed_message.add_reaction('👍')
		await embed_message.add_reaction('👎')

@client.command(name='poll2', pass_context=True)
async def poll2(context, *args):
	mesg = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		embed = discord.Embed(title='{0}'.format(mesg), description=' -- ', color=cola)
		embed.set_footer(text='Poll created by: {0} • React to vote!'.format(context.message.author))
		embed_message = await context.message.channel.send(embed=embed)
		await embed_message.add_reaction('👍')
		await embed_message.add_reaction('👎')
		await embed_message.add_reaction('🤷')

@client.command(name='8ball', pass_context=True, aliases=['8b', '8', '8bal'])
async def eight_ball(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.', 'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
		embed = discord.Embed(title='**My Answer:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=cola)
		embed.set_footer(text='Question asked by: {0} • Ask your own now!'.format(context.message.author))
		await context.message.channel.send(embed=embed)

@client.command(name='coin', pass_context=True, aliases=['flip'])
async def coin(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		answers = ['Heads', 'Tails']
		emed = discord.Embed(title='**My Answer:** ', description='wait for it...', color=cola)
		emed.set_image(url='https://s3-eu-west-1.amazonaws.com/onlinebingo/upload/coin-toss-YkQK9LE/coin-toss')
		emed.set_footer(text='Question asked by: {0} • Ask your own now!'.format(context.message.author))
		msg = await context.message.channel.send(embed=emed)
		await asyncio.sleep(2)
		embe = discord.Embed(title='**My Answer:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=cola)
		embe.set_footer(text='Question asked by: {0} • Ask your own now!'.format(context.message.author))
		await msg.edit(embed=embe)

@client.command(name='say', pass_context=True, aliases=['echo'])
async def say(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		mesag = ' '.join(args)
		await context.message.channel.send('{0} \n||{1}||'.format(mesag, context.message.author))
		await context.message.delete()
           
@client.command(name='embed', pass_context=True)
async def embed(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		mesg = ' '.join(args)
		edm = discord.Embed(title=mesg, color=cola)
		edm.set_footer(text='Originally said by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=edm)
		await context.message.delete()

@client.command(name='colour', pass_context=True, aliases=['color'])
async def color(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		mesg = ' '.join(args)
		uppercase = mesg.upper()
		c = Color(mesg)
		print (uppercase)
		hexnumb = c.hex
		hexno = hexnumb[1:]
		hslnumb = c.hsl
		(h, s, l) = hslnumb
		hhsl = round(h, 2)
		hssl = round(s, 2)
		hsll = round(l, 2)
		rgbnumb = c.rgb
		(r, g, b) = rgbnumb
		rrgb = round(r, 2)
		rggb = round(g, 2)
		rgbb = round(b, 2)
		funnytext = ['Color+Me+Happy', 'Crack+a+Smile', 'Dream+Come+True', 'Grinning+From+Ear+to+Ear', 'Happy+As+a+Clam', 'Happy+As+a+Pig+In+Mud', 'Happy+Camper', 'Jump+For+Joy', 'Made+My+Day', 'On+Cloud+Nine', 'On+Top+of+The+World', 'Over+The+Moon', 'Walking+On+Air', 'Walking+On+Sunshine']
		latext = random.choice(funnytext)
		preview = 'https://dummyimage.com/600x600/{}/ffffff.png&text={}'.format(hexno, latext)
		print(preview)
		ebed = discord.Embed(title='**__{}__** '.format(uppercase), description='some info about {}...'.format(c), color=cola)
		ebed.add_field(name='HEX', value=hexnumb, inline=False)
		ebed.add_field(name='HSL', value='{0}, {1}, {2}'.format(hhsl, hssl, hsll), inline=False)
		ebed.add_field(name='RGB', value='{0}, {1}, {2}'.format(rrgb, rggb, rgbb), inline=False)
		ebed.set_thumbnail(url=preview)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebed)

@client.command(name='connect4', pass_context=True, aliases=['c4','connect','cf'])
async def connect4(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		ebed = discord.Embed(title='**__Connect 4__** ', description="Let's start!", color=cola)
		ebed.add_field(name=':one: :two: :three: :four: :five: :six: :seven:', value=':white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:\n:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:\n:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:\n:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:\n:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:\n:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:\n:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:', inline=False)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebed)

@client.command(name='random', pass_context=True, aliases=['randomimage', 'rand'])
async def realorcake(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		it = ['https://picsum.photos/400','https://picsum.photos/600/400/','https://picsum.photos/600/800/','https://picsum.photos/600','https://picsum.photos/800/400/','https://picsum.photos/400/800/','https://picsum.photos/800','https://picsum.photos/1000','https://picsum.photos/200/300','https://picsum.photos/200/300?grayscale','https://picsum.photos/400?grayscale','https://picsum.photos/800?grayscale','https://picsum.photos/200/300/?blur=2','https://picsum.photos/200/300/?blur=3','https://picsum.photos/200/300/?blur=1','https://picsum.photos/200/300?random=2','https://picsum.photos/200/300?random=1']
		ebed = discord.Embed(title='**__Random Pic!...__** ', description="Hope you like it!", color=cola)
		ebed.set_image(url=it[randint(0, len(it))])
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebed)

@client.command(name='bmi', pass_context=True)
async def bmi(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		ebed = discord.Embed(title='**Weight** ', description='What is your weight in kg?', color=cola)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebed)
		def is_correct(m):
			return m.author == context.message.author
		try:
			msg = await client.wait_for("message", check=is_correct, timeout=30)
		except asyncio.TimeoutError:
			await context.message.channel.send("Timed out, try again.")
		await context.message.channel.purge(limit=2)
		w = int(msg.content)
		eed = discord.Embed(title='**Height** ', description='What is your height in cm?', color=cola)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=eed)
		try:
			mg = await client.wait_for("message", check=is_correct, timeout=30)
		except TimeoutError:
			await context.message.channel.send("Timed out, try again.")
		await context.message.channel.purge(limit=2)
		h = int(mg.content)
		await context.message.delete()
		bmi = w / (h ** 2) * 10000
		BMI = (round(bmi,2))
		if(bmi <= 18.5):
			fat = "underweight"
		elif(bmi > 18.5 and bmi <= 24.9):
			fat = ("normal weight")
		elif(bmi > 24.9 and bmi <= 29.9):
			fat = ("overweight")
		else:
			fat = ("obesity")
		ebd = discord.Embed(title='**__BMI__** ', description='||Your BMI is {}. The classification of your BMI is {}||'.format (BMI, fat), color=cola)
		ebd.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebd)

triviatimes = 0
@client.command(name='trivia', pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def trivia(context, *args):
	global triviatimes
	count = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	elif count == 'count':
		await context.message.channel.send(triviatimes)
	else:
		triviatimes += 1
		r = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
		data = json.loads(r.text)
		question = data['results'][0]['question']
		answers = data['results'][0]['incorrect_answers']
		correct_answer = data['results'][0]['correct_answer']
		answers.append(correct_answer)
		random.shuffle(answers)
		print (correct_answer)
		a = answers[0]
		b = answers[1]
		c = answers[2]
		d = answers[3]
		emed = discord.Embed(title='**Trivia Time!** ', description = (html.unescape(question)), color=cola)
		emed.add_field(name='a) {}'.format(a.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü').replace('&auml;', 'ä').replace('&ouml;', 'ö')), value = "type a", inline = False)
		emed.add_field(name='b) {}'.format(b.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü').replace('&auml;', 'ä').replace('&ouml;', 'ö')), value = "type b", inline = False)
		emed.add_field(name='c) {}'.format(c.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü').replace('&auml;', 'ä').replace('&ouml;', 'ö')), value = "type c", inline = False)
		emed.add_field(name='d) {}'.format(d.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü').replace('&auml;', 'ä').replace('&ouml;', 'ö')), value = "type d", inline = False)
		emed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=emed)
		def check(m):
			return m.author == context.message.author and m.channel == context.message.channel
		try:
			mssag = await client.wait_for("message", check=check, timeout=30)
		except asyncio.TimeoutError:
			await context.message.channel.send("Timed out, try again.")
		useranswer = mssag.content.lower()
		if useranswer == 'a':
			user_answer = answers[0]
		if useranswer == 'b':
			user_answer = answers[1]
		if useranswer == 'c':
			user_answer = answers[2]
		if useranswer == 'd':
			user_answer = answers[3]
		
		if user_answer == correct_answer:
			await context.message.channel.send("YAY! you got it right! Thanks for playing!")
		if user_answer != correct_answer:
			print (user_answer)
			await context.message.channel.send("Sorry, that is incorrect. Correct answer is {}. Thanks for playing tho :)".format(correct_answer))


dong = {}
queuenumb = 0


@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()

	await voice.disconnect()

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		print(f"The bot has connected to {channel}\n")

	await ctx.send(f"Joined {channel}")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		print(f"The bot has left {channel}")
		await ctx.send(f"Left {channel}")
	else:
		print("Bot was told to leave voice channel, but was not in one")
		await ctx.send("Don't think I am in a voice channel")

@client.command(pass_context=True, aliases=['qeueua'])
async def queuea(ctx, *args):
	with open('mydata.json', 'a') as f:
		lasong = ' '.join(args)
		dong = {ctx.guild.id: lasong}
		print(dong)
		json.dump(dong, f)
		await ctx.send('k queued')
		

@client.command(pass_context=True, aliases=['qued'])
async def queueda(ctx, *args):
	with open('mydata.json', 'r') as f:
		server = json.load(f)
		for s_id, s_info in server.items():
			print("\nServer ID:", s_id)
			for key in s_info:
				it = s_info[key]
				if s_id == ctx.guild.id:
					await ctx.send(it)

global voice
global queue_list

@client.command(name='queue', pass_context=True, aliases=['qeueu'])
async def queue(ctx, *args):
	queue_list = {}
	lasong = ' '.join(args)
	try:
		with open('mydata.json', 'r') as f:
			queue_list = json.load(f)
			queue_list["{}".format(ctx.guild.id)].append(lasong)
			with open('mydata.json', 'w') as f:
				json.dump(queue_list, f)
	except Exception:
		with open('mydata.json', 'a') as f:
			queue_list = {ctx.guild.id: [lasong]}
			json.dump(queue_list, f)
	await ctx.send("k queued")

@client.command(pass_context=True, aliases=['aartist'])
async def artist(ctx, *args):
	laartist = ' '.join(args)
	results = sp.search(q=laartist, limit=1, type='artist') 
	print (results)
	url = 'https://open.spotify.com/artist/{}'.format(results['artists']['items'][0]['id'])
	await ctx.send(content=url)

@client.command(pass_context=True, aliases=['aalbmn'])
async def album(ctx, *args):
	laalbum = ' '.join(args)
	results = sp.search(q=laalbum, limit=1, type='album') 
	print (results)
	url = 'https://open.spotify.com/album/{}'.format(results['albums']['items'][0]['id'])
	await ctx.send(content=url)	

@client.command(pass_context=True, aliases=['ssong'])
async def song(ctx, *args):
	lasong = ' '.join(args)
	results = sp.search(q=lasong, limit=1, type='track')  
	print (results)
	url = 'https://open.spotify.com/track/{}'.format(results['tracks']['items'][0]['id'])
	print(url)
	await ctx.send(content=url)

@client.command(pass_context=True, aliases=['go'])
async def gota(ctx, *args):
	asyncio.set_event_loop
	voice = get(client.voice_clients, guild=ctx.guild)
	f = open('mydata.json')
	queue_list = json.load(f)
	song_there = os.path.isfile("{}.mp3".format(ctx.guild.id))
	song = [] 
	songiee = queue_list["{}".format(ctx.guild.id)][0]
	print (songiee)
	song.insert(0, songiee)
	print(song)
	if song_there:
		os.remove("{}.mp3".format(ctx.guild.id))
	await ctx.send("Getting everything ready, playing audio soon")
	print("Someone wants to play music let me get that ready for them...")
	serverr=ctx.guild.id
	try:
		if voice.is_playing():
			await ctx.send("ayy there we go!")
			await ctx.send("NOW PLAYING: {}".format(song))
			song.clear()
			print ("{}".format(songiee))
		with open('mydata.json', 'w') as f:
			print (queue_list)
			songa = queue_list["{}".format(serverr)]
			print (songa)
			sonly = songa[0]
			print (sonly)
			songa.pop(0)
			queue_list.pop("{}".format(serverr))
			queue_list = {ctx.guild.id: songa}
			json.dump(queue_list,f)

	except PermissionError:
		await ctx.send("im not in a voice channel dummy")

@client.command(pass_context=True, aliases=['pau'])
async def pause(ctx, *args):
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.pause()

@client.command(pass_context=True, aliases=['ski'])
async def skip(ctx, *args):
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.pause()

@client.command(pass_context=True, aliases=['res'])
async def resume(ctx, *args):
	voice = get(client.voice_clients, guild=ctx.guild)
	voice.resume()

@client.command(pass_context=True, aliases=['p', 'pla'])
async def playa(ctx, *args):
	f = open('mydata.json')
	dong = json.load(f)
	voice = get(client.voice_clients, guild=ctx.guild)
	while voice.is_playing() == False:
		song_there = os.path.isfile("{}.mp3".format(ctx.guild.id))
		song = dong["{}".format(ctx.guild.id)]
		print(song)
		try:
			if song_there:
				os.remove("{}.mp3".format(ctx.guild.id))
		except PermissionError:
			await ctx.send("Wait for the current playing music end or use the 'queue' command")
			return
		await ctx.send("Getting everything ready, playing audio soon")
		print("Someone wants to play music let me get that ready for them...")
		ydl_opts = {
			'format': 'bestaudio/best',
			'noplaylist': True,
			'default_search': 'auto',
		}
		serverr=ctx.guild.id
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			extract=ydl.extract_info(song)
			print(extract)
			for file in os.listdir("./"):
				if file.endswith(".mp3"):
					os.rename(file, '{}.mp3'.format(serverr))




@client.command(name='quote', pass_context=True, aliases=['qu'])
async def quote(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		req = requests.get("https://type.fit/api/quotes")
		da = json.loads(req.text)
		numb = random.randint(0,1500)
		quote = da[numb]['text']
		author = da[numb]['author']
		print (quote)
		edebm = discord.Embed(title=" ", color=cola)
		edebm.add_field(name='*"{}"*'.format(quote), value="- {}".format(author), inline=False)
		edebm.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=edebm)

@client.command(name='image', pass_context=True, aliases=['img'])
async def image(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		topic = ' '.join(args)
		print (topic)
		if topic == ('.'):
			await context.message.add_reaction('👍')
		elif topic == ('cupcake'):
			cupcakeimgs = ["https://cdn.sallysbakingaddiction.com/wp-content/uploads/2018/09/chai-latte-cupcakes.jpg", 
				"https://cdn.sallysbakingaddiction.com/wp-content/uploads/2019/05/yellow-cupcakes-with-chocolate-frosting-sprinkles.jpg", 
				"https://truffle-assets.imgix.net/pxqrocxwsjcc_4mlylloieeiqmyecgk0qq8_rose%CC%81-champagne-cupcakes-landscape-no-graphic.jpg", 
				"https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/45/1510091784-baked-by-melissa-chocolate-sundae-cupcake-1217.jpg", 
				"https://www.cookingclassy.com/wp-content/uploads/2014/09/neapolitan-cupcakes7-edit-srgb..jpg", 
				"https://www.cookwithmanali.com/wp-content/uploads/2017/01/Eggless-Vanilla-Cupcakes-500x375.jpg", 
				"https://cdn.cupcakeproject.com/wp-content/uploads/2010/10/Apple-Cupcakes-07.jpg", 
				"https://sweetandsavorymeals.com/wp-content/uploads/2018/03/Unicorn-Cupcakes-4.jpg", 
				"https://images-gmi-pmc.edge-generalmills.com/08663952-9f88-4b3f-aa79-c3122ac1601c.jpg", 
				"https://www.tablefortwoblog.com/wp-content/uploads/2013/01/wedding-cupcakes-tablefortwoblog-3.jpg", 
				"https://i.pinimg.com/236x/7c/35/2d/7c352dcde48ed835670f3f9fb92eb344.jpg", 
				"https://i.pinimg.com/236x/1b/7f/54/1b7f54ba3f6012b2bf94a9a6f271750e.jpg", 
				"https://i.pinimg.com/236x/10/a5/cc/10a5cc81b24938396cfd71af1925bf94.jpg",
				"https://i.pinimg.com/236x/92/e2/1c/92e21cb338951205858357052b691902.jpg",
				"https://i.pinimg.com/236x/81/41/b5/8141b5d8c6be2a6d8fe8a9402f36754b.jpg",
				"https://i.pinimg.com/236x/90/fc/8b/90fc8bd04f3373ec04502270185fd7f5.jpg",
				"https://i.pinimg.com/236x/72/70/bf/7270bf57d0b8c6cc5676fe62a45a49a0.jpg",
				"https://i.pinimg.com/236x/cf/e7/5c/cfe75cc588be37c1bfee1f404d71c807.jpg",
				"https://i.pinimg.com/236x/7d/d2/8c/7dd28c70175f8cc8f3e7824494622649.jpg",
				"https://i.pinimg.com/236x/62/38/0d/62380d6ca6c8f4437423e211e43b6cec.jpg",
				"https://i.pinimg.com/236x/31/d7/09/31d70903ab833bf67b1967659f3af2ff.jpg",
				"https://i.pinimg.com/236x/d4/7f/66/d47f66c619ebc75711a06742607fbe75.jpg",
				"https://i.pinimg.com/236x/09/70/2d/09702d236d2a42aaf8b32de5172dfeb8.jpg"]
			cupcake = random.choice(cupcakeimgs)
			edbm = discord.Embed(title="CUPCAKE :two_hearts:", description="omg look at that icing i-", color=cola)
			edbm.set_image(url=cupcake)
			edbm.set_footer(text='Requested by: {0}'.format(context.message.author))
			await context.message.channel.send(embed=edbm)
		elif topic == ('pizza'):
			pizzaimgs = ["https://www.simplyrecipes.com/wp-content/uploads/2019/09/easy-pepperoni-pizza-lead-4.jpg", 
				"https://assets.kraftwhatscooking.ca/adaptivemedia/rendition/122046_3000x2000.jpg?id=12a910429e20fa8ff0ce0d1c2d6382bce0213672&ht=250&wd=375&clid=KRCA", 
				"https://www.abeautifulplate.com/wp-content/uploads/2015/08/the-best-homemade-margherita-pizza-1-4-480x480.jpg", 
				"https://i.cbc.ca/1.3993184.1583946118!/fileImage/httpImage/hawaiian-pizza-pineapple-pizza.jpg", 
				"https://storage-cube.quebecormedia.com/v1/cl_prod/canadian_living/bbd3e23858ce9459564e706b39900536355b72d8/deluxe-pizza.jpg", 
				"https://cavendishbeachpei.com/wp-content/uploads/2018/07/15IN_PIZZA-1.jpg", 
				"https://images.thestar.com/6d0PmzpMTWrYs0cRJBKRYMIX8tA=/968x613/smart/filters:cb(2700061000)/https://www.stcatharinesstandard.ca/content/dam/niagaradailies/life/food-wine/restaurants/2020/04/23/hold-the-covid-niagara-falls-pizzeria-turning-up-oven-for-project-share/B881116193Z.1_20200423195113_000_G9OUG4SS.3-0_Gallery.jpg", 
				"https://static.toiimg.com/photo/76481989.cms", 
				"https://www.insauga.com/sites/default/files/article/2020/04/boston_pizza.jpg",
				"https://i.pinimg.com/236x/7c/fd/34/7cfd343fe793152cd2638989bc88dfd0.jpg",
				"https://i.pinimg.com/236x/1c/21/02/1c21027542b1e90afb3d154f41370823.jpg",
				"https://i.pinimg.com/236x/b6/26/45/b62645cd188f9ba9afcb85b46dc62432.jpg",
				"https://i.pinimg.com/236x/d5/e9/ef/d5e9efb16372fd2c65940e07ae61fd90.jpg",
				"https://i.pinimg.com/236x/c4/3a/41/c43a41181de81ee4a561d1c76e2f0404.jpg",
				"https://i.pinimg.com/236x/38/89/3b/38893b34052b8e6866b1018d231dfd60.jpg",
				"https://i.pinimg.com/236x/bf/84/45/bf8445c0ddb202c2f81b9a4af9fdba74.jpg",
				"https://i.pinimg.com/236x/26/0e/42/260e42b3be650de1d780711be3ddfc43.jpg"]
			pizza = random.choice(pizzaimgs)
			edbm = discord.Embed(title="PIZZA :sparkles:", description="time to eat pizzaa", color=cola)
			edbm.set_image(url=pizza)
			edbm.set_footer(text='Requested by: {0}'.format(context.message.author))
			await context.message.channel.send(embed=edbm)
		elif topic == ('cat'):
			catimgs=['https://placekitten.com/600/800',
				'https://placekitten.com/200/400',
				'https://placekitten.com/400/600',
				'https://placekitten.com/600/600',
				'https://placekitten.com/200/300',
				'https://placekitten.com/600/400']
			cat = random.choice(catimgs)
			edbm = discord.Embed(title="KITTY :cat:", description="*meow*", color=cola)
			edbm.set_image(url=cat)
			edbm.set_footer(text='Requested by: {0}'.format(context.message.author))
			await context.message.channel.send(embed=edbm)
			print (cat)
		elif topic == ('bup'):
			edbm = discord.Embed(title=("BUP"), description=" -- ", color=cola)
			edbm.set_image(url='https://imageproxy.ifunny.co/crop:square,resize:100x,quality:90x75/user_photos/e9a084a277bfb51a7d9113f8f5b1b9ddec06bb12_0.jpg')
			edbm.set_footer(text='Requested by: {0}'.format(context.message.author))
			await context.message.channel.send(embed=edbm)
			emoji = client.get_emoji(737333737158606908)
			await context.message.add_reaction(emoji)
		elif topic == ('pog'):
			edbm = discord.Embed(title=("POG"), description=" -- ", color=cola)
			edbm.set_image(url='https://forum.politicsandwar.com/uploads/profile/photo-thumb-220.png')
			edbm.set_footer(text='Requested by: {0}'.format(context.message.author))
			await context.message.channel.send(embed=edbm)
			emoji = client.get_emoji(735905627267793006)
			await context.message.add_reaction(emoji)
		else:
			randomchoices = "0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"
			random1 = random.choice(randomchoices)
			random2 = random.choice(randomchoices)
			random3 = random.choice(randomchoices)
			random4 = random.choice(randomchoices)
			random5 = random.choice(randomchoices)
			random6 = random.choice(randomchoices)
			randomstr = "{0}{1}{2}{3}{4}{5}".format(random1,random2,random3,random4,random5,random6)
			edbm = discord.Embed(title=(topic), description="hmm", color=cola)
			edbm.set_image(url='https://dummyimage.com/400x400/{0}/fff&text={1}'.format(randomstr,topic))
			edbm.set_footer(text='Requested by: {0}'.format(context.message.author))
			await context.message.channel.send(embed=edbm)

@client.command(name='sentence', pass_context=True)
async def sentence(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		nouns = ("puppy", "man", "rabbit", "girl", "monkey")
		verbs = ("runs", "hits", "jumps", "drives", "barfs") 
		adv = ("crazily.", "quickly.", "foolishly.", "merrily.", "occasionally.")
		adj = ("adorable", "clueless", "dirty", "odd", "stupid")
		num = random.randrange(0,5)
		numb = random.randrange(0,5)
		numbe = random.randrange(0,5)
		number = random.randrange(0,5)
		await context.message.channel.send(' ' + adj[num] + ' ' + nouns[numb] + ' ' + verbs[numbe] + ' ' + adv[number])

@client.command(name='checkword', pass_context=True)
async def checkword(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		d = enchant.Dict("en_US")
		checkword = ' '.join(args)
		print (d.check(checkword))
		if d.check(checkword) == True:
			await context.message.channel.send("Yep, that's a word")
		else:
			await context.message.channel.send("Sorry, I don't think that's a word...")

@client.command(name='define', pass_context=True, aliases=['english', 'en'])
async def define(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		word = ' '.join(args)
		req = requests.get("https://api.dictionaryapi.dev/api/v1/entries/en/{}" .format(word))
		dta = json.loads(req.text)
		if d.check(word) == True:
			try:
				definition = dta[0]['meaning']['adjective'][0]['definition']
				print (definition)
				embld = discord.Embed(title=(word),
							  description=(definition), color=cola)
				await context.message.channel.send(embed=embld)
			except Exception:
				try:
					definition = dta[0]['meaning']['adverb'][0]['definition']
					print (definition)
					embld = discord.Embed(title=(word),
							  description=(definition), color=cola)
					await context.message.channel.send(embed=embld)
				except Exception:
					try:
						definition = dta[0]['meaning']['transitive verb'][0]['definition']
						print (definition)
						embld = discord.Embed(title=(word),
									  description=(definition), color=cola)
						await context.message.channel.send(embed=embld)
					except Exception:
						try:
							definition = dta[0]['meaning']['intransitive verb'][0]['definition']
							print (definition)
							embld = discord.Embed(title=(word),
										  description=(definition), color=cola)
							await context.message.channel.send(embed=embld)
						except Exception:
							try:
								definition = dta[0]['meaning']['exclamation'][0]['definition']
								print (definition)
								embld = discord.Embed(title=(word),
											  description=(definition), color=cola)
								await context.message.channel.send(embed=embld)
							except Exception:
								try:
									definition = dta[0]['meaning']['conjunction'][0]['definition']
									print (definition)
									embld = discord.Embed(title=(word),
											  	  description=(definition), color=cola)
									await context.message.channel.send(embed=embld)
								except Exception:
									try:
										definition = dta[0]['meaning']['pronoun'][0]['definition']
										print (definition)
										embld = discord.Embed(title=(word),
											  		  description=(definition), color=cola)
										await context.message.channel.send(embed=embld)
									except Exception:
										try:
											definition = dta[0]['meaning']['determiner'][0]['definition']
											print (definition)
											embld = discord.Embed(title=(word),
											  			  description=(definition), color=cola)
											await context.message.channel.send(embed=embld)
										except Exception:
											try:
												definition = dta[0]['meaning']['verb'][0]['definition']
												print (definition)
												embld = discord.Embed(title=(word),
															  description=(definition), color=cola)
												await context.message.channel.send(embed=embld)
											except Exception:
												try:
													definition = dta[0]['meaning']['noun'][0]['definition']
													print (definition)
													embld = discord.Embed(title=(word),
																  description=(definition), color=cola)
													await context.message.channel.send(embed=embld)
												except Exception:
													await context.message.channel.send('dang, idk')
		if d.check(word) == False:
			await context.message.channel.send("bruhhh that not a wordd")

@client.command(name='synonyms', pass_context=True, aliases=['sy', 'syn'])
async def synonyms(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		word = ' '.join(args)
		req = requests.get("https://api.dictionaryapi.dev/api/v1/entries/en/{}" .format(word))
		dta = json.loads(req.text)
		if d.check(word) == True:
			try:
				synonyms = dta[0]['meaning']['adjective'][0]['synonyms'][0]
				synonymss = dta[0]['meaning']['adjective'][0]['synonyms'][1]
				synonymsss = dta[0]['meaning']['adjective'][0]['synonyms'][2]
				print (synonyms)
				embld = discord.Embed(title=(word),
							  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
				await context.message.channel.send(embed=embld)
			except Exception:
				try:
					synonyms = dta[0]['meaning']['adverb'][0]['synonyms'][0]
					synonymss = dta[0]['meaning']['adverb'][0]['synonyms'][1]
					synonymsss = dta[0]['meaning']['adverb'][0]['synonyms'][2]
					print (synonyms)
					embld = discord.Embed(title=(word),
							  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
					await context.message.channel.send(embed=embld)
				except Exception:
					try:
						synonyms = dta[0]['meaning']['transitive verb'][0]['synonyms'][0]
						synonymss = dta[0]['meaning']['transitive verb'][0]['synonyms'][1]
						synonymsss = dta[0]['meaning']['transitive verb'][0]['synonyms'][2]
						print (synonyms)
						embld = discord.Embed(title=(word),
									  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
						await context.message.channel.send(embed=embld)
					except Exception:
						try:
							synonyms = dta[0]['meaning']['intransitive verb'][0]['synonyms'][0]
							synonymss = dta[0]['meaning']['intransitive verb'][0]['synonyms'][1]
							synonymsss = dta[0]['meaning']['intransitive verb'][0]['synonyms'][2]
							print (synonyms)
							embld = discord.Embed(title=(word),
										  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
							await context.message.channel.send(embed=embld)
						except Exception:
							try:
								synonyms = dta[0]['meaning']['exclamation'][0]['synonyms'][0]
								synonymss = dta[0]['meaning']['exclamation'][0]['synonyms'][1]
								synonymsss = dta[0]['meaning']['exclamation'][0]['synonyms'][2]
								print (synonyms)
								embld = discord.Embed(title=(word),
											  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
								await context.message.channel.send(embed=embld)
							except Exception:
								try:
									synonyms = dta[0]['meaning']['conjunction'][0]['synonyms'][0]
									synonymss = dta[0]['meaning']['conjunction'][0]['synonyms'][1]
									synonymsss = dta[0]['meaning']['conjunction'][0]['synonyms'][2]
									print (synonyms)
									embld = discord.Embed(title=(word),
											  	  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
									await context.message.channel.send(embed=embld)
								except Exception:
									try:
										synonyms = dta[0]['meaning']['pronoun'][0]['synonyms'][0]
										synonymss = dta[0]['meaning']['pronoun'][0]['synonyms'][1]
										synonymsss = dta[0]['meaning']['pronoun'][0]['synonyms'][2]
										print (synonyms)
										embld = discord.Embed(title=(word),
											  		  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
										await context.message.channel.send(embed=embld)
									except Exception:
										try:
											synonyms = dta[0]['meaning']['determiner'][0]['synonyms'][0]
											synonymss = dta[0]['meaning']['determiner'][0]['synonyms'][1]
											synonymsss = dta[0]['meaning']['determiner'][0]['synonyms'][2]
											print (synonyms)
											embld = discord.Embed(title=(word),
											  			  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
											await context.message.channel.send(embed=embld)
										except Exception:
											try:
												synonyms = dta[0]['meaning']['verb'][0]['synonyms'][0]
												synonymss = dta[0]['meaning']['verb'][0]['synonyms'][1]
												synonymsss = dta[0]['meaning']['verb'][0]['synonyms'][2]
												print (synonyms)
												embld = discord.Embed(title=(word),
															  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
												await context.message.channel.send(embed=embld)
											except Exception:
												try:
													synonyms = dta[0]['meaning']['noun'][0]['synonyms'][0]
													synonymss = dta[0]['meaning']['noun'][0]['synonyms'][1]
													synonymsss = dta[0]['meaning']['noun'][0]['synonyms'][2]
													print (synonyms)
													embld = discord.Embed(title=(word),
																  description=("Here are some that I found: {}, {} and {}.").format(synonyms, synonymss, synonymsss), color=cola)
													await context.message.channel.send(embed=embld)
												except Exception:
													await context.message.channel.send('dang, idk')
		if d.check(word) == False:
			await context.message.channel.send("bruhhh that not a wordd")

@client.command(name='kick', pass_context=True)
async def kick(context, member: discord.Member, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.kick_members:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=cola)
				await context.message.channel.send(embed=embed)
			else:
				mesg = ' '.join(args)
				embed = discord.Embed(title='User Kicked!', description='**{0}** was kicked by **{1}**!'.format(member, context.message.author),color=cola)
				embed.add_field(name='Reason:', value='{}'.format(mesg))
				await context.message.channel.send(embed=embed)
				if member.bot != True:
					await member.send('You where kicked by **{0}**!  '.format(context.message.author) + 'Reason: {0}'.format(mesg))
				await member.kick()
				await context.message.delete()
					
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=cola)
			await context.message.channel.send(embed=embed)

@client.command(pass_context=True)
async def nick(context, member: discord.Member, nick):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.manage_nicknames:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=cola)
				await context.message.channel.send(embed=embed)
			else:
				embed = discord.Embed(title='Nickname Changed!', description="**{0}** 's nickname was changed by **{1}**!".format(member,
																												context.message.author),
									  color=cola)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.edit(nick=nick)
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=cola)
			await context.message.channel.send(embed=embed)

@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=cola)
				await context.message.channel.send(embed=embed)
			else:
				mesg = ' '.join(args)
				embed = discord.Embed(title='User Banned!', description='**{0}** was banned by **{1}**!'.format(member,
																												context.message.author),
									  color=cola)
				embed.add_field(name='Reason:', value=mesg)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.send('You where banned by **{0}**!'.format(
					context.message.author) + 'Reason: {0}'.format(mesg))
				await member.ban()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=cola)
			await context.message.channel.send(embed=embed)

@client.command(name='unban', pass_context=True)
async def unban(context, user: discord.Member):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			embed = discord.Embed(title='User Unbanned!',
								  description='**{0}** was unbanned by **{1}**!'.format(user, context.message.author),
								  color=cola)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await user.send('You where unbanned by **{0}**!  '.format(context.message.author) + 'Reason: Ban revoked')
			await user.unban()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=cola)
			await context.message.channel.send(embed=embed)


@client.command(name='warn', pass_context=True)
async def warn(context, member: discord.Member, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			mesg = ' '.join(args)
			embed = discord.Embed(title='User Warned!',
								  description='**{0}** was warned by **{1}**!'.format(member, context.message.author),
								  color=cola)
			embed.add_field(name='Reason:', value=mesg)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await member.send('You were warned by **{0}**!  '.format(context.message.author) + 'Reason: {0}'.format(mesg))
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=cola)
			await context.message.channel.send(embed=embed)

@client.command(name='purge', pass_context=True)
async def purge(context, number):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.manage_messages:
			numberr = int(number)+1
			await context.message.channel.purge(limit=numberr)
			await asyncio.sleep(2)
			embed = discord.Embed(title='Chat Cleared!', description='**{}** cleared **{}** messages!'.format(context.message.author, number), color=cola)
			message = await context.message.channel.send(embed=embed)
			await asyncio.sleep(3)
			await message.delete()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=cola)
			await context.message.channel.send(embed=embed)

@client.command(name='blacklist', pass_context=True)
async def blacklistt(context, mode : str, user : discord.User = None):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if (mode.lower() == "add"):
				try:
					blacklist.append(user.id)
					embed = discord.Embed(title="User Blacklisted", description='**{0}** has been successfully added to the blacklist'.format(user.name), color=cola)
					embed.set_footer(text='There are now {0} users in the blacklist'.format(len(blacklist)))
					await context.message.channel.send(embed=embed)
				except:
					embed = discord.Embed(title=":x: Error!", description="An unknown error occurred when trying to add **{0}** to the blacklist.".format(user.name), color=0xFF0000)
					await context.message.channel.send(embed=embed)
			elif (mode.lower() == "remove"):
				try:
					blacklist.remove(user.id)
					embed = discord.Embed(title="User Unblacklisted",
										  description='**{0}** has been successfully removed from the blacklist'.format(
											  user.name), color=cola)
					embed.set_footer(text='There are now {0} users in the blacklist'.format(len(blacklist)))
					await context.message.channel.send(embed=embed)
				except:
					embed = discord.Embed(title=":x: Error!",
										  description="An unknown error occurred when trying to remove **{0}** from the blacklist.\nAre you sure the user is in the blacklist?".format(
											  user.name), color=0xFF0000)
					await context.message.channel.send(embed=embed)
			elif (mode.lower() == "list"):
				embed = discord.Embed(title="There are currently {0} blacklisted IDs".format(len(blacklist)),
									  description="{0}".format(blacklist),
									  color=cola)
				await context.message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF0000)
			await context.message.channel.send(embed=embed)

client.remove_command('help')

@client.command(name='help', description='HELPPPP.', brief='commands', pass_context=True, aliases=['Help'])
async def help(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=cola)
		await context.message.channel.send(embed=embed)
	else:
		mesagg = ' '.join(args)
		print (mesagg)
		if mesagg == ('info'):
			embed = discord.Embed(title='Fiona', description='commands - info', color=cola)
			embed.add_field(name='Info (bot) - I want to tell you guys more about me! :smile:', value='Usage: fi info', inline=False)
			embed.add_field(name='Info (bot) - My story! :)', value='Usage: fi detailedinfo', inline=False)
			embed.add_field(name='Info (server) - I bet I know more about this server than you', value='Usage: fi serverinfo', inline=False)
			embed.add_field(name='Info (user) - Take a look at your online self ', value='Usage: fi userinfo', inline=False)
			embed.add_field(name='Info (Spotify) - See what others are listening to ', value='Usage: fi spotify', inline=False)
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('fun'):
			embed = discord.Embed(title='Fiona', description='commands - fun', color=cola)
			embed.add_field(name='8ball - Answers to your futile questions :8ball:', value='Usage: fi 8ball <question>', inline=False)
			embed.add_field(name='Say - I say what you say',value='Usage: fi say <message>', inline=False)
			embed.add_field(name='Embed - I say what you say in an embed message', value='Usage: fi embed <message>', inline=False)
			embed.add_field(name='Trivia - Ahaha! test out your knowledge!', value='Usage: fi trivia', inline=False)
			embed.add_field(name='Image - Imma find some pics of stufs',value='Usage: fi image <anything>', inline=False)
			embed.add_field(name='Quote - To cheer you up!',value='Usage: fi quote', inline=False)
			embed.add_field(name='Colour - Just some facts about colors!',value='Usage: fi colour <color>', inline=False)
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('mod'):
			embed = discord.Embed(title='Fiona', description='commands - mod', color=cola)
			embed.add_field(name='Kick - Kick someone out', value='Usage: fi kick <user> <reason>', inline=False)
			embed.add_field(name='Ban - Ban someone cuz they should not be here', value='Usage: fi ban <user> <reason>', inline=False)
			embed.add_field(name='Warn - Warn someone in DMs, (yea, imma do the dirty work for you :ok_hand:)', value='Usage: fi warn <user> <reason>', inline=False)
			embed.add_field(name='Unban - Unban someone', value='Usage: fi unban <user>', inline=False)
			embed.add_field(name='Purge - Let me delete messages so you do not need to do it one-by-one', value='Usage: fi purge <number>', inline=False)
			embed.add_field(name='Nickname - Save some time, let me help you nickname a user', value='Usage: fi nick <user> <new nickname>')
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('tools'):
			embed = discord.Embed(title='Fiona', description='commands - tools', color=cola)
			embed.add_field(name='Poll - Create a poll with me because why not', value='Usage: fi poll<1/2> <idea>', inline=False)
			embed.add_field(name='BMI check - Check if your weight is healthy', value='Usage: fi bmi', inline=False)
			embed.add_field(name='Warn - Warn someone in DMs, (yea, imma do the dirty work for you :ok_hand:)', value='Usage: fi warn <user> <reason>', inline=False)
			embed.add_field(name='Definitions - Define a word with me', value='Usage: fi define <word>', inline=False)			
			embed.add_field(name='Synonyms - Find some synonyms with me', value='Usage: fi synonyms <word>', inline=False)
			embed.add_field(name='Check Word - Check a word with me', value='Usage: fi checkword <word>', inline=False)
			embed.add_field(name='Help - Gives this AWESOME menu :sunglasses:', value='Usage: fi help', inline=False)
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('other'):
			embed = discord.Embed(title='Fiona', description='commands - other', color=cola)
			embed.add_field(name='Invite - Invite me! I wanna be in more servers :pleading_face:', value='Usage: fi invite', inline=False)
			embed.add_field(name='Server - Join my server!', value='Usage: fi server', inline=False)
			await context.message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title='Fiona', description='commands', color=cola)
			embed.add_field(name='Info - fi help info', value='some things abt me, you, and the server', inline=False)
			embed.add_field(name='Fun - fi help fun', value='idk, use if you are bored', inline=False)
			embed.add_field(name='Mod - fi help mod', value='in case moderating a server is too much work', inline=False)
			embed.add_field(name='Tools - fi help tools', value="to make everyone's life easier", inline=False)
			embed.add_field(name='Other - fi help other', value='uselesss stufs', inline=False)
			await context.message.channel.send(embed=embed)
		

@blacklistt.error
async def blacklist_error(context, error):
	embed = discord.Embed(title='**Command:** fi blacklist', description='**Description::** Prevents a user from using the bot \n **Usage:** fi blacklist [add/remove/list] [user] \n **Example:** fi blacklist add @RandomUser', color=cola)
	await context.message.channel.send(embed=embed)

@ban.error
async def ban_error(context, error):
	embed = discord.Embed(title='**Command:** fi ban', description='**Description:** Bans a member \n **Usage:** fi ban [user] [reason] \n **Example:** fi ban @RandomUser Get out! You suck!', color=cola)
	await context.message.channel.send(embed=embed)

@poll.error
async def poll_error(context, error):
	embed = discord.Embed(title='**Command:** fi poll', description='**Description:** Create a poll to vote \n **Usage:** fi poll[1/2] [idea] \n **Example:** fi poll1 Should we play another game as a server?', color=cola)
	await context.message.channel.send(embed=embed)
@poll2.error
async def poll2_error(context, error):
	embed = discord.Embed(title='**Command:** fi poll2', description='**Description:** Create a poll to vote \n **Usage:** fi poll2 [idea] \n **Example:** fi poll2 Are you free tomorrow?', color=cola)
	await context.message.channel.send(embed=embed)

@eight_ball.error
async def eight_ball_error(context, error):
	embed = discord.Embed(title='**Command:** fi 8ball', description='**Description:** Get an answer to all of your questions, sometimes my answers can be quite... cruel :smiling_imp: \n **Usage:** fi 8ball [question] \n **Example:** fi 8ball Is this bot cool?', color=cola)
	await context.message.channel.send(embed=embed)

@say.error
async def say_error(context, error):
	embed = discord.Embed(title='**Command:** fi say',
						  description='**Description:** I say what you say because I wanna be cool like you :wink:\n **Usage:** fi say [message] \n **Example:** fi say Hello!!',
						  color=cola)
	await context.message.channel.send(embed=embed)

@embed.error
async def embed_error(context, error):
	embed = discord.Embed(title='**Command:** fi embed',
						  description='**Description:** I say what you say as an embed message because I can and you cannot do it :innocent:\n **Usage:** fi embed [message] \n **Example:** fi embed Hello!!',
						  color=cola)
	await context.message.channel.send(embed=embed)

@unban.error
async def unban_error(context, error):
	embed = discord.Embed(title='**Command:** fi unban',
						  description='**Description:** Unbans a member because they should not be banned and you were wrong for doing so in the first place \n **Usage:** fi unban [user] \n **Example:** fi unban @RandomUser',
						  color=cola)
	await context.message.channel.send(embed=embed)

@warn.error
async def warn_error(context, error):
	embed = discord.Embed(title='**Command:** fi warn',
						  description='**Description:** Warns a member, use only is necessary \n **Usage:** fi warn [user] [reason] \n **Example:** fi warn @RandomUser Stop the caps, thanks!',
						  color=cola)
	await context.message.channel.send(embed=embed)

@purge.error
async def purge_error(context, error):
	embed = discord.Embed(title='**Command:** fi purge',
						  description='**Description:** Deletes a certain amount of messages to make your life easier \n **Usage:** fi purge [number of messages] \n **Example:** fi purge 20',
						  color=cola)
	await context.message.channel.send(embed=embed)

@trivia.error
async def trivia_error(context, error):
	if isinstance(error, commands.CommandOnCooldown):
		if error.retry_after == '0':
			return await context.message.channel.send(f"This command is on a cooldown. Try again in ... less than a second :)")
		else:
			return await context.message.channel.send(f"This command is on a cooldown. Try again in {int(error.retry_after)} second(s).")

@define.error
async def define_error(context, error):
	embed = discord.Embed(title='**Command:** fi define',
						  description='**Description:** Let me define a word for you\n **Usage:** fi define [word] \n **Example:** fi define nice',
						  color=cola)
	await context.message.channel.send(embed=embed)

@synonyms.error
async def synonyms_error(context, error):
	embed = discord.Embed(title='**Command:** fi define',
						  description='**Description:** Let me find some synonyms of a word for you\n **Usage:** fi synonyms [word] \n **Example:** fi define nice',
						  color=cola)
	await context.message.channel.send(embed=embed)

client.run(token)
