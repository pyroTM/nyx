import discord
from discord.ext import commands
from simple_chalk import chalk


class Avatar(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command avatar"))

    @commands.command(aliases=["av", "pfp"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member: member = ctx.message.author
        message = discord.Embed(title=str(member), color=discord.Colour.blurple())
        message.set_image(url=member.avatar_url)

        await ctx.send(embed=message)


def setup(nyx):
    nyx.add_cog(Avatar(nyx))
