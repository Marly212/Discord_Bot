import discord
import logging
from discord.ext import commands
from discord.utils import get
import os
import Musik


logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

command_prefix = '.'
bot = commands.Bot(command_prefix=command_prefix)
Token = 'Njc0OTI3OTE1NDg1NjI2Mzc4.XkpqFQ.TkwSGm7HSqNeo8oYYVp3TKVNWhk'


@bot.event
async def on_ready():
    print("Iam Ready")


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


@bot.command(pass_context=True)
async def leave(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Ich bin in keinem Channel")


@bot.command(pass_context=True)
async def play(ctx, url: str):
    await Musik.play(ctx, url, bot)


@bot.command(pass_context=True)
async def pause(ctx):
    await Musik.pause(ctx, bot)


@bot.command(pass_context=True)
async def resume(ctx):
    await Musik.resume(ctx, bot)


@bot.command(pass_context=True)
async def stop(ctx):
    await Musik.stop(ctx, bot)

bot.run(Token)