import discord
from discord.ext import commands
from simple_chalk import chalk


class Pixelate(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command pixelate"))

    @commands.command()
    async def pixelate(self, ctx, member: discord.Member = None):
        url = f"https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url}"
        e = discord.Embed(title="\uFEFF", color=discord.Color.blurple())
        e.set_image(url=url)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Pixelate(nyx))
