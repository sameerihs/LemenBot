import discord, datetime, time
from discord.ext import commands
import webbrowser
from discord.ext.commands import has_permissions, MissingPermissions


class meet(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	'''@commands.command(pass_context=True)
	async def math(self, ctx):
		webbrowser.open("https://meet.google.com/bkg-rewp-hvp")
		await ctx.send("Joining Math class")'''


def setup(client):
	client.add_cog(meet(client))

	