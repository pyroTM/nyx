import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class Cat(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command cat"))

    @commands.command()
    async def cat(self, ctx):
        url = "https://some-random-api.ml/img/cat"
        url2 = "https://some-random-api.ml/facts/cat"
        info = self.getInfo(url)
        info2 = self.getInfo(url2)
        fact = info2['fact']
        img = info['link']

        e = discord.Embed(title=fact, color=discord.Color.blurple())
        e.set_image(url=img)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Cat(nyx))
