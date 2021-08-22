import discord, datetime, time
from discord.ext import commands
import os
import shutil


#NOTE: By usual, the filename given will save images/videos inside the folder inside another folder called "8mb+" on desktop
# If you wanna change that, make changes to only "copier" variable

class imageMOD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def save(self,ctx: commands.Context):
        def check(message: discord.Message):
            return message.author == ctx.author and message.channel == ctx.channel
        await ctx.send('``Name the folder name to create and save the attachments.``')
        loci = await self.bot.wait_for('message', check=check)
        locci=loci.content+"\\"
        mypath = "C:\\Users\\Admin\\Desktop\\"+loci.content
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        await ctx.send("Saving all attachments...")


        messages = await ctx.history(limit=10000).flatten()
        for i in messages:
            if len(i.attachments)==0:
                continue
            else:
                main=str(i.attachments[0].filename)
                #await ctx.send(main)
            
                try:
                    for j in i.attachments:
                        place="C:\\Users\\Admin\\Desktop\\"+locci+str(main)
                        await j.save(place)
                                               
                except:
                    err="Could not save the file named: "+str(main)
                    await ctx.send(err)
                    await ctx.send(i.attachments[0])
        await ctx.send("```Process Completed```")


    			#await attachment.save(attachment.filename)
    @commands.command()
    @commands.is_owner()
    async def upload(self,ctx: commands.Context,*,foldername):
        errfile=[]         
        #try:
        arr = os.listdir(foldername)
        def check(message: discord.Message):
            return message.author == ctx.author and message.channel == ctx.channel
        await ctx.send('All the items more than **8 MB** will be *copied* to a folder. Please specify the foldername:')
        mb = await self.bot.wait_for('message', check=check)
        for p in arr:
            if ".png" in p.lower() or ".jpg" in p.lower() or ".JPG" in p.lower() or ".PNG" in p.lower() or ".JPEG" in p.lower() or ".jpeg" in p.lower()  or ".GIF" in p.lower() or ".gif" in p.lower() or ".mp4" in p.lower() or ".MP4" in p.lower() or ".AVI" in p.lower() or ".3gp" in p.lower() or ".pdf" in p.lower() or ".PDF" in p.lower() or ".docx" in p.lower() or ".xlsx" in p.lower() or ".pptx" in p.lower() or ".3gp" in p.lower() or ".mp3" in p.lower() or ".zip" in p.lower() or ".txt" in p.lower() or ".TXT" in p.lower():
                files=foldername+"\\"+ str(p)
                if int(os.path.getsize(files)) < 8388608:
                    #deets=str(p)+" : "+str(os.path.getsize(files))   #you can print this to get size of each of em
                    await ctx.send(file=discord.File(files))
                elif int(os.path.getsize(files)) > 8388608:
                    copier = "C:\\Users\\Admin\\Desktop\\8mb+"+"\\"+str(mb.content)
                    if not os.path.isdir(copier):
                        os.makedirs(copier)
                    destination=str(copier)+"\\"+str(p)
                    shutil.copy2(files, destination)
            else:
                try:
                    files=foldername+"\\"+ str(p)
                    copier = "C:\\Users\\Admin\\Desktop\\8mb+"+"\\"+str(mb.content)
                    if not os.path.isdir(copier):
                        os.makedirs(copier)
                    destination=str(copier)+"\\"+str(p)
                    shutil.copy2(files, destination)
                except:
                    er="```"+str(p)+" couldn't be uploaded and moved to folder. Path: "+foldername+"\\"+ str(p)+"```"
                    errfile.append(er)
        if len(errfile)>1:
            for ei in errfile:
                await ctx.send(ei)
        await ctx.send("```Process Completed```")


        #except:
        #    await ctx.send("Path specified is either **wrong** or **does not exist**")
        


       

    

def setup(client):
    client.add_cog(imageMOD(client))

