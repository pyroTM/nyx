import discord
from discord.ext import commands
import requests
import time
import random
import colorama
import pyfiglet

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


@nyx.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

    embed = discord.Embed(title=f"Member Ban")
    embed.add_field(name="Member Banned", value=f"{member.tag}")
    embed.add_field(name="Reason", value=f"{reason}")
    embed.set_thumbnail(url=f"https://media4.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif?cid"
                            f"=ecf05e47gpl02iozuxpbvq7njw7rloocsq0zbxip42z4kaj3&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

    embed = discord.Embed(title=f"Member Kick")
    embed.add_field(name="Member Kicked", value=f"{member.tag}")
    embed.add_field(name="Reason", value=f"{reason}")
    embed.set_thumbnail(url=f"https://media4.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif?cid"
                            f"=ecf05e47gpl02iozuxpbvq7njw7rloocsq0zbxip42z4kaj3&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
@commands.has_permissions(ADMINISTRATOR=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

    embed = discord.Embed(title=f"Member Unban")
    embed.add_field(name="Member Unbanned", value=f"{member.tag}")
    embed.set_thumbnail(
        url=f"https://media4.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif?cid"
            f"=ecf05e47gpl02iozuxpbvq7njw7rloocsq0zbxip42z4kaj3&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
async def ascii(ctx, *, text):
    ascii_output = pyfiglet.figlet_format(f"{text}")
    await ctx.send(ascii_output)


nyx.run("")
