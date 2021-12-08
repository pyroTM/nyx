import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class meme(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command meme"))

    @commands.command()
    async def meme(self, ctx):
        url = f"https://meme-api.herokuapp.com/gimme"
        data = self.getInfo(url)

        memecap = data["title"]
        memeimg = data["preview"][2]
        e = discord.Embed(title=memecap, colour=discord.Color.blurple())
        e.set_image(url=memeimg)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(meme(nyx))
