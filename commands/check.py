import discord
import requests
from discord.ext import commands
from simple_chalk import chalk


class Check(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def rq(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command check"))

    @commands.command()
    async def check(self, ctx, member: discord.Member = None):
        url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
        e = self.rq(url)
        resp = e["insult"]
        response = f"{member.mention} :skull:, {resp}"

        await ctx.send(response)


def setup(nyx):
    nyx.add_cog(Check(nyx))
