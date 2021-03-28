import discord
from discord import emoji
from discord.ext import commands
import json
from decouple import config


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


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '-o '

    with open('channels.json', 'r') as f:
        channels = json.load(f)

    prefixes[str(guild.id)] = '-o '
    channels[str(guild.id)] = {}

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    with open('channels.json', 'w') as f:
        json.dump(channels, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    with open('channels.json', 'r') as f:
        channels = json.load(f)

    prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    with open('channels.json', 'w') as f:
        json.dump(channels, f, indent=4)


@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix + ""

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    embedVar = discord.Embed(
        title=f"Successfully changed prefix to {prefix}", color=0x61aaf1)
    await ctx.send(embed=embedVar)

private_rooms = {}

@client.event
async def on_voice_state_update(member, before, after):
    if member.id in private_rooms:
        await private_rooms[member.id].delete()
        private_rooms.pop(member.id)

    if after.channel is not None:
        with open('channels.json', 'r') as f:
            channels = json.load(f)
            if str(after.channel.id) in channels[str(member.guild.id)]:
                overwrites = {
                    member.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    member.guild.me: discord.PermissionOverwrite(read_messages=True)
                }
                channel = await member.guild.create_voice_channel(member.name + " 's channel", overwrites=overwrites, user_limit=after.channel.user_limit)
                await member.move_to(channel)
                private_rooms[member.id] = channel


@client.command()
@commands.has_permissions(administrator=True)
async def addroom(ctx, channel):
    with open('channels.json', 'r') as f:
        channels = json.load(f)

    guild = ctx.guild.id
    if channel not in channels[str(guild)]:
        channels[str(guild)] += [channel]
    
        with open("channels.json", "w") as file:
            json.dump(channels, file, indent=4)

    embedVar = discord.Embed(title=f"Successfully added the channel {channel} to user's custom channel maker", color=0x61aaf1)
    await ctx.send(embed=embedVar)


@client.command()
async def help(ctx):
    page1 = discord.Embed(title="Rooms", color=0x61aaf1)
    page1.add_field(name="Create rooms", value="addroom [id_channel]  ││  Create private room", inline=False)
    page1.add_field(name="Delete rooms", value="delroom [id_channel]  ││  Delete private room", inline=False)
    page1.add_field(name="Rooms names", value="nameroom [id_channel] [name]  ││  Rename private room", inline=False)
    page1.add_field(name="Private room", value="privroom [id_channel] [yes/no]  ││  Enable or disable private room", inline=False)
    page1.set_footer(text="Page 1/4", icon_url="https://cdn.discordapp.com/avatars/825696493037944882/db7f3d6bbe165222fc75b50402fcfdec.webp")
    page2 = discord.Embed(title="Commands", color=0x61aaf1)
    page2.add_field(name="Change prefix", value="changeprefix [prefix]  ││  Change prefix bot", inline=False)
    page2.set_footer(text="Page 2/4", icon_url="https://cdn.discordapp.com/avatars/825696493037944882/db7f3d6bbe165222fc75b50402fcfdec.webp")
    final_message = await ctx.send(embed=page2)
    await final_message.add_reaction('◀')
    await final_message.add_reaction('▶')

client.run(token)
client.add_command(changeprefix)
client.add_command(help)
client.add_command(addroom)
