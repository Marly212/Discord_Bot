import discord
import unittest
from pprint import pprint
from Rule34 import send34
from Watch2Gether import newRoom
from BronzeBravery import BronzeBravery
from VirusTotal import vcheck

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ready")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith(".send"):
            await send34(message, message.channel.id)

        if message.content.startswith(".wg"):
            await newRoom(message, message.channel.id)

        if message.content.startswith(".yummi"):
        
            await  message.channel.send("Hat sich gedacht komm erstmal yummi im clash auspacken weil richtig auf hurensohn \n"+
                   "basis erstmal richtig rein pimpern, kommplett balanced der champ, 200 years btw, \n"+
                   "wie wars mal mit löschen von dem champ, oder nerfen, z.B. machen das der kek auf dem \n"
                   "yummi sitzt nicht nicht von kha isoliert ist wie eine kleine pussy im arsch seines teammates"
                   "sitzt und nur  eine Taste braucht um das ganze game zu carrien: \n"+"\n"+
                                                                                                    \
                    "Aber jz mal for real warum existiert ein champ wie yummi der keinerlei skill \n"+
                    "anforderungen hat und nichts machen muss außer eine Taste drücken um das game \n"
                    "carrien zu können solang sie auch nur einen kompetenten teammate hat, for real \n"
                    "mate 200 Jahre nur koks genommen oder was...")

        if message.content.startswith(".bravery"):
            await BronzeBravery(message)

        if message.content.startswith(".check"):
            await vcheck(message)


client = MyClient()
client.run("")




#Bronze Bravery build nur lol