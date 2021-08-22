import discord, datetime, time
from discord.ext import commands
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import itertools
import asyncio
import discord.utils
from discord.ext import tasks

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Google API") #name of sheet file
sheet_instance = sheet.get_worksheet(0) # 0 refers to the first worksheet

onemic=['8']


# REMEMBER: MAKE SURE THE BOT IS IN HIGHER HEIRARCHY IN THE ROLES

class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


   # '''@commands.Cog.listener()
   # async def on_member_join(self, member):
   # 		
   # 	for i in range(1,25):
   # 		disc = sheet_instance.col_values(i)
   # 		for j in disc:
   # 			if str(j)==str(member):
   # 				
#
   # 				if str(i) in onemic:
   # 					try:
   # 						user = member
   # 						role = "one mic"
   # 						await user.add_roles(discord.utils.get(user.guild.roles, name=role))
   # 					except:
   #                         pass
   # 	channel = self.bot.get_channel(int(841058131194281994))
   # 	if channel is not None:
   # 		await channel.send("Welcome to One Mic Stand, {0.mention}".format(member))'''




    @commands.command()
    async def data(self, ctx):
        #a={}
        column1=11
        column2=12
        name=sheet_instance.col_values(int(column1))
        disc=sheet_instance.col_values(int(column2))
        for i in range (len(name)):
            await asyncio.sleep(1)
            #a[str(name[i])] = str(disc[i])
            if str(name[i])=="":
                pass
            elif str(disc[i])=="":
                pass
            else:
                await ctx.send("{} : {}".format(str(name[i]),str(disc[i])))



def setup(client):
    client.add_cog(Google(client))



