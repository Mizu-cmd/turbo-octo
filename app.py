import discord
from discord import emoji
from discord.ext import commands
import json
from decouple import config
import asyncio

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)
token = config('DISCORD_BOT_TOKEN')
client.remove_command("help")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("Turbo Octo ! Manage Roles"))

cogs = ["help", "addroom", "changeprefix", "events"]

if __name__ == "__main__": 
    for cog in cogs:
        client.load_extension("cogs."+cog)

    client.run(token)
    client.add_command("help")
    client.add_command("addroom")
    client.add_command("changeprefix")
