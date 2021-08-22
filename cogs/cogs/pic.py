import discord, datetime, time
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

class picworld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    	

    @commands.command(aliases=['notes'])
    async def note(self,ctx: commands.Context, *, ab: str):
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylim([-80, 10])
        data = np.ones(100)
        data[100:] -= np.arange(0)
        ax.plot(data)
        ax.set_xlabel(' ')
        ax.set_ylabel(' ')
        fig.text(0.5, 0.85,'Notes',ha='center')
        



        plt.savefig("notes.png")
        base1 = Image.open(r"C:\SAMEER MAIN\Sameer\Code\Lemen Bot\LemenBot\notes.png").convert("RGBA")
        txt1 = Image.new("RGBA", base1.size, (255,255,255,0))
        fnt1 = ImageFont.truetype(r"C:\Windows\Fonts\inkfree.ttf", 25)

        if len(ab.split())<8:
            fullnote=str(ab)
            d1 = ImageDraw.Draw(txt1)
            d1.text((70,100),fullnote, font=fnt1, fill='black')
            out1 = Image.alpha_composite(base1, txt1)
            out1.save('notessss.png')
            await ctx.author.send(file=discord.File('notessss.png'))
            plt.clf()
            

        '''else:
            for aaa in ab.split()[0:7]:
                msga=aaa+" "
            fullnote=str(msga)
            for bbb in ab.split()[7:14]:
                msgb=bbb+" "
            fullnote2=str(msgb)
            d1 = ImageDraw.Draw(txt1)
            d2 = ImageDraw.Draw(txt1)
            d1.text((70,100),fullnote, font=fnt1, fill='black')
            d2.text((70,120),fullnote2, font=fnt1, fill='black')

            out1 = Image.alpha_composite(base1, txt1)
            out1.save('notessss.png')
            await ctx.author.send(file=discord.File('notessss.png'))
            plt.clf()'''

        '''elif 21<len(ab)<42:
    		d1 = ImageDraw.Draw(txt1)
    		d2 = ImageDraw.Draw(txt1)
    		full1=str("-"+str(ab.split()[0:20]))
    		full2=str(ab.split()[20:40])
    		d1.text((70,100),full1, font=fnt1, fill='black')
    		d2.text((70,120),full2, font=fnt1, fill='black')

    		out2 = Image.alpha_composite(base1, txt1)
    		out2.save('notessss.png')
    		await ctx.author.send(file=discord.File('notessss.png'))
    		plt.clf()'''

	


def setup(client):
    client.add_cog(picworld(client))
