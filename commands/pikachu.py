import discord
from discord.ext import commands
from simple_chalk import chalk
import requests
from discord_slash import SlashCommand


class Pikachu(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command pikachu"))

    @commands.command()
    async def pikachu(self, ctx):
        url = "https://some-random-api.ml/img/pikachu"
        info = self.getInfo(url)
        img = info['link']

        e = discord.Embed(title="\uFEFF", color=discord.Color.blurple())
        e.set_image(url=img)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Pikachu(nyx))
