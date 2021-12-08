import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class snipe(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx
        self.last_msg = None

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message


    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command snipe"))

    @commands.command()
    async def snipe(self, ctx):
        if not self.last_msg:
            await ctx.send("No recent deleted messages")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"Last Deleted Message", description="`" + content + "`")
        embed.set_author(name=author)
        await ctx.send(embed=embed)

def setup(nyx):
    nyx.add_cog(snipe(nyx))
