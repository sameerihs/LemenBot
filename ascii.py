  
import discord, datetime, time
from discord.ext import commands
import pyfiglet


class ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ascii(self,ctx: commands.Context,*,main):
        try:
            ascii_banner = pyfiglet.figlet_format(main)
            sender="``"+ascii_banner+"``"
            await ctx.send(sender)
        except:
            await ctx.send("Must be 2000 or fewer in length")


def setup(client):
    client.add_cog(ascii(client))