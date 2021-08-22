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
		weird = [                                                                                                                         'fuck','Fuck','punda','otha','shit','mf','ffs','FFS']
		lemen_list = ['lemen','Lemen','LEMEN']
		lemon= ['lemon',"Lemon","LEMON"]
		g=["gey","gay"]

		messageContent = message.content
		if len(messageContent) > 0:
			for word in weird:
				if word in messageContent:
					await message.add_reaction(emoji="⛔")
					
			print(message.author,"said",message.content)


	@commands.command()
	async def chat(self,ctx):
		a=ctx.message.author
		await ctx.channel.send("Heyy, Let's chat")
		await ctx.channel.send("How are you?")
		
			
			
			#if ('good','fine','amaze','nice','cool','ok','well') in message.content:
			#	how = ('Hi', 'Hello', '안녕하세요 (Annyeonghaseyo)', '你好', 'こんにちは(Konnichiwa)', 'Bonjour')
			#	response = random.choice(how)
			#	await message.channel.send(response)
			#	pass
#
			#if ('bad','idiotic','shit','not','lame','fucked','weird') in message.content:
			#	how = ('Hi', 'Hello', '안녕하세요 (Annyeonghaseyo)', '你好', 'こんにちは(Konnichiwa)', 'Bonjour')
			#	response = random.choice(how)
			#	await message.channel.send(response)
			#	pass










def setup(client):
	client.add_cog(Chat(client))





