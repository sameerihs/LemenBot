import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from gtts import gTTS


class mod(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	#Commands
	'''@commands.command()
	async def role(self, ctx):'''
		



	

def setup(client):
	client.add_cog(mod(client))
