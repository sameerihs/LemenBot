import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random


class Chat(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


#Commands
	@commands.command(aliases=['hii',"hello","Hi","Hello",'hi','Hii',"Hey","Heyy","heyy"])
	async def hey(self,ctx):
		async with ctx.typing():
			await ctx.send("Hey there!")


	@commands.command()
	async def logo(self,ctx):
		await ctx.send('''``` _      ________  ___ _____ _   _ 
| |    |  ___|  \/  ||  ___| \ | |
| |    | |__ | .  . || |__ |  \| |
| |    |  __|| |\/| ||  __|| . ` |
| |____| |___| |  | || |___| |\  |
\_____/\____/\_|  |_/\____/\_| \_/
                                  ```''')



	@commands.Cog.listener()
	async def on_message(self, message):
		weird = [                                                                                                                                                               'fuck','Fuck','punda','otha','shit','mf','ffs','FFS']
		

		messageContent = message.content
		if len(messageContent) > 0:
			for word in weird:
				if word in messageContent:
					await message.add_reaction(emoji="⛔")
					
			print(message.author,"said",message.content)


	
			
			
	
def setup(client):
	client.add_cog(Chat(client))





