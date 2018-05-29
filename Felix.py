import discord
from discord.ext.commands import bot
from discord.ext import commands
import Token #imports Token.py which holds the bot token
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

felixPics = [0, 1]
felixPics[0] = "https://myanimelist.cdn-dena.com/images/characters/5/353573.jpg"
felixPics[1] = "https://www.dailydot.com/wp-content/uploads/228/6f/ab64a69d4cd848bad23ed0f9190a91eb.jpg"

#Startup Log
@client.event
async def on_ready():
    print(f"{client.user.name} is online and running")
    print('------')
    print("Log:\n")
    #Set the 'playing' status as the set string
    await client.change_presence(game=discord.Game(name='!commands | !github',  type = 1, url = 'https://www.twitch.tv/thelittledude_ld'))

@client.event
async def on_message(message):
    if message.content.lower().startswith('!commands'):
        print("!commands command called")
        await client.send_message(message.channel, "```\nHere are all the commands:\n\n*Not available\n\n!github - Link to the github of Felix Bot\n!alive? - Checking for my pulse I see...\n!gay - Use at your own risk... \n*!image 'search' - Searches Google images```")
    elif message.content.lower().startswith('!github'):
        print("!github command called")
        await client.send_message(message.channel, "https://github.com/Jmaonri/Felix")
    elif message.content.lower().startswith('!alive?'):#The message is transformed into lowercase characters
        print("!alive? command called")
        await client.send_message(message.channel, "Yes, im alive")
    elif message.content.lower().startswith('!nut'):
        print("!nut command called")
        await client.send_message(message.channel, "https://www.dailydot.com/wp-content/uploads/228/6f/ab64a69d4cd848bad23ed0f9190a91eb.jpg")
    elif message.content.lower().startswith('!gay'):
        #AFTER ONE FUCKING HOUR THIS FINALLY WORKS, DONT TOUCH THIS SHIT EVER AGAIN (nvm I broke my rule but I made it better)
        print("!gay command called")
        embed = discord.Embed(title = "No u faggot")
        embed.set_image(url = felixPics[0])
        await client.send_message(message.author, embed = embed)

#Bot token goes here
client.run(Token.token) #Opens Token.py and draws the token variable "client.run(file name, variable in file)"
