  
import discord, datetime, time
from discord.ext import commands


class Announcement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    '''@commands.command()
    async def make(self,ctx):
    	def check(message):
    		return message.author == ctx.author and message.channel == ctx.channel
    	await ctx.send('Waiting for a title')
    	title = await self.bot.wait_for('message', check=check)
    	await ctx.send('Waiting for a description')
    	desc = await self.bot.wait_for('message', check=check)
    	embed = discord.Embed(title=title.content, description=desc.content, color=0x72d345)
    	await ctx.send(embed=embed)'''
   
    
    @commands.command(aliases=['Ann','ann','botann','announcement'])
    #@has_permissions(administrator=True)
    async def announce(self,ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        await ctx.send('Enter the title')
        title = await self.bot.wait_for('message', check=check)
        await ctx.send('Enter the announcement')
        desc = await self.bot.wait_for('message', check=check)
        embed87 = discord.Embed(title=title.content, description=desc.content, color=0xfff44f)
        embed87.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        try:
            await ctx.send('Enter the Channel Id.')
            id_1 = await self.bot.wait_for('message', check=check)
            channel = self.bot.get_channel(int(id_1.content))
            await channel.send(embed=embed87)
            await ctx.send("``The announcement has been made.``")
        except:
            await ctx.send(embed=embed87)
            await ctx.send("``The announcement has been made.``")




def setup(client):
    client.add_cog(Announcement(client))