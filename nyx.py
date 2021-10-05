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
    skin.set_thumbnail(url=f"https://minotar.net/avatar/{username}")
    skin.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=skin)


@nyx.command()
async def getuuid(ctx, username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    data = getInfo(url)
    uuid = data["id"]

    getid = discord.Embed(title=f"{username} to UUID")
    getid.add_field(name=f"UUID of Player: {username}", value=f"{uuid}")
    getid.set_thumbnail(url=f"https://minotar.net/avatar/{username}")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def crystalball(ctx, *, question):
    url = f"https://8ball.delegator.com/magic/JSON/{question}"
    data = getInfo(url)
    response = data["magic"]["answer"]
    getid = discord.Embed(title=f"Crystal Ball")
    getid.add_field(name="Your question was:", value=f"{question}", inline=False)
    getid.add_field(name=f"The all-knowing Crystall Ball says:", value=f"{response}", inline=False)
    getid.set_thumbnail(url=f"https://www.macmillandictionary.com/external/slideshow/full/emoji_crystal_ball_full.jpg")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


nyx.run("")
