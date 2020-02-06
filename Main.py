import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Iam Ready")

    async def on_message(self, message):
        if message.author == self.user:
            return

        print("Nachricht von " + str(message.author) + "die enthält " + str(message.content))


client = MyClient()
client.run("Njc0OTI3OTE1NDg1NjI2Mzc4.XjwhZA.HJ9ZZb4FxGalFOWzFjxBDHtDn8c")