import discord
import pyfiglet
from discord.ext import commands
from simple_chalk import chalk


class Ascii(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command ascii"))

    @commands.command()
    async def ascii(self, ctx, *, text):
        output = pyfiglet.figlet_format(f"{text}")

        formatted_output = f"""
        ```{output}```
        """
        e = discord.Embed(color=discord.Color.blurple(), title=" ")
        e.add_field(name="ASCII", value=f"{formatted_output}")
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Ascii(nyx))
