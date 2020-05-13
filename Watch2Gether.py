from fake_useragent import UserAgent
import discord
import requests

async def newRoom(ctx):

    try:

        streamkey = ""

        ua = UserAgent()

        parameter = {'share': 1, 'api_key': 'ujww212vghgcc2bwef4d'}

        r = requests.post("https://www.watch2gether.com/rooms/create.json",data=parameter)

        json = r.json()

        for key, value in json.items():
            if key == "streamkey":
                streamkey = value
                await ctx.send("https://www.watch2gether.com/rooms/"+streamkey)

            else:
                continue

        

    except Exception as e:
        print(e)

   
    