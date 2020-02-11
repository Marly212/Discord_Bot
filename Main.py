import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class MyClient(discord.Client):
    async def on_ready(self):
        print("Iam Ready")

    async def on_message(self, message):
        if message.author == self.user:
            return

        print("Nachricht von " + str(message.author) + "die enthält " + str(message.content))


client = MyClient()
client.run("Njc0OTI3OTE1NDg1NjI2Mzc4.XjwhZA.HJ9ZZb4FxGalFOWzFjxBDHtDn8c")