import discord
from discord.ext import commands
import asyncio
from pprint import pprint
import rule34
import random
import os
from dotenv import load_dotenv

#region variblen
bot = commands.Bot(command_prefix='.')
loop = bot.loop
r34 = rule34.Rule34(loop)
COGS = ['cogs.Watch2Gether']
load_dotenv()

#Cogs laden
for cog in COGS:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f'Could not load Cog {cog}: {str(e)}')

#endregion
autorole = {
    705509565881647114:{'memberroles': [742061678413348895], 'botroles': [705509886745641102]}
}

async def getRandomNumber(start, end):
    r = random.randint(start, end)
    return r

async def rule34DataEmbed(postData):
    tags = postData.get('@tags').replace(' ', ',')
    if postData.get('@source') == '':
        source = 'Keine Source angegeben'
    else:
        source = postData.get('@source')
    
    embed = discord.Embed(title='Postinformation', 
                        description='Folgende Informationen gibt es zu dem Post: ')
    embed.set_image(url=postData.get('@preview_url'))
    
    embed.add_field(name='Score',
                    value=postData.get('@score'))
    
    embed.add_field(name='Creator',
                    value=postData.get('@creator_id'))
    
    embed.add_field(name='Source',
                    value=source)

    embed.add_field(name='Tags',
                    value=tags)
    return embed

async def routine():
    while True:
        await bot.change_presence(activity=discord.Game('mit den Kindern'), status=discord.Status.online)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game('VR Hentai'), status=discord.Status.online)
        await asyncio.sleep(10)

def is_not_pinned(mess):
    return not mess.pinned

#Einloggen
@bot.event
async def on_ready():
    print("Ready")
    bot.loop.create_task(routine())

@bot.event
async def on_member_join(member):
    guild : Guild = member.guild
    if not member.bot:
        channel = bot.get_channel(705509565881647117)
        embed = discord.Embed(title='Willkommen auf dem Server, warum bist du hier?',
                                description='{} kannst du bitte wieder gehen? Keiner will dich hier'.format(member.mention),color=discord.Color.purple)
        await channel.send(embed=embed)
        autoguild = autorole.get(guild.id)
        if autoguild and autoguild['memberroles']:
            for roleId in autoguild['memberroles']:
                role = guild.getrole(roleId)
                if roleId:
                    await member.add_roles(role, reason='Autoroles', atomic=True)
    else:
        autoguild = autorole.get(guild.id)
        if autoguild and autoguild['botroles']:
            for roleId in autoguild['botroles']:
                role = guild.getrole(roleId)
                if roleId:
                    await member.add_roles(role, reason='Autoroles', atomic=True)

@bot.command()
async def yuumi(ctx):
    await  ctx.channel.send("Hat sich gedacht komm erstmal yummi im clash auspacken weil richtig auf hurensohn \n"+
        "basis erstmal richtig rein pimpern, kommplett balanced der champ, 200 years btw, \n"+
        "wie wars mal mit löschen von dem champ, oder nerfen, z.B. machen das der kek auf dem \n"
        "yummi sitzt nicht nicht von kha isoliert ist wie eine kleine pussy im arsch seines teammates"
        "sitzt und nur  eine Taste braucht um das ganze game zu carrien: \n"+"\n"+
                                                                                        \
        "Aber jz mal for real warum existiert ein champ wie yummi der keinerlei skill \n"+
        "anforderungen hat und nichts machen muss außer eine Taste drücken um das game \n"
        "carrien zu können solang sie auch nur einen kompetenten teammate hat, for real \n"
        "mate 200 Jahre nur koks genommen oder was...",tts=True)

@bot.command()    
async def send(ctx, *, args):
    if ctx.channel.id == 711164822859022408 or ctx.channel.id == 705521599880626217:
        data = await r34.getImages(tags=args, randomPID=True)
        r = await getRandomNumber(0, len(data)-1) 
        await ctx.channel.send(data[r].file_url)
        await ctx.channel.send('Id: {}'.format(data[r].id))
        postData = await r34.getPostData(data[r].id)
        infoPanel = await rule34DataEmbed(postData)
        await ctx.channel.send(embed=infoPanel)

@send.error
async def send_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Bitte Tags mitgeben')
    if isinstance(error, commands.CommandInvokeError):
        await ctx.channel.send('Kein Bilder zu den Tags gefunden')
        
@bot.command()
async def userinfo(ctx, member: discord.Member):
    if member:
        embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                description='Dies ist eine UserInfo für den User {}'.format(member.mention),
                                color=0x22a7f0)
        embed.add_field(name='Server beigetreten ',value=member.joined_at.strftime('%d/%m/%Y, %H:%m:%S'),
                        inline=True)

        embed.add_field(name='Discord beigetreten ',value=member.created_at.strftime('%d/%m/%Y, %H:%m:%S'),
                        inline=True)

        embed.set_footer(text='Domi ist still kinda Gay NGL')

        await ctx.channel.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('User konnte nicht gefunden werden')

@bot.command()      
async def clear(ctx, arg):
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        if ctx.author.id == 261844254563762197:#Meine Eigene User_ID
            if arg.isdigit():
                count = int(arg)+1
                deleted = await ctx.channel.purge(limit=count,check=is_not_pinned)
                await ctx.channel.send('{} Nachrichten gelöscht'.format(len(deleted)-1),delete_after=5)

@clear.error
async def send_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Bitte Zahl mitgeben')

# @bot.command(pass_context=True)
# async def wg(ctx):
#     if ctx.channel.id == 709111247362064394:
#         streamkey = await newRoom()
#         await ctx.channel.send("https://w2g.tv/rooms/"+streamkey)
#     else:
#         ctx.channel.send('Bitte den richtigen Channel benutzen')

@bot.command()
async def bravery(ctx, arg):
    pass
    #await BronzeBravery(message)

@bot.command()
async def check(ctx, arg):
    pass
    #await vcheck(arg)

@bot.command()
async def test(ctx):
    await ctx.channel.send("123456789abcdefghijklmopqrstuvwxyz",tts=True)



bot.run(os.getenv('TOKEN'))




#Bronze Bravery build nur lol