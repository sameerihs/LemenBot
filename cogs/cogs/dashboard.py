from discord import Embed
import discord, datetime, time
from discord.ext import commands


  


class dashBoard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    '''@commands.command()
    async def dashboard(self,ctx):
    	async with ctx.typing():
    		first_embed = Embed(title='embed 1')
    		new_embed = Embed(title='embed 2')
    		msg = await ctx.send(embed=first_embed)
    		await msg.edit(embed=new_embed)'''
        

def setup(client):
    client.add_cog(dashBoard(client))