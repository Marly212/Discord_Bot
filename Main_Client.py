import discord
import asyncio
from pprint import pprint
#from Rule34 import send34
from Watch2Gether import newRoom
from BronzeBravery import BronzeBravery
from VirusTotal import vcheck

client = discord.Client()

autorole = {
    705509565881647114:{'memberroles': [742061678413348895], 'botroles': [705509886745641102]}
}

async def routine():
    while True:
        await client.change_presence(activity=discord.Game('mit den Kindern'), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('VR Hentai'), status=discord.Status.online)
        await asyncio.sleep(10)

def is_not_pinned(mess):
    return not mess.pinned

#Einloggen
@client.event
async def on_ready():
    print("Ready")
    client.loop.create_task(routine())

@client.event
async def on_member_join(member):
    guild : Guild = member.guild
    if not member.bot:
        channel = client.get_channel(705509565881647117)
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


@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return

    if ctx.content.startswith('.yummi'):
        await  ctx.channel.send("Hat sich gedacht komm erstmal yummi im clash auspacken weil richtig auf hurensohn \n"+
            "basis erstmal richtig rein pimpern, kommplett balanced der champ, 200 years btw, \n"+
            "wie wars mal mit löschen von dem champ, oder nerfen, z.B. machen das der kek auf dem \n"
            "yummi sitzt nicht nicht von kha isoliert ist wie eine kleine pussy im arsch seines teammates"
            "sitzt und nur  eine Taste braucht um das ganze game zu carrien: \n"+"\n"+
                                                                                            \
            "Aber jz mal for real warum existiert ein champ wie yummi der keinerlei skill \n"+
            "anforderungen hat und nichts machen muss außer eine Taste drücken um das game \n"
            "carrien zu können solang sie auch nur einen kompetenten teammate hat, for real \n"
            "mate 200 Jahre nur koks genommen oder was...")

    #if '.send' in ctx.content:
        #await send34(message, message.channel.id)

    if ctx.content.startswith('.userinfo'):
        args = ctx.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, ctx.guild.members)
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
                
    if ctx.content.startswith('.clear'):
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            if ctx.author.id == '261844254563762197':#Meine Eigene User_ID
                args = ctx.content.split(' ')
                if len(args) == 2:
                    if args[1].isdigit():
                        count = int(args[1])+1
                        deleted = await ctx.channel.purge(limit=count,check=is_not_pinned)
                        await ctx.channel.send('{} Nachrichten gelöscht'.format(len(deleted)-1))


    # if ctx.content.startswith('.wg'):
    #     await newRoom(message, message.channel.id)

    # if '.bravery' in ctx.content:
    #     await BronzeBravery(message)

    # if '.check' in ctx.content:
    #     await vcheck(message)




client.run("Njc0OTI3OTE1NDg1NjI2Mzc4.Xjvtmg.lwg5G238UncUMFJahN2Z_EHYcnU")




#Bronze Bravery build nur lol