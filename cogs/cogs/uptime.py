  
import discord, datetime, time
from discord.ext import commands
import asyncio

start_time = time.time()


class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,aliases=['ut'])
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=0xfff44f)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Note: Uptime updates every 5 mins")
        try:
            a= await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

        while True:
            current_timem = time.time()
            differencen = int(round(current_timem - start_time))
            textn = str(datetime.timedelta(seconds=differencen))
            newtime = str(textn)
            embedn = discord.Embed(colour=0xfff44f)
            embedn.add_field(name="Uptime", value=newtime)
            embedn.set_footer(text="Note: Uptime updates every 5 mins")
            await asyncio.sleep(300)
            await a.edit(embed=embedn)





def setup(client):
    client.add_cog(Uptime(client))

    