import discord
import logging
import youtube_dl
from discord.ext import commands
from discord.utils import get
import os
import asyncio

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)






logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

command_prefix = '.'
bot = commands.Bot(command_prefix=command_prefix)
Token = 'Njc0OTI3OTE1NDg1NjI2Mzc4.XkVAmA.0WOZ-upZbTKJomZyN0QmjYPBXqI'


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
    author = ctx.message.author
    channel = author.voice.channel

    vc = await channel.connect()
    player = await YTDLSource.from_url(url, loop=bot.loop)

    vc.play(discord.FFmpegPCMAudio(player.url))


@bot.command(pass_context=True)
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
        await ctx.send("Musik Paused")
    else:
        await ctx.send("Keine Musik am Spielen")


@bot.command(pass_context=True)
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        voice.resume()
        await ctx.send("Musik resumed")
    else:
        await ctx.send("Keine Musik am halten")


bot.run(Token)