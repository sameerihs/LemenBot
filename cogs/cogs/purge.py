import discord, datetime, time
from discord.ext import commands
import asyncio 


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def t(self, ctx):
    	a="Deleting in 3"
    	b="Deleting in 2"
    	c="Deleting in 1"
    	mmm= await ctx.send(a)
    	await asyncio.sleep(0.8)
    	await mmm.edit(content=b)
    	await asyncio.sleep(0.8)
    	await mmm.edit(content=c,delete_after=0.8) 
        
    @commands.command()
    async def tt(self, ctx):
    	counter=0
    	a="Numbers: {}".format(counter)
    	mmm= await ctx.send(a)
    	while True:
    		counter+=1
    		await asyncio.sleep(1)
    		await mmm.edit(content="Numbers: {}".format(counter))
    		

def setup(client):
    client.add_cog(Purge(client))

