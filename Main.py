import discord
import logging
import youtube_dl
from discord.ext import commands
from discord.utils import get
import os

logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

command_prefix = '.'
bot = commands.Bot(command_prefix=command_prefix)
Token = 'Njc0OTI3OTE1NDg1NjI2Mzc4.XkJ8fw.vwqz9XkeogSEwcTBmXPrRNbMLY0'


@bot.event
async def on_ready():
    print("Iam Ready")


@bot.commands(pass_context=True)
async def join(ctx):
    voice = get(bot.voice_clients)
    channel = ctx.message.author.voice.channel

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

bot.run(Token)