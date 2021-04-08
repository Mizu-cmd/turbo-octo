from discord.ext import commands
from pages import *
import asyncio

class help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        pages = 2
        cur_page = 1
        message = await ctx.send(embed=help_1)

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "▶️":
                    cur_page += 1
                
                if str(reaction.emoji) == "◀️":
                    cur_page -= 1

                if cur_page > pages:
                    await message.remove_reaction(reaction, user)
                    cur_page -= 1
                elif cur_page < 1:
                    await message.remove_reaction(reaction, user)
                    cur_page += 1

                if cur_page == 1:
                    await message.edit(embed=help_1)
                    await message.remove_reaction(reaction, user)
                elif cur_page == 2:
                    await message.edit(embed=help_2)
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                await message.delete()
                break

def setup(client):
    client.add_cog(help(client))