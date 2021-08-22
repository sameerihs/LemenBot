import discord, datetime, time
from discord.ext import commands
import aiml
import os

kernel=aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
kernel.respond("LOAD AIML B")

class ChatBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        m= str(message.content)   
        if m.startswith(">"):
            inp=str(m.strip(">"))
            response=kernel.respond(inp)
            mainresponse="``{}``".format(response)
            await message.channel.send(str(mainresponse))
        else:
            pass

def setup(client):
    client.add_cog(ChatBot(client))