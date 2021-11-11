import discord
from discord.ext import commands
from simple_chalk import chalk


class Comment(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command comment"))

    @commands.command()
    async def comment(self, ctx, member: discord.Member, *, comment):
        url = f"https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar_url}&username={member.display_name}&comment={comment}"
        e = discord.Embed(title="*still in beta*", color=discord.Color.blurple())
        e.set_image(url=url)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Comment(nyx))
