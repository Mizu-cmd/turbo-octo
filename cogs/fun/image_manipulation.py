import discord
from discord.ext import commands
from discord import File
import errors
import requests
import os
import asyncio
import numpy
from PIL import Image

class image_manipulation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def distord(self, ctx, member:discord.Member):
        response = requests.get(member.avatar_url, stream=True)

        with open("image.png", "wb") as f:
            f.write(response.content)

        image = Image.open("image.png")
        HSV= image.convert('HSV')
        H, S, V = HSV.split()

        m = numpy.asarray(image)
        m2 = numpy.zeros((image.size[0],image.size[1],3))
        width = image.size[0]
        height = image.size[1]

        A = m.shape[0] / 3.0
        w = 1.0 / m.shape[1]

        shift = lambda x: A * numpy.sin(2.0*numpy.pi*x * w)

        for i in range(m.shape[0]):
            m2[:,i] = numpy.roll(m[:,i], int(shift(i)))

        im2 = Image.fromarray(numpy.uint8(m2))

        HSVr = Image.merge('HSV', (H,S,V))
        RGBr = HSVr.convert('RGB')
        im2.save("output.png","PNG")
        await ctx.send(file=File("output.png"))

def setup(client):
    client.add_cog(image_manipulation(client))