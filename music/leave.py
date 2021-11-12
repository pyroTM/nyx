import discord
import pyfiglet
from discord.ext import commands
from simple_chalk import chalk


class Leave(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command Music: leave"))

    @commands.command()
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        myvoicetrue = ctx.guild.me.voice

        if voicetrue is None:
            return await ctx.send("Please join a voice channel!")
        if myvoicetrue is None:
            return await ctx.send("I am not in a voice channel!")
        await ctx.voice_client.disconnect()
        e = discord.Embed(title="Nyx Music", color=discord.Color.blurple())
        e.add_field(name="Left Channel:", value=f"{ctx.author.voice.channel}")
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Leave(nyx))
