import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class Hug(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command hug"))

    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        url = "https://some-random-api.ml/animu/hug"
        info = self.getInfo(url)
        img = info['link']
        e = discord.Embed(title=f"{ctx.message.author.display_name} hugs {member.display_name}!",
                          color=discord.Color.blurple())
        e.set_image(url=img)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Hug(nyx))
