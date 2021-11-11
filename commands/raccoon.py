import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class Raccoon(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command raccoon"))

    @commands.command()
    async def raccoon(self, ctx):
        url = "https://some-random-api.ml/img/raccoon"
        url2 = "https://some-random-api.ml/facts/raccoon"
        info = self.getInfo(url)
        info2 = self.getInfo(url2)
        fact = info2['fact']
        img = info['link']

        e = discord.Embed(title=fact, color=discord.Color.blurple())
        e.set_image(url=img)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Raccoon(nyx))
