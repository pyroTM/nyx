import discord
import pyfiglet
from discord.ext import commands
from simple_chalk import chalk


class Google(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command google"))

    @commands.command(name="google", aliases=["lmgt", "lmgtfy"])
    async def command_google(self, ctx, *, query: str) -> None:
        if len(query) > 250:
            return await ctx.send("Your query should be no longer than 500 characters.")

        await ctx.send(f"<https://letmegooglethat.com/?q={query.replace(' ', '+')}>")


def setup(nyx):
    nyx.add_cog(Google(nyx))
