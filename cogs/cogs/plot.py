  
import discord, datetime, time
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox

class Plot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['g','G'])
    async def graph(self, ctx, a,b,c):
    	fig, ax = plt.subplots()
    	ax.set(xlim=(0, 10), ylim=(0, 5))
    	plt.plot([a,b,c])
    	plt.ylabel('some numbers')
    	plt.savefig('graph.png')
    	await ctx.send(file=discord.File('graph.png'))
    	 


    @commands.command(aliases=['fungraph','FG','Fg'])
    async def fg(self, ctx: commands.Context, *, a: str):
    	with plt.xkcd():
    		fig = plt.figure()
    		ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    		ax.spines['right'].set_color('none')
    		ax.spines['top'].set_color('none')
    		ax.set_xticks([])
    		ax.set_yticks([])
    		ax.set_ylim([-30, 10])
		
    		data = np.ones(100)
    		data[70:] -= np.arange(30)
		
    		ax.annotate(a,
    		    xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))
		
    		ax.plot(data)
		
    		ax.set_xlabel('time')
    		ax.set_ylabel('peace of mind')
    		fig.text(
    		    0.5, 0.05,
    		    'Just Lemen things bruh',
    		    ha='center')
    	plt.savefig('ffg.png')
    	await ctx.send(file=discord.File('ffg.png'))
    	plt.clf()



def setup(client):
    client.add_cog(Plot(client))