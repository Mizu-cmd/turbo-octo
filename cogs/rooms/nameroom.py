import discord
from discord.ext import commands
import errors

class nameroom(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def nameroom(self, ctx, name):
        from cogs.events import private_rooms
        if not ctx.author.id in private_rooms:
            await ctx.send(embed=errors.make_error("You must have a room to do that", "Join create a room channel"))
            await ctx.message.delete()
            return
        await private_rooms[ctx.author.id].edit(name=name)
        embedVar = discord.Embed(title=f"Successfully changed room name to {name}", color=0x61aaf1)
        await ctx.send(embed=embedVar)
    
    @nameroom.error
    async def nameroom_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=errors.make_error("This command take one positional argument", "-o nameroom [new room name]"))
            await ctx.message.delete()

def setup(client):
    client.add_cog(nameroom(client))