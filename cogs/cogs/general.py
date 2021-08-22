import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import pyfiglet

ascii_banner = pyfiglet.figlet_format("status : online")



class Initiate(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


#events
	@commands.Cog.listener()
	async def on_ready(self):
		print("Lemen is online")
		print(ascii_banner)
	

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel=member.guild.system_channel
		if channel is not None:
			await channel.send("Welcome {0.mention}.".format(member))


#Commands

	'''@commands.command()
	async def help(self,ctx):
		embedh = discord.Embed(title="Information and Commands", color=0xc8dc6c)
		embedh.set_author(name="lemen")
		embedh.add_field(name=f"Commands", value="**`.join`** (Joins a voice channel.)\n **`.leave`** (Clears the queue and leaves the voice channel)\n **`.play <song/video name>`** (Plays the song/audio in VC)\n **`.pause`** (Pauses the song)\n **`.resume`** (Resumes the song) \n **`.now`** (Displays the current playing song.)\n **`.help`** (Sends the commands for this bot)",
    		inline=False)
		await ctx.send(embed=embedh)'''


	@commands.command()
	async def help(self,ctx):
		embedh = discord.Embed(title="Information and Commands", color=0xfff44f)
		embedh.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
		embedh.add_field(name=f"**`.join`**", value="Joins a voice channel.",inline=True)
		embedh.add_field(name=f"**`.leave`**", value="Leaves the voice channel.",inline=True)
		embedh.add_field(name=f"**`.play <song/video url>`**", value="Plays the song in your VC.",inline=True)
		embedh.add_field(name=f"**`.say <message>`**", value="* The bot speaks the message in the VC. *",inline=True)
		embedh.add_field(name=f"**`.spotifyplay <spotify playlist url>`**", value="* Plays the Playlist. *",inline=True)
		embedh.add_field(name=f"**`.pause`**", value="Pauses the current playing song.",inline=True)
		embedh.add_field(name=f"**`.resume`**", value="Resumes the current playing song.",inline=True)
		embedh.add_field(name=f"**`.queue`**", value="Shows all the songs that are queued.",inline=True)
		embedh.add_field(name=f"**`.now`**", value="Displays the details of the current playing song.",inline=True)
		embedh.add_field(name=f"**`.remove <song number from queue>`**", value="Removes the song from the queue.",inline=True)
		embedh.add_field(name=f"**`.lyric <song name>`**", value="Displays the lyrics of the song.",inline=True)
		embedh.add_field(name=f"**`.volume <percentage>`**", value="Changes the volume of the player.",inline=True)
		embedh.add_field(name=f"**`.graph <val1 val2 val3>`**", value="Plots a graph",inline=True)
		embedh.add_field(name=f"**`.fg <thing/person that pisses you off>`**", value="Just try it.",inline=True)
		embedh.add_field(name=f"**`.note <message>`**", value="Your notes will be DM'd to you.",inline=True)
		embedh.add_field(name=f"**`.uptime`**", value="Displays the duration the bot has been online.",inline=True)
		embedh.add_field(name=f"**`.announce`**", value="Used to make announcements.",inline=True)
		embedh.add_field(name=f"**`.vcannounce <content>`**", value="Used to make announcements over Voice chats.",inline=True)
		embedh.add_field(name=f"**`.dance`**", value="* dances *",inline=True)
		embedh.add_field(name=f"**`> message`**", value="To begin Chat with Lemen",inline=True)
		embedh.add_field(name=f"**`.help`**", value="Sends this Help Bar ",inline=True)
		

		embeded = discord.Embed(title="Exclusive cmds", color=0xfff44f)
		embeded.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
		embeded.add_field(name=f"**`.offline`**", value="Bot sets its status to Offline",inline=True)
		embeded.add_field(name=f"**`.online`**", value="Bot sets its status to Online",inline=True)
		embeded.add_field(name=f"**`.sleep`**", value="Bot sets its status to Idle",inline=True)		
		embeded.add_field(name=f"**`.rall`**", value="Reloads all cogs",inline=True)
		embeded.add_field(name=f"**`.upload <file path>`**", value="Uploads attachments from the folder",inline=True)
		embeded.add_field(name=f"**`.save`**", value="Saves all the attachments from the channel to a folder.",inline=True)
		embeded.add_field(name=f"**`.die`**", value="Kills me",inline=True)

		
		if str(ctx.author)=="Your discord name":
			await ctx.send(embed=embedh)
			await ctx.send(embed=embeded)
		else:
			await ctx.send(embed=embedh)


def setup(client):
	client.add_cog(Initiate(client))







