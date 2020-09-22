import discord
import logging
from discord.ext import commands
from discord.utils import get
import os
import Musik
from Rule34 import send34
from LolHentai import sendlolHentai
from Watch2Gether import newRoom
from Gmod import startTTT



logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

command_prefix = '.'
bot = commands.Bot(command_prefix=command_prefix)
Token = 'Njc0OTI3OTE1NDg1NjI2Mzc4.XrvdeQ.rncBaAqlxCDF03U7DfaQD8UKdpU'

@bot.event
async def on_ready():
    print("Iam Ready")


@bot.command(pass_context=True)
async def join(ctx):
    channel_voice = ctx.message.author.voice.channel
    channel_text = ctx.message.channel.id
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel_voice)
    else:
        voice = await channel_voice.connect()


@bot.command(pass_context=True)
async def leave(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Ich bin in keinem Channel")


@bot.command(pass_context=True)
async def play(ctx, url: str):
    channel_voice = ctx.message.author.voice.channel
    channel_text = ctx.message.channel.id
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel_voice)
    else:
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


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def send(ctx, message):

    channel_text = ctx.message.channel.id

    if channel_text == 705521599880626217:
    
        try:
            await send34(ctx, message, channel_text)

        except Exception as e:
            print(str(e))

    elif channel_text == 708968847834873857:

        try:
            await sendlolHentai(ctx, message)

        except Exception as e:
            print(str(e))


@bot.command(pass_context=True)
async def wg(ctx):

    await newRoom(ctx)


@bot.command(pass_context=True)
async def yuumi(ctx):

    await ctx.send("Hat sich gedacht komm erstmal yummi im clash auspacken weil richtig auf hurensohn \n"+
                   "basis erstmal richtig rein pimpern, kommplett balanced der champ, 200 years btw, \n"+
                   "wie wars mal mit löschen von dem champ, oder nerfen, z.B. machen das der kek auf dem \n"
                   "yummi sitzt nicht nicht von kha isoliert ist wie eine kleine pussy im arsch seines teammates"
                   "sitzt und nur  eine Taste braucht um das ganze game zu carrien: \n"+"\n"+
                                                                                                    \
                    "Aber jz mal for real warum existiert ein champ wie yummi der keinerlei skill \n"+
                    "anforderungen hat und nichts machen muss außer eine Taste drücken um das game \n"
                    "carrien zu können solang sie auch nur einen kompetenten teammate hat, for real \n"
                    "mate 200 Jahre nur koks genommen oder was...")


@bot.command(pass_context=True)
async def gmod(ctx):
    channel_voice = ctx.message.author.voice.channel

    #await startTTT(ctx)




bot.run(Token)

