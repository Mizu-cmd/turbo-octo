import discord
from discord.ext import commands
import errors

class araah(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def araah(self, ctx):
        if ctx.message.author.voice is not None:
            for member in ctx.message.author.voice.channel.members:
                if member.id != ctx.author.id:
                    await member.move_to(None)
        else:
            await ctx.send(embed=errors.make_error("You must be in a voice channel to do that", "Join One !"))
            await ctx.message.delete()
            return

    @araah.error
    async def araah_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("It seems there are no police there !")
            await ctx.message.delete()
def setup(client):
    client.add_cog(araah(client))