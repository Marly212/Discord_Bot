import rule34
import discord
import random
import nest_asyncio
import asyncio


nest_asyncio.apply()

loop = asyncio.get_event_loop()

rule = rule34.Rule34(loop)


async def send34(message, channel):

    if channel == 705521599880626217:
        try:
            tags = message.clean_content
            tags = tags.split(" ")[1]
            ruel34Image = loop.run_until_complete(rule.getImages(tags))

            try:

                randomNumber = random.randint(0, len(ruel34Image)-1)

            except Exception as e:
                await message.channel.send("Kein Bild zum Tag gefunden \n"+"Nachricht: "+tags+"\nAuthor: "+message.author.display_name)
                return

            await message.channel.send(ruel34Image[randomNumber].file_url)

            await message.channel.send(len(ruel34Image))

        except Exception as e:
            print(str(e))
            await message.channel.send("Kein Bild zum Tag gefunden \n"+"Nachricht: "+tags+"\nAuthor: "+message.author.display_name)

