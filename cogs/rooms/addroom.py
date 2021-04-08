import discord
from discord.ext import commands
import errors
import json

class addroom(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addroom(self, ctx, channel):

        if len(channel) < 18:
            await ctx.send(embed=errors.make_error("This is not a valid channel id", "-o addroom [room id]"))
            await ctx.message.delete()
            return

        with open('channels.json', 'r') as f:
            channels = json.load(f)

        guild = ctx.guild.id
        if channel not in channels[str(guild)]:
            if len(channels[str(guild)]) == 0:
                channels[str(guild)] = [channel]
            else :
                channels[str(guild)] += [channel]
        
            with open("channels.json", "w") as file:
                json.dump(channels, file, indent=4)

            embedVar = discord.Embed(title=f"Successfully added the channel {channel} to user's custom channel maker", color=0x61aaf1)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send(embed=errors.make_error("This channel is allready added as vocal maker", "-o addroom [room id]"))
            await ctx.message.delete()
            return
    
    @addroom.error
    async def addroom_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=errors.make_error("This command take one positional argument", "-o addroom [room id]"))
            await ctx.message.delete()
        

def setup(client):
    client.add_cog(addroom(client))