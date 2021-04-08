import discord
from discord.ext import commands
import json
import errors
import asyncio

private_rooms = {}

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
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

    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        with open('channels.json', 'r') as f:
            channels = json.load(f)

        prefixes.pop(str(guild.id))
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        with open('channels.json', 'w') as f:
            json.dump(channels, f, indent=4)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
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

def setup(client):
    client.add_cog(events(client))