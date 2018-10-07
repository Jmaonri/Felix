#!/usr/bin/python

import discord
from discord.ext.commands import bot
from discord.ext import commands
import Token #imports Token.py which holds the bot token
import asyncio
import time
import datetime
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#Startup Log
@client.event
async def on_ready():
    print(f"{client.user.name} is online and running")
    print('------')
    print("Log:\n")
    #Set the 'playing' status as the set string
    await client.change_presence(game=discord.Game(name='The Big Gay'))

@client.event
async def on_message(message):
    if message.content.lower().startswith('!github'):
        await client.send_message(message.channel, "https://github.com/Jmaonri/Felix")
    elif message.content.lower().startswith('!nut'):
        embed = discord.Embed(title = None)
        embed.set_image(url = "https://www.dailydot.com/wp-content/uploads/228/6f/ab64a69d4cd848bad23ed0f9190a91eb.jpg")
        await client.send_message(message.channel, embed = embed)
    elif message.content.lower().startswith('!gay'):
        #AFTER ONE FUCKING HOUR THIS FINALLY WORKS, DONT TOUCH THIS SHIT EVER AGAIN (nvm I broke my rule but I made it better)
        embed = discord.Embed(title = "No u faggot")
        embed.set_image(url = "https://myanimelist.cdn-dena.com/images/characters/5/353573.jpg")
        await client.send_message(message.author, embed = embed)
    elif message.content.lower().startswith('night'):
        await client.send_message(message.channel, "Goodnight!")
    elif message.content.lower().startswith('ryan pls'):
        await client.send_message(message.channel, "Yeah shut the fuck up Ryan")
    elif message.content.lower().startswith('!bo4'): #COUNTDOWN TO BLACK OPS 4
        dt  = datetime.datetime
        now = dt.now()
        day = 11 - now.day
        hour = 23 - now.hour
        minute = 59 - now.minute
        second = 59 - now.second
        await client.send_message(message.channel, f'{day} days {hour} hours {minute} minutes and {second} seconds btw') ##
    elif message.content.lower().startswith('rip'):
         await client.send_message(message.channel, "Dicks are so cute omg (⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ when you hold one in your hand and it starts twitching its like its nuzzling you(/ω＼) or when they perk up and look at you like owo nya? :3c hehe ~ penis-kun is happy to see me!!（＾ワ＾）and the most adorable thing ever is when sperm-sama comes out but theyre rlly shy so u have to work hard!! but when penis-kun and sperm-sama meet and theyre blushing and all like uwaaa~! (ﾉ´ヮ´)ﾉ: ･ﾟhehehe~penis-kun is so adorable (●´Д｀●)・::・")


#Bot token goes here
client.run(Token.token) #Opens Token.py and draws the token variable "client.run(file name, variable in file)"
