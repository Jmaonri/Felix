import discord
from discord.ext.commands import bot
from discord.ext import commands
import Token #imports Token.py which holds the bot token
import asyncio
import time

#Declare variables
sendMessage = BotClient.send_message()
messageStarts = message.content.lower().startswith()
githubLink = "https://github.com/Jmaonri/Felix"
twitchLink = 'https://www.twitch.tv/thelittledude_ld'
Streaming = 1
Client = discord.Client()
botClient = commands.Bot(command_prefix = "!")
sendCommands = "```\nHere are all the commands:\n\n!github - Link to the github of Felix Bot\n!alive? - Checking for my pulse I see...\n!gay - Use at your own risk... \n!nut - Pretty self explanatory```"

imageList = [0, 1]
imageList[0] = "https://myanimelist.cdn-dena.com/images/characters/5/353573.jpg" #despacito
imageList[1] = "https://www.dailydot.com/wp-content/uploads/228/6f/ab64a69d4cd848bad23ed0f9190a91eb.jpg"

#Startup Log
@client.event
async def on_ready():
    print(f"{botClient.user.name} is online and running")
    print('------')
    print("Log:\n")
    #Set the 'playing' status as the set string
    await botClient.change_presence(game=discord.Game(name='!commands | !github',  type = Streaming, url = twitchLink))

@client.event
async def on_message(message):
    if messageStarts('!commands'):
        print("!commands command called")
        await sendMessage(message.channel, sendCommands)
    elif messageStarts('!github'):
        print("!github command called")
        await sendMessage(message.channel, githubLink)
    elif messageStarts('!alive?'):#The message is transformed into lowercase characters
        print("!alive? command called")
        await sendMessage(message.channel, "Yes, im alive")
    elif messageStarts('!nut'):
        print("!nut command called")
        await sendMessage(message.channel, "https://www.dailydot.com/wp-content/uploads/228/6f/ab64a69d4cd848bad23ed0f9190a91eb.jpg")
    elif messageStarts('!gay'):
        #AFTER ONE FUCKING HOUR THIS FINALLY WORKS, DONT TOUCH THIS SHIT EVER AGAIN (nvm I broke my rule but I made it better)
        print("!gay command called")
        embed.set_image(url = imageList[0])
        await sendMessage(message.author, discord.Embed(title = "No u faggot"))

#Bot token goes here
botClient.run(Token.token) #Opens Token.py and draws the token variable "botClient.run(file name, variable in file)"
