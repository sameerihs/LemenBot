import asyncio
import functools
import itertools
import math
import random
import asyncpg
import ast
from collections import deque
import youtube_dl
from async_timeout import timeout
import discord
import os
import discord.utils
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from gtts import gTTS
from tempfile import TemporaryFile
from discord.utils import get
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component
import pygsheets
from dpymenus import Page, TextMenu
from dpymenus.constants import CONFIRM
from dislash import SlashClient, SelectMenu, SelectOption

bot = commands.Bot(command_prefix='.',intents = discord.Intents.all())
Token='NzY2MzY0MTg0ODA3NDczMTkz.X4iSRA.N5SBTq7Esbd0wsD4ex5BHV1mGs0'
bot.remove_command('help')
ddb=DiscordComponents(bot)
slash = SlashClient(bot)


#COG LOADING 
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

@bot.command(aliases=['r'])
@commands.is_owner()
async def reload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	bot.load_extension(f'cogs.{extension}')
	await ctx.send("Reloading done")

@bot.command(aliases=['reloadall'])
@commands.is_owner()
async def rall(ctx):
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			bot.unload_extension(f'cogs.{filename[:-3]}')
			bot.load_extension(f'cogs.{filename[:-3]}')
	await ctx.send("``Reloaded all cogs``")


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')





print("code work bruh")


@bot.command()
@commands.is_owner()
async def die(ctx):
    game = discord.Game("")
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    bot.active = False
    await ctx.send("Logging off, please wait...")
    #await ctx.bot.logout()
    await ctx.bot.close()
    print("Bot offline") 

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))


@bot.event
async def on_message_error(ctx, error):
    if isinstance(error,commands.errors.CommandNotFound):
        await ctx.send("``There's no such command.``")



#BOT STATUS

@bot.command(aliases=['idle'])
@commands.is_owner()
async def sleep(self):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="no one"))
       
@bot.command(aliases=['online'])
@commands.is_owner()
async def awake(self):
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))

@bot.command(aliases=['donotdisturb','dontdisturb'])
@commands.is_owner()
async def dnd(self):
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="flyinLemon"))

@bot.command(aliases=['offline'])
@commands.is_owner()
async def invisible(self):
    await bot.change_presence(status=discord.Status.invisible)



@bot.command()
@has_permissions(administrator=True)
async def clear(ctx,limit):
    a=str(limit)
    if limit.isdigit():
        await ctx.channel.purge(limit=int(limit))
        await ctx.send("Deleted {} messages.".format(a),delete_after=1)
    else:
        await ctx.send("command usage: ``.clear < no. of messages to be deleted >``")



 


bot.run("NzY2MzY0MTg0ODA3NDczMTkz.X4iSRA.N5SBTq7Esbd0wsD4ex5BHV1mGs0")

gae=input()