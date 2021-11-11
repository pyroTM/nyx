import discord
from discord.ext import commands
from simple_chalk import chalk


class Ping(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command ping"))

    @commands.command(name="ping", pass_context=True, aliases=["latency"])
    async def ping(self, ctx):
        embed = discord.Embed(title="__**Latency**__", colour=discord.Color.blurple(),
                              timestamp=ctx.message.created_at)
        embed.add_field(name="Latency :", value=f"`{round(self.nyx.latency * 1000)} ms`")

        await ctx.send(embed=embed)


def setup(nyx):
    nyx.add_cog(Ping(nyx))
