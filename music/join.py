import discord
import pyfiglet
from discord.ext import commands
from simple_chalk import chalk


class Join(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command Music: join"))

    @commands.command()
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            return await ctx.send("Please join a voice channel!")
        await ctx.author.voice.channel.connect()
        e = discord.Embed(title="Nyx Music", color=discord.Color.blurple())
        e.add_field(name="Joined Channel:", value=f"{ctx.author.voice.channel}")
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Join(nyx))
