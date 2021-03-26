import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = "fi ")

token = ('mmhm')

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! I am now ready to begin! {round (client.latency * 1000)}ms ')

@client.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

response_list = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '8 ball' in message.content:
        lucky_num = random.randint(0,len(response_list) - 1)
        await message.channel.send(response_list[lucky_num])
    if '8b' in message.content:
        lucky_num = random.randint(0,len(response_list) - 1)
        await message.channel.send(response_list[lucky_num])
        
client.run(token)
