import rule34
import discord
import random
import nest_asyncio
import asyncio

nest_asyncio.apply()

loop = asyncio.get_event_loop()

rule = rule34.Rule34(loop)


async def send34(ctx, tags, channel,):

    if channel == 705521599880626217:
        try:
            ruel34Image = loop.run_until_complete(rule.getImageURLS(tags,True,True,True))

            randomNumber = random.randint(0, len(ruel34Image)-1)

            await ctx.send(ruel34Image[randomNumber])

            await ctx.send(len(ruel34Image))

        except Exception as e:
            print(str(e))
            await ctx.send("Kein Bild zum Tag gefunden \n"+"Nachricht: "+tags+"\nAuthor: "+ctx.author.display_name)

