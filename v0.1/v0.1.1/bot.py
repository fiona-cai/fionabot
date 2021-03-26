import discord
import requests
import asyncio
import json
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from random import randint
import random
from discord.ext import commands
from platform import python_version
import os
import platform
import html

import enchant
from wiktionaryparser import WiktionaryParser

bprefix = ('fi ', 'Fi ')
token = 'eeeee'
me = [511025033976741889]
blacklist = []
client = Bot(command_prefix=bprefix)
d = enchant.Dict("en_US")


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
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="2 servers"))
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
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		e = discord.Embed(description="Here you go! Free information about me!", color=0xFF8CC4,title='**__Bot Information__**')
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
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('I sent you a private message! Go check your DMs')
		await context.message.author.send("Hello Hello! I'm Fiona, nice to meet you! I'm assuming you want to know how I came to life right? well... Get ready to hear my story.")
		await context.message.author.send("My creator, occona#9933 was inspired by a bot named President Pizza. She didn't really know coding all that well but, eh she decided to give it a try. Within 48 hours, her bot, (me!) came to life. I was truly a moment for her. Thanks to all her friends, this bot quickly grew and got more and more commands! How great that made her feel! But her main concern now is that no one wants to use her bot :( hopefully this won't last for long. I really want to be in more servers and help more people... :pleading_face:")
		await context.message.author.send("Oh! haha she just texted me and wanted me to remind you that you can always give suggestions to her by DMing her. Sigh, How could I almost forget to tell you that..")

@client.command(name='serverinfo', pass_context=True)
async def serverinfo(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
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
		em = discord.Embed(description='%s ' % (str(server)), title='**__Server Name:__**', color=0xFF8CC4)
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

@client.command()
async def userinfo(ctx, *, member: discord.Member=None):
	if not member: 
		member = ctx.message.author 
	userAvatar = member.avatar_url
	status = member.status
	role = member.top_role
	nname = member.display_name
	joined = member.created_at
	eb = discord.Embed(description=str(member), color=0xFF8CC4, title='**__User Information__**')
	eb.add_field(name="Displayed Name", value=str(nname), inline=True)
	eb.add_field(name="Current Status", value=str(status), inline=False)
	eb.add_field(name="Date Joined Discord:", value=str(joined), inline=False)
	eb.add_field(name="Top Role", value=str(role), inline=False)
	eb.set_thumbnail(url=userAvatar)
	eb.set_footer(text="Requested by {0}".format(ctx.message.author))
	await ctx.send(embed=eb)

@client.command(name='ping', pass_context=True)
async def ping(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(color=0xFF8CC4)
		embed.set_footer(text='Pong request by {0}'.format(context.message.author))
		embed.add_field(name='Pong!', value="Now you know I'm ready :wink:", inline=True)
		await context.message.channel.send(embed=embed)

@client.command(name='invite', pass_context=True)
async def invite(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('I sent you a private message! Go check your DMs')
		await context.message.author.send('Invite me by clicking here: https://discord.com/api/oauth2/authorize?client_id=736372330644897893&permissions=8&scope=bot')

@client.command(name='server', pass_context=True)
async def server(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send('I sent you a private message! Go check your DMs')
		await context.message.author.send('Join my discord server by clicking here: https://discord.gg/x9h2MZq')

@client.command(name='poll', pass_context=True)
async def poll(context, *args):
	mesg = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		ebd = discord.Embed(title='Ahhh add 1 or 2 behind "poll" dummy!', description='{0}'.format(mesg), color=0xFF8CC4)
		ebd.set_footer(text='Poll created by: {0} • error!'.format(context.message.author))
		await context.message.channel.send(embed=ebd)

@client.command(name='poll1', pass_context=True)
async def poll1(context, *args):
	mesg = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		embed = discord.Embed(title='We have a poll !', description='{0}'.format(mesg), color=0xFF8CC4)
		embed.set_footer(text='Poll created by: {0} • React to vote!'.format(context.message.author))
		embed_message = await context.message.channel.send(embed=embed)
		await embed_message.add_reaction('👍')
		await embed_message.add_reaction('👎')

@client.command(name='poll2', pass_context=True)
async def poll2(context, *args):
	mesg = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		embed = discord.Embed(title='We have a poll !', description='{0}'.format(mesg), color=0xFF8CC4)
		embed.set_footer(text='Poll created by: {0} • React to vote!'.format(context.message.author))
		embed_message = await context.message.channel.send(embed=embed)
		await embed_message.add_reaction('👍')
		await embed_message.add_reaction('👎')
		await embed_message.add_reaction('🤷')

@client.command(name='8ball', pass_context=True, aliases=['8b', '8', '8bal'])
async def eight_ball(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.', 'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
		embed = discord.Embed(title='**My Answer:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=0xFF8CC4)
		embed.set_footer(text='Question asked by: {0} • Ask your own now!'.format(context.message.author))
		await context.message.channel.send(embed=embed)

@client.command(name='say', pass_context=True)
async def say(context, *, content:str):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.channel.send(context.message.content[6:].format(content))
		await context.message.delete()
           
@client.command(name='embed', pass_context=True)
async def embed(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		mesg = ' '.join(args)
		edm = discord.Embed(description=mesg, color=0xFF8CC4)
		await context.message.channel.send(embed=edm)
		await context.message.delete()

@client.command(name='bmi', pass_context=True)
async def bmi(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		ebed = discord.Embed(title='**Weight** ', description='What is your weight in kg?', color=0xFF8CC4)
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
		eed = discord.Embed(title='**Height** ', description='What is your height in cm?', color=0xFF8CC4)
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
		ebd = discord.Embed(title='**BMI** ', description='||Your BMI is {}. The classification of your BMI is {}||'.format (BMI, fat), color=0xFF8CC4)
		ebd.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebd)


@client.command(name='trivia', pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def trivia(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
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
		emed = discord.Embed(title='**Trivia Time!** ', description = (html.unescape(question)), color=0xFF8CC4)
		emed.add_field(name='a) {}'.format(a.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü')), value = "type a", inline = False)
		emed.add_field(name='b) {}'.format(b.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü')), value = "type b", inline = False)
		emed.add_field(name='c) {}'.format(c.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü')), value = "type c", inline = False)
		emed.add_field(name='d) {}'.format(d.replace("&amp;", "and").replace("&#039;", "'").replace("&aacute;", "á").replace('&uuml;', 'ü')), value = "type d", inline = False)
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

@client.command(name='checkword', pass_context=True)
async def checkword(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
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
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
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
							  description=(definition), color=0xFF8CC4)
				await context.message.channel.send(embed=embld)
			except Exception:
				try:
					definition = dta[0]['meaning']['adverb'][0]['definition']
					print (definition)
					embld = discord.Embed(title=(word),
							  description=(definition), color=0xFF8CC4)
					await context.message.channel.send(embed=embld)
				except Exception:
					try:
						definition = dta[0]['meaning']['noun'][0]['definition']
						print (definition)
						embld = discord.Embed(title=(word),
									  description=(definition), color=0xFF8CC4)
						await context.message.channel.send(embed=embld)
					except Exception:
						try:
							definition = dta[0]['meaning']['verb'][0]['definition']
							print (definition)
							embld = discord.Embed(title=(word),
										  description=(definition), color=0xFF8CC4)
							await context.message.channel.send(embed=embld)
						except Exception:
							try:
								definition = dta[0]['meaning']['exclamation'][0]['definition']
								print (definition)
								embld = discord.Embed(title=(word),
											  description=(definition), color=0xFF8CC4)
								await context.message.channel.send(embed=embld)
							except Exception:
								await context.message.channel.send('dang, idk')
		if d.check(word) == False:
			await context.message.channel.send("bruhhh that not a wordd")

@client.command(name='french', pass_context=True, aliases=['fr'])
async def french(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		word = ' '.join(args)
		req = requests.get("https://api.dictionaryapi.dev/api/v1/entries/fr/{}" .format(word))
		dta = json.loads(req.text)
		if d.check(word) == True:
			try:
				definition = dta[0]['meaning']['adjective'][0]['definition']
				print (definition)
				embld = discord.Embed(title=(word),
							  description=(definition), color=0xFF8CC4)
				await context.message.channel.send(embed=embld)
			except Exception:
				try:
					definition = dta[0]['meaning']['adverb'][0]['definition']
					print (definition)
					embld = discord.Embed(title=(word),
							  description=(definition), color=0xFF8CC4)
					await context.message.channel.send(embed=embld)
				except Exception:
					try:
						definition = dta[0]['meaning']['noun'][0]['definition']
						print (definition)
						embld = discord.Embed(title=(word),
									  description=(definition), color=0xFF8CC4)
						await context.message.channel.send(embed=embld)
					except Exception:
						try:
							definition = dta[0]['meaning']['verb'][0]['definition']
							print (definition)
							embld = discord.Embed(title=(word),
										  description=(definition), color=0xFF8CC4)
							await context.message.channel.send(embed=embld)
						except Exception:
							try:
								definition = dta[0]['meaning']['exclamation'][0]['definition']
								print (definition)
								embld = discord.Embed(title=(word),
											  description=(definition), color=0xFF8CC4)
								await context.message.channel.send(embed=embld)
							except Exception:
								try:
									definition = dta[0]['meaning']['preposition'][0]['definition']
									print (definition)
									embld = discord.Embed(title=(word),
												  description=(definition), color=0xFF8CC4)
									await context.message.channel.send(embed=embld)
								except Exception:
									await context.message.channel.send('dang, idk')
		if d.check(word) == False:
			await context.message.channel.send("bruhhh that not a wordd")

@client.command(name='kick', pass_context=True)
async def kick(context, member: discord.Member, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.kick_members:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=0xFF8CC4)
				await context.message.channel.send(embed=embed)
			else:
				mesg = ' '.join(args)
				embed = discord.Embed(title='User Kicked!', description='**{0}** was kicked by **{1}**!'.format(member,
																												context.message.author),
									  color=0xFF8CC4)
				embed.add_field(name='Reason:', value=mesg)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.send('You where kicked by **{0}**!  '.format(context.message.author) + 'Reason: {0}'.format(mesg))
				await member.kick()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)

@client.command(pass_context=True)
async def nick(context, member: discord.Member, nick):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.manage_nicknames:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=0xFF8CC4)
				await context.message.channel.send(embed=embed)
			else:
				embed = discord.Embed(title='Nickname Changed!', description="**{0}** 's nickname was changed by **{1}**!".format(member,
																												context.message.author),
									  color=0xFF8CC4)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.edit(nick=nick)
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)

@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if member.guild_permissions.administrator:
				embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=0xFF8CC4)
				await context.message.channel.send(embed=embed)
			else:
				mesg = ' '.join(args)
				embed = discord.Embed(title='User Banned!', description='**{0}** was banned by **{1}**!'.format(member,
																												context.message.author),
									  color=0xFF8CC4)
				embed.add_field(name='Reason:', value=mesg)
				await context.message.channel.send(embed=embed)
				await context.message.delete()
				await member.send('You where banned by **{0}**!'.format(
					context.message.author) + 'Reason: {0}'.format(mesg))
				await member.ban()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)

@client.command(name='unban', pass_context=True)
async def unban(context, user: discord.Member):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			embed = discord.Embed(title='User Unbanned!',
								  description='**{0}** was unbanned by **{1}**!'.format(user, context.message.author),
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await user.send('You where unbanned by **{0}**!  '.format(context.message.author) + 'Reason: Ban revoked')
			await user.unban()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)


@client.command(name='warn', pass_context=True)
async def warn(context, member: discord.Member, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			mesg = ' '.join(args)
			embed = discord.Embed(title='User Warned!',
								  description='**{0}** was warned by **{1}**!'.format(member, context.message.author),
								  color=0xFF8CC4)
			embed.add_field(name='Reason:', value=mesg)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await member.send('You were warned by **{0}**!  '.format(context.message.author) + 'Reason: {0}'.format(mesg))
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)


@client.command(name='purge', pass_context=True)
async def purge(context, number):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			number = int(number)
			await context.message.channel.purge(limit=number)
			embed = discord.Embed(title='Chat Cleared!',
								  description='**{0}** cleared **{1}** messages!'.format(context.message.author,
																						 number), color=0xFF8CC4)
			message = await context.message.channel.send(embed=embed)
			await asyncio.sleep(3)
			await message.delete()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)

@client.command(name='blacklist', pass_context=True)
async def blacklistt(context, mode : str, user : discord.User = None):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if (mode.lower() == "add"):
				try:
					blacklist.append(user.id)
					embed = discord.Embed(title="User Blacklisted", description='**{0}** has been successfully added to the blacklist'.format(user.name), color=0xFF8CC4)
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
											  user.name), color=0xFF8CC4)
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
									  color=0xFF8CC4)
				await context.message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF0000)
			await context.message.channel.send(embed=embed)

client.remove_command('help')

@client.command(name='help', description='HELPPPP.', brief='commands', pass_context=True, aliases=['Help'])
async def help(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		mesagg = ' '.join(args)
		print (mesagg)
		if mesagg == ('info'):
			embed = discord.Embed(title='Fiona', description='commands - info', color=0xFF8CC4)
			embed.add_field(name='Info (bot) - I want to tell you guys more about me! :smile:', value='Usage: fi info', inline=False)
			embed.add_field(name='Info (bot) - My story! :)', value='Usage: fi detailedinfo', inline=False)
			embed.add_field(name='Info (server) - I bet I know more about this server than you', value='Usage: fi serverinfo', inline=False)
			embed.add_field(name='Info (user) - Take a look at your online self ', value='Usage: fi userinfo', inline=False)
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('fun'):
			embed = discord.Embed(title='Fiona', description='commands - fun', color=0xFF8CC4)
			embed.add_field(name='8ball - Answers to your futile questions :8ball:', value='Usage: fi 8ball <question>', inline=False)
			embed.add_field(name='Say - I say what you say',value='Usage: fi say <message>', inline=False)
			embed.add_field(name='Embed - I say what you say in an embed message', value='Usage: fi embed <message>', inline=False)
			embed.add_field(name='Trivia - Ahaha! test out your knowledge!', value='Usage: fi trivia', inline=False)
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('mod'):
			embed = discord.Embed(title='Fiona', description='commands - mod', color=0xFF8CC4)
			embed.add_field(name='Kick - Kick someone out', value='Usage: fi kick <user> <reason>', inline=False)
			embed.add_field(name='Ban - Ban someone cuz they should not be here', value='Usage: fi ban <user> <reason>', inline=False)
			embed.add_field(name='Warn - Warn someone in DMs, (yea, imma do the dirty work for you :ok_hand:)', value='Usage: fi warn <user> <reason>', inline=False)
			embed.add_field(name='Unban - Unban someone', value='Usage: fi unban <user>', inline=False)
			embed.add_field(name='Purge - Let me delete messages so you do not need to do it one-by-one', value='Usage: fi purge <number>', inline=False)
			embed.add_field(name='Nickname - Save some time, let me help you nickname a user', value='Usage: fi nick <user> <new nickname>')
			await context.message.channel.send(embed=embed)
			
		elif mesagg == ('tools'):
			embed = discord.Embed(title='Fiona', description='commands - tools', color=0xFF8CC4)
			embed.add_field(name='Poll - Create a poll with me because why not', value='Usage: fi poll<1/2> <idea>', inline=False)
			embed.add_field(name='BMI check - Check if your weight is healthy', value='Usage: fi bmi', inline=False)
			embed.add_field(name='Warn - Warn someone in DMs, (yea, imma do the dirty work for you :ok_hand:)', value='Usage: fi warn <user> <reason>', inline=False)
			embed.add_field(name='Dictionary - Define a word with me', value='Usage: fi define <word>', inline=False)			
			embed.add_field(name='Check Word - Check a word with me', value='Usage: fi checkword <word>', inline=False)
			embed.add_field(name='Help - Gives this AWESOME menu :sunglasses:', value='Usage: fi help', inline=False)
			await context.message.channel.send(embed=embed)
			
		else:
			embed = discord.Embed(title='Fiona', description='commands', color=0xFF8CC4)
			embed.add_field(name='Info - fi help info', value='some things abt me, you, and the server', inline=False)
			embed.add_field(name='Fun - fi help fun', value='idk, use if you are bored', inline=False)
			embed.add_field(name='Mod - fi help mod', value='in case moderating a server is too much work', inline=False)
			embed.add_field(name='Tools - fi help tools', value="to make everyone's life easier", inline=False)
			embed.add_field(name='Other - fi help other', value='uselesss stufs', inline=False)
			await context.message.channel.send(embed=embed)
		
@client.command(name='helpother', pass_context=True, aliases=['hother'])
async def helpother(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Fiona', description='commands - other', color=0xFF8CC4)
		embed.add_field(name='Invite - Invite me! I wanna be in more servers :pleading_face:', value='Usage: fi invite', inline=False)
		embed.add_field(name='Server - Join my server!', value='Usage: fi server', inline=False)
		await context.message.channel.send(embed=embed)

@blacklistt.error
async def blacklist_error(context, error):
	embed = discord.Embed(title='**Command:** fi blacklist', description='**Description::** Prevents a user from using the bot \n **Usage:** fi blacklist [add/remove/list] [user] \n **Example:** fi blacklist add @RandomUser', color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@ban.error
async def ban_error(context, error):
	embed = discord.Embed(title='**Command:** fi ban', description='**Description:** Bans a member \n **Usage:** fi ban [user] [reason] \n **Example:** fi ban @RandomUser Get out! You suck!', color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@poll.error
async def poll_error(context, error):
	embed = discord.Embed(title='**Command:** fi poll', description='**Description:** Create a poll to vote \n **Usage:** fi poll[1/2] [idea] \n **Example:** fi poll1 Should we play another game as a server?', color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@poll1.error
async def poll1_error(context, error):
	embed = discord.Embed(title='**Command:** fi poll1', description='**Description:** Create a poll to vote \n **Usage:** fi poll1 [idea] \n **Example:** fi poll1 Should we play another game as a server?', color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@poll2.error
async def poll2_error(context, error):
	embed = discord.Embed(title='**Command:** fi poll2', description='**Description:** Create a poll to vote \n **Usage:** fi poll2 [idea] \n **Example:** fi poll2 Are you free tomorrow?', color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@eight_ball.error
async def eight_ball_error(context, error):
	embed = discord.Embed(title='**Command:** fi 8ball', description='**Description:** Get an answer to all of your questions, sometimes my answers can be quite... cruel :smiling_imp: \n **Usage:** fi 8ball [question] \n **Example:** fi 8ball Is this bot cool?', color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@say.error
async def say_error(context, error):
	embed = discord.Embed(title='**Command:** fi say',
						  description='**Description:** I say what you say because I wanna be cool like you :wink:\n **Usage:** fi say [message] \n **Example:** fi say Hello!!',
						  color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@embed.error
async def embed_error(context, error):
	embed = discord.Embed(title='**Command:** fi embed',
						  description='**Description:** I say what you say as an embed message because I can and you cannot do it :innocent:\n **Usage:** fi embed [message] \n **Example:** fi embed Hello!!',
						  color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@unban.error
async def unban_error(context, error):
	embed = discord.Embed(title='**Command:** fi unban',
						  description='**Description:** Unbans a member because they should not be banned and you were wrong for doing so in the first place \n **Usage:** fi unban [user] \n **Example:** fi unban @RandomUser',
						  color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@warn.error
async def warn_error(context, error):
	embed = discord.Embed(title='**Command:** fi warn',
						  description='**Description:** Warns a member, use only is necessary \n **Usage:** fi warn [user] [reason] \n **Example:** fi warn @RandomUser Stop the caps, thanks!',
						  color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

@purge.error
async def purge_error(context, error):
	embed = discord.Embed(title='**Command:** fi purge',
						  description='**Description:** Deletes a certain amount of messages to make your life easier \n **Usage:** fi purge [number of messages] \n **Example:** fi purge 20',
						  color=0xFF8CC4)
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
						  color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

client.run(token)
