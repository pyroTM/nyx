import discord
import pyfiglet
from discord.ext import commands
from simple_chalk import chalk


class TopRole(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command toprole"))

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        e = discord.Embed(title=f"Top Role for {member.display_name}", color=discord.Color.blurple())
        e.add_field(name="\uFEFF", value=member.top_role.mention)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(TopRole(nyx))
