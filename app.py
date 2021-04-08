import discord
from discord import emoji
from discord.embeds import Embed
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


admin = ["araah", "changeprefix", "help"]
fun = ["image_manipulation"]
rooms = ["addroom", "nameroom", "privroom"]
utils = []

cogs = [admin, fun, rooms, utils]
cogs_names = ["admin", "fun", "rooms", "utils"]

if __name__ == "__main__": 
    for i in range(0, len(cogs_names)):
        for j in range(0, len(cogs[i])):
            client.load_extension("cogs."+cogs_names[i]+"."+cogs[i][j])

    client.run(token)

    client.add_command("help")
    client.add_command("addroom")
    client.add_command("changeprefix")
    client.add_command("nameroom")
    client.add_command("privroom")
    client.add_command("araah")
