import discord
import requests
import asyncio
import json
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from random import randint
from discord.ext import commands
from platform import python_version
import os
import platform

bprefix = ('fi ', 'Fi ')
token = 'eeeeeeeeeee'
me = [511025033976741889]
blacklist = []
client = Bot(command_prefix=bprefix)



async def status_task():
	while True:
		await client.change_presence(activity=discord.Game("fi help"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you guys"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you guys"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("with my status!"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="2 servers"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("something"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="you"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("fi help"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game("with my friends!"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my parents"))
		await asyncio.sleep(10)

@client.event
async def on_ready():
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
		e = discord.Embed(description='not done', color=0xFF8CC4,title='**__Bot Information__**')
		e.add_field(name="Owner:", value="occona#9933", inline=True)
		e.add_field(name="Python Version:", value="{0}".format(python_version()), inline=True)
		e.add_field(name="Prefix:", value="fi ", inline=False)
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
		time = str(server.created_at)
		time = time.split(' ')
		time = time[0]
		em = discord.Embed(description='%s ' % (str(server)), title='**__Server Name:__**', color=0xFF8CC4)
		em.set_thumbnail(url=server.icon_url)
		em.add_field(name='Owner', value=str(server.owner) + '\n' + str(server.owner.id))
		em.add_field(name='Server ID', value=str(server.id))
		em.add_field(name='Member Count', value=str(server.member_count))
		em.add_field(name='Text/Voice Channels', value=str(channels))
		em.add_field(name='Roles (%s)' % str(role_length), value=roles)
		em.set_footer(text='Created at: %s' % time)
		await context.message.channel.send(embed=em)

@client.command(name='myinfo', pass_context=True)
async def myinfo(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		asker = context.message.author
		status = asker.status
		role = asker.top_role
		nname = asker.display_name
		joined = asker.joined_at
		eb = discord.Embed(description=str(asker), color=0xFF8CC4, title='**__User Information__**')
		eb.add_field(name="Displayed Name:", value=str(nname), inline=True)
		eb.add_field(name="Current Status:", value=str(status), inline=False)
		eb.add_field(name="Joined date:", value=str(joined), inline=False)
		eb.add_field(name="Top Role", value=str(role), inline=False)
		eb.set_footer(text="Requested by {0}".format(context.message.author))
		await context.message.channel.send(embed=eb)
    
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
		await context.message.author.send('Join my discord server by clicking here: https://discord.gg/5KJPzz')

@client.command(name='poll', pass_context=True)
async def poll(context, *args):
	mesg = ' '.join(args)
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		await context.message.delete()
		ebd = discord.Embed(title='Ahhh add 1 or 2 behind what you just sent me dummy!', description='{0}'.format(mesg), color=0xFF8CC4)
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

@client.command(name='8ball', pass_context=True)
async def eight_ball(context, *args):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
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
				await member.send('You where warned by **{0}**!  '.format(context.message.author) + 'Reason: {0}'.format(mesg))
				await member.kick()
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
								  color=0xFF8CC4)
			await context.message.channel.send(embed=embed)

@client.command(name='bmi', pass_context=True)
async def bmi(context, *args):

	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!',
							  description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		ebed = discord.Embed(title='**Weight** ', description='What is your weight in kg?', color=0xFF8CC4)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebed)
		def check(m):
			return m.author == context.message.author and m.channel == context.message.channel
		try:
			msg = await client.wait_for("message", check=check, timeout=30)
		except TimeoutError:
			return await context.message.channel.send("Timed out, try again.")
		w = int(msg.content)
		eed = discord.Embed(title='**Height** ', description='What is your height in cm?', color=0xFF8CC4)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=eed)
		try:
			mg = await client.wait_for("message", check=check, timeout=30)
		except TimeoutError:
			return await context.message.channel.send("Timed out, try again.")
		h = int(mg.content)
		bmi = w / (h ** 2) * 10000
		BMI = (round(bmi,2))
		ebed = discord.Embed(title='**BMI** ', description='Your BMI is {}'.format (BMI), color=0xFF8CC4)
		ebed.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebed)
		if(bmi <= 18.5):
			fat = "underweight"
		elif(bmi > 18.5 and bmi <= 24.9):
			fat = ("normal weight")
		elif(bmi > 24.9 and bmi <= 29.9):
			fat = ("overweight")
		else:
			fat = ("obesity")
		ebd = discord.Embed(title='**BMI** ', description='The classification of your BMI is {}'.format (fat), color=0xFF8CC4)
		ebd.set_footer(text='Requested by: {0}'.format(context.message.author))
		await context.message.channel.send(embed=ebd)

@client.command(name='nick', pass_context=True)
async def nick(context, member: discord.Member, *, name : str):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		if context.message.author.guild_permissions.administrator:
			if name.lower() == "!reset":
				name = None
			embed = discord.Embed(title='Changed Nickname!', description='**{0}** new nickname is **{1}**!'.format(member, name), color=0xFF8CC4)
			await context.message.channel.send(embed=embed)
			await context.message.delete()
			await member.change_nickname(name)
		else:
			embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.', color=0xFF8CC4)
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

@client.command(name='help', description='HELPPPP.', brief='commands', pass_context=True)
async def help(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Fiona', description='commands', color=0xFF8CC4)
		embed.add_field(name='Info - fi helpinfo', value='or you can use fi hinfo', inline=False)
		embed.add_field(name='Fun - fi helpfun', value='or you can use fi hfun', inline=False)
		embed.add_field(name='Mod - fi helpmod', value='or you can use fi hmod', inline=False)
		embed.add_field(name='Tools - fi helptools', value='or you can use fi htools', inline=False)
		embed.add_field(name='Other - fi helpother', value='or you can use fi hother', inline=False)
		await context.message.channel.send(embed=embed)

@client.command(name='helpinfo', pass_context=True, aliases=['hinfo'])
async def helpinfo(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Fiona', description='commands - info', color=0xFF8CC4)
		embed.add_field(name='Info (bot) - I want to tell you guys more about me! :smile:', value='Usage: fi info', inline=False)
		embed.add_field(name='Info (bot) - My story! :)', value='Usage: fi detailedinfo', inline=False)
		embed.add_field(name='Info (server) - I bet I know more about this server than you', value='Usage: fi serverinfo', inline=False)
		embed.add_field(name='Info (you) - Take a look at your online self ', value='Usage: fi myinfo', inline=False)
		await context.message.channel.send(embed=embed)
	

@client.command(name='helpfun', pass_context=True, aliases=['hfun'])
async def helpfun(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Fiona', description='commands - fun', color=0xFF8CC4)
		embed.add_field(name='8Ball - Answers to your futile questions :8ball:', value='Usage: fi 8ball <question>', inline=False)
		embed.add_field(name='Say - I say what you say',value='Usage: fi say <message>', inline=False)
		embed.add_field(name='Embed - I say what you say in an embed message', value='Usage: fi embed <message>', inline=False)
		await context.message.channel.send(embed=embed)

@client.command(name='helpmod', pass_context=True, aliases=['hmod'])
async def helpmod(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Fiona', description='commands - mod', color=0xFF8CC4)
		embed.add_field(name='Kick - Kick someone out', value='Usage: fi kick <user> <reason>', inline=False)
		embed.add_field(name='Ban - Ban someone cuz they should not be here', value='Usage: fi ban <user> <reason>', inline=False)
		embed.add_field(name='Warn - Warn someone in DMs, (yea, imma do the dirty work for you :ok_hand:)', value='Usage: fi warn <user> <reason>', inline=False)
		embed.add_field(name='Unban - Unban someone', value='Usage: fi unban <user>', inline=False)
		embed.add_field(name='Purge - Let me delete messages so you do not need to do it one-by-one', value='Usage: fi purge <number>', inline=False)
		await context.message.channel.send(embed=embed)

@client.command(name='helptools', pass_context=True, aliases=['htools'])
async def helptools(context):
	if context.message.author.id in blacklist:
		embed = discord.Embed(title='You\'re blacklisted!', description='If you think this is a mistake, contact the owner of this server', color=0xFF8CC4)
		await context.message.channel.send(embed=embed)
	else:
		embed = discord.Embed(title='Fiona', description='commands - tools', color=0xFF8CC4)
		embed.add_field(name='Poll - Create a poll with me because why not', value='Usage: fi poll<1/2> <idea>', inline=False)
		embed.add_field(name='BMI check - Check if your weight is healthy ', value='Usage: fi bmi', inline=False)
		embed.add_field(name='Warn - Warn someone in DMs, (yea, imma do the dirty work for you :ok_hand:)', value='Usage: fi warn <user> <reason>', inline=False)
		embed.add_field(name='Help - Gives this AWESOME menu :sunglasses:', value='Usage: fi help', inline=False)
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


@kick.error
async def kick_error(context, error):
	embed = discord.Embed(title='**Command:** fi kick',
						  description='**Description:** Kicks a member so that they will blame it all on me, not you \n **Usage:** fi kick [user] [reason] \n **Example:** fi kick @RandomUser Rejoin when you\'ll be smarter, like me!',
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

@bmi.error
async def bmi_error(context, error):
	embed = discord.Embed(title='**Command:** fi bmi',
						  description='**Description:** Body mass index (BMI) is a value derived from the mass (weight) and height of a person \n **Usage:** fi bmi [number of messages] \n **Example:** fi bmi 20',
						  color=0xFF8CC4)
	await context.message.channel.send(embed=embed)

client.run(token)
