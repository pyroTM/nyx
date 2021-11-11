from simple_chalk import chalk
import discord
import json
from discord.ext import commands
import datetime


class AntiChannel(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] AntiNuke: AntiChannel"))

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        with open('whitelisted.json') as f:
            whitelisted = json.load(f)
        async for i in channel.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                                                action=discord.AuditLogAction.channel_create):
            if str(i.user.id) in whitelisted[str(channel.guild.id)]:
                return

            await channel.guild.kick(i.user, reason="Nyx Anti-Nuke: Creating Channels")
            await i.target.delete(reason=f"Nyx Anti-Nuke: Deleting user created channels")
            await i.target.delete(reason=f"Nyx Anti-Nuke: Deleting user created channels")
            return

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        async for i in channel.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                                                action=discord.AuditLogAction.channel_delete):
            await channel.guild.kick(i.user, reason="Nyx Anti-Nuke: Deleting Channels")
            return


def setup(nyx):
    nyx.add_cog(AntiChannel(nyx))
