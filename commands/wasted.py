import discord
from discord.ext import commands
from simple_chalk import chalk


class Wasted(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command wasted"))

    @commands.command()
    async def wasted(self, ctx, member: discord.Member = None):
        url = f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url}"
        e = discord.Embed(title="\uFEFF", color=discord.Color.blurple())
        e.set_image(url=url)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Wasted(nyx))
