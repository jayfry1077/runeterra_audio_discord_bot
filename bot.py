# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
import heimerdinger


JSON_PATH = './set1-en_us.json'
TEXT_PATH = './examples/card_text/'
WAV_PATH = './examples/wav/'
OGG_PATH = './examples/ogg/'
RUNETERRA_AUDIO_FILES = './examples/runeterra_audio/'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.split(" ")[0] == '!convert' and message.content.split(" ")[1] != 'help':
        DECK_CODE = message.content.split(" ")[1]
        
        if len(message.content.split(" ")) > 2:
            DECK_NAME = message.content.split(" ")[2]
        else:
            DECK_NAME = DECK_CODE


        response = heimerdinger.deck_code_to_audio(DECK_CODE, DECK_NAME, WAV_PATH, RUNETERRA_AUDIO_FILES, 2)
        await message.channel.send(file=discord.File(response, '{}.mp3'.format(DECK_NAME)))
    
    if message.content.startswith('!convert help'):
        await message.channel.send('To use this bot type !convert DECK_CODE OUTPUT_NAME')


client.run(TOKEN, bot=True)