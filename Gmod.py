import discord
import subprocess
import os


async def startTTT(ctx):

    try:

        os.chdir('P:\\Server\\TTT')

        subprocess.call([r'P:\\Server\\TTT\\startServer.bat'])

        os.chdir('P:\\Programming\\Python\\Projekte')

    except Exception as e:
        print(e)


