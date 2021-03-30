import discord

def make_error(error:str, exemple:str):
    embed=discord.Embed(title="Error", description=error, color=0xf32b2b)
    embed.add_field(name="exemple", value=exemple, inline=False)
    embed.set_footer(text="Turbo Octo - Error message", icon_url="https://cdn.discordapp.com/avatars/825696493037944882/db7f3d6bbe165222fc75b50402fcfdec.webp")
    return embed


