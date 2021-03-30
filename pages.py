import discord

def __help_1():
    page1 = discord.Embed(title="Rooms", color=0x61aaf1)
    page1.add_field(name="Create rooms", value="addroom [id_channel]  ││  Create private room", inline=False)
    page1.add_field(name="Delete rooms", value="delroom [id_channel]  ││  Delete private room", inline=False)
    page1.add_field(name="Rooms names", value="nameroom [id_channel] [name]  ││  Rename private room", inline=False)
    page1.add_field(name="Private room", value="privroom [id_channel] [yes/no]  ││  Enable or disable private room", inline=False)
    page1.set_footer(text="Page 1/4", icon_url="https://cdn.discordapp.com/avatars/825696493037944882/db7f3d6bbe165222fc75b50402fcfdec.webp")
    return page1

def __help_2():
    page2 = discord.Embed(title="Commands", color=0x61aaf1)
    page2.add_field(name="Change prefix", value="changeprefix [prefix]  ││  Change prefix bot", inline=False)
    page2.set_footer(text="Page 2/4", icon_url="https://cdn.discordapp.com/avatars/825696493037944882/db7f3d6bbe165222fc75b50402fcfdec.webp")
    return page2

help_1 = __help_1()
help_2 = __help_2()