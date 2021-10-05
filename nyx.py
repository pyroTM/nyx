import discord
from discord.ext import commands
import requests
import time
import random
import colorama

intents = discord.Intents().all()

nyx = commands.Bot(command_prefix='$', intents=intents)


def getInfo(call):
    r = requests.get(call)
    return r.json()


@nyx.event
async def on_ready():
    print(f'Logged in as {nyx.user} (ID: {nyx.user.id})')
    print('------')
    await nyx.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nyxbot.gq"))


@nyx.command()
async def getskin(ctx, username):
    skin = discord.Embed(title=f"Skin of {username}",
                         description=f"The skin of the player {username}",
                         color=0x00ff00)
    skin.add_field(value=f"[Download](https://mc-heads.net/download/{username})", name=f"{username}")
    skin.set_thumbnail(url=f"https://craftar.com/avatars/{username}")
    skin.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=skin)


nyx.run("")
