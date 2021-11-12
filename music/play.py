import discord
import pyfiglet
from discord.ext import commands
from simple_chalk import chalk
import DiscordUtils.Music

music = DiscordUtils.Music()


class Play(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command Music: beta play"))

    @commands.command()
    async def play(self, ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            e = discord.Embed(title="Nyx Music", color=discord.Color.blurple())
            e.add_field(name="Started Playing:", value=f"{song.name}")
            await ctx.send(embed=e)
        else:
            song = await player.queue(url, search=True)
            e = discord.Embed(title="Nyx Music", color=discord.Color.blurple())
            e.add_field(name="Added to Queue:", value=f"{song.name}")
            await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Play(nyx))
