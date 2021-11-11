import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class AnimeQ(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command animeq"))

    @commands.command()
    async def animeq(self, ctx):
        url = "https://some-random-api.ml/animu/quote"
        info = self.getInfo(url)
        quote = info["sentence"]
        char = info["characther"]
        anime = info["anime"]

        e = discord.Embed(title="Anime Quote", color=discord.Color.blurple())
        e.add_field(name="Requested by:", value=ctx.message.author.mention)
        e.add_field(name="Quote:", value=quote)
        e.add_field(name="Character:", value=char)
        e.add_field(name="Anime:", value=anime)
        e.set_footer(text="Command Requested by qtgang :)")
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(AnimeQ(nyx))
