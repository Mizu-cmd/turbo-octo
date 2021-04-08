import discord
from discord.ext import commands
import errors
from cogs.events import private_rooms

class privroom(commands.Cog):


    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def privroom(self, ctx, arg):
        print(private_rooms[ctx.author.id])
        if not ctx.author.id in private_rooms:
            await ctx.send(embed=errors.make_error("You must have a room to do that", "Create one !"))
            await ctx.message.delete()
            return
        if arg.lower() == "yes":
            print("yes")
            await private_rooms[ctx.author.id].set_permission(ctx.guild.default_role, view_channel=False)
            embedVar = discord.Embed(title=f"Successfully made room private", color=0x61aaf1)
            await ctx.send(embed=embedVar)
        elif arg.lower() == "no":
            channel = private_rooms[ctx.author.id]
            print(channel)
            channel.set_permission(ctx.guild.default_role, view_channel=True)
            embedVar = discord.Embed(title=f"Successfully made room public", color=0x61aaf1)
            await ctx.send(embed=embedVar)
    
    @privroom.error
    async def privroom_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=errors.make_error("This command take one positional argument", "-o privroom [yes/no]"))
            await ctx.message.delete()

def setup(client):
    client.add_cog(privroom(client))