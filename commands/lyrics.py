import discord
from discord.ext import commands
from simple_chalk import chalk
import requests
from discord_slash import SlashCommand


class Lyrics(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command lyrics"))

    @commands.command()
    async def lyrics(self, ctx, *, songname):
        url = f"https://some-random-api.ml/lyrics?title={songname}"
        info = self.getInfo(url)
        title = info['title']
        author = info['author']
        lyrics = info['lyrics']
        thumb = info['thumbnail']['genius']
        urle = info['links']['genius']
        e = discord.Embed(title=f"Lyrics for {songname}",
                          color=discord.Color.blurple(), description=lyrics)
        e.set_thumbnail(url=thumb)
        e.set_author(name=author, icon_url=thumb, url=urle)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Lyrics(nyx))
