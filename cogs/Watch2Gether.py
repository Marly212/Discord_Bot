from fake_useragent import UserAgent
import discord
from discord.ext import commands
import requests

class Watch2Gether(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def wg(self, ctx):
        if ctx.channel.id == 709111247362064394 or ctx.channel.id == 711164822859022408:
            try:
                streamkey = ""

                ua = UserAgent()

                parameter = {'share': 1, 'api_key': 'ujww212vghgcc2bwef4d'}

                r = requests.post("https://w2g.tv/rooms/create.json",data=parameter)

                json = r.json()

                for key, value in json.items():
                    if key == "streamkey":
                        streamkey = value
                        await ctx.channel.send("https://w2g.tv/rooms/"+streamkey)

                    else:
                        continue 

            except Exception as e:
                print(e)
        else:
            await ctx.channel.send('Bitte den richtigen Channel benutzen')


def setup(bot):
    bot.add_cog(Watch2Gether(bot))



   
    