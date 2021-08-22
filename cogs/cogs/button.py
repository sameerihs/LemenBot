  
import discord, datetime, time
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType


class button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def button(self,ctx):
        await ctx.send("Hello!",components = [Button(style= ButtonStyle.blue,label = "Button!")])
        interaction = await self.bot.wait_for("button_click", check = lambda i: i.component.label.startswith("Button"))
        await interaction.respond(content = "Playing...")
        

def setup(client):
    client.add_cog(button(client))