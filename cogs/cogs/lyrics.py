                
import discord, datetime, time
from discord.ext import commands
import lyricsgenius

genius = lyricsgenius.Genius("GENIUS KEY")


class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        er=str(error)
        if "AttributeError" in er:
            await ctx.send("``There seems to be an error.``")
            print(error)
        else:
            await ctx.send('An error occurred: {}'.format(str(error)))
    

    @commands.command(pass_context=True,aliases=['l','L','lyric','Lyric','Lyrics'])
    async def lyrics(self, ctx: commands.Context, *, name: str):
        async with ctx.typing():
            await ctx.send("Hold up, Lemme search....")
        artist = " "
        song = genius.search_song(name, artist)
        sl=song.lyrics
        if len(str(sl))< 1000:
            embedl = discord.Embed(title="``🟡Lyrics``", color=0xc8dc6c)
            embedl.set_author(name="lemen")
            embedl.add_field(name="•", value=sl)
            async with ctx.typing():
                await ctx.send(embed=embedl)


        elif 2000>len(str(sl))> 1000:
            sl1=sl[0:600]
            sl2=sl[600:1200]
            sl3=sl[1200:2000]
            embedll = discord.Embed(title="``🟡Lyrics``", color=0xc8dc6c)
            embedll.set_author(name="lemen")
            embedll.add_field(name="-----------------------------", value=sl1)
            embedll.add_field(name="-----------------------------", value=sl2)
            embedll.add_field(name="-----------------------------", value=sl3)
            async with ctx.typing():
                await ctx.send(embed=embedll)


        elif len(str(sl))> 2000:
            sl1=sl[0:1000]
            sl2=sl[1000:2000]
            sl3=sl[2000:3000]
            embedll = discord.Embed(title="``🟡Lyrics``", color=0xc8dc6c)
            embedll.set_author(name="lemen")
            embedll.add_field(name="-----------------------------", value=sl1)
            embedll.add_field(name="-----------------------------", value=sl2)
            embedll.add_field(name="-----------------------------", value=sl3)
            async with ctx.typing():
                await ctx.send(embed=embedll)
        

def setup(client):
    client.add_cog(Lyrics(client))

 
