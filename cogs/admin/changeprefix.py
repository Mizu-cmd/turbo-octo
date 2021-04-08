import discord
from discord.ext import commands
import errors
import json

class changeprefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix + " "

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        embedVar = discord.Embed(title=f"Successfully changed prefix to {prefix}", color=0x61aaf1)
        await ctx.send(embed=embedVar)
    
        
    @changeprefix.error
    async def addroom_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=errors.make_error("This command take one positional argument", "-o changeprefix [new prefix]"))
            await ctx.message.delete()

def setup(client):
    client.add_cog(changeprefix(client))