import discord
from discord.ext import commands
from simple_chalk import chalk


class Purge(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command purge"))

    @commands.command(aliases=['clean', 'cls', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount + 1)


def setup(nyx):
    nyx.add_cog(Purge(nyx))
