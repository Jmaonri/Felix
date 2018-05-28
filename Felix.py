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
    await client.change_presence(game=discord.Game(name='!commands | !github',  type = 1, url = 'https://www.twitch.tv/thelittledude_ld'))

@client.event
async def on_message(message):
    if message.content.lower().startswith('!commands'):
        await client.send_message(message.channel, "```\nHere are all the commands:\n\n*Not available\n\n!github - Link to the github of Felix Bot\n!alive? - Checking for my pulse I see...\n!gay - Use at your own risk... \n*!image 'search' - Searches Google images```")
    elif message.content.lower().startswith('!github'):
        await client.send_message(message.channel, "https://github.com/Jmaonri/Felix")
    elif message.content.lower().startswith('!alive?'):#The message is transformed into lowercase characters
        await client.send_message(message.channel, "Yes, im alive")
    elif message.content.lower().startswith('!gay'):
        #AFTER ONE FUCKING HOUR THIS FINALLY WORKS, DONT TOUCH THIS SHIT EVER AGAIN
        embed = discord.Embed()
        embed.set_image(url = "https://myanimelist.cdn-dena.com/images/characters/5/353573.jpg")
        await client.send_message(message.author, embed = embed)
        await client.send_message(message.author, "No u faggot")

#Bot token goes here
client.run('')
