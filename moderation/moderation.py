import datetime
import asyncio
import discord
from discord.ext import commands
from simple_chalk import chalk
import requests
import random


class mod(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Moderation"))

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel locked.')

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!",
                             description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!",
                            description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        role_members = discord.utils.get(ctx.guild.roles, name='Members')
        role_muted = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role_members)
        await member.add_roles(role_muted)
        await context.send("User was muted")

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        role_members = discord.utils.get(ctx.guild.roles, name='Members')
        role_muted = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role_muted)
        await member.add_roles(role_members)
        await context.send("User was unmuted")

    @commands.command()
    async def afk(self, ctx, reason=None):
        current_nick = ctx.author.nick
        await ctx.send(f"{ctx.author.mention} is afk: {reason} ")
        await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            if counter == int(mins):
                await ctx.author.edit(nick=current_nick)
                await ctx.send(f"{ctx.author.mention} is no longer AFK")
                break


def setup(nyx):
    nyx.add_cog(mod(nyx))
