import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#Startup Log
@client.event
async def on_ready():
    print(f"{client.user.name} is online and running")
    print('------')
    print("Error Log:")
    #Set the 'playing' status as the set string
    await client.change_presence(game=discord.Game(name='Doki Doki Literature Club'))

#Client event
@client.event
async def on_message(message):
    if message.content.lower().startswith('!alive?'):#The message is transformed into lowercase characters
         await client.send_message(message.channel, "Yes, im alive")

#Bot token goes here
client.run('')
