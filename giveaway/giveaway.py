import datetime
import asyncio
import discord
from discord.ext import commands
from simple_chalk import chalk
import requests
import random


class Giveaway(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Giveaway"))

    @commands.command()
    @commands.has_role("🚀 Owner")
    async def gstart(self, ctx):
        def convert(self, time):
            pos = ["s", "m", "h", "d"]
            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}
            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2

            return val * time_dict[unit]

        await ctx.send("Let's start creating this giveaway! Answer these questions within 15 minutes!")
        qs = ["❓ Which channel should this giveaway be hosted in? ", "❓ How long will the giveaway last? ",
              "❓ What is the prize for this giveaway? "]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in qs:
            await ctx.send(i)
            try:
                msg = await self.nyx.wait_for('message', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('Timed Out')
                return
            else:
                answers.append(msg.content)
        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"You didn't mention a channel properly. Please use {ctx.channel.mention}. ")
            return
        channel = self.nyx.get_channel(c_id)

        time = convert(self, time=answers[1])
        if time == 1:
            await ctx.send(f"You didn't answer with a proper unit of time. Please use (s|m|h|d)")
            return
        elif time == -2:
            await ctx.send(f"The time must be an integer. Please enter an integer next time.")
            return
        prize = answers[2]

        await ctx.send(f"🥳 The giveaway will be in {channel.mention} and will last {time} seconds")

        e = discord.Embed(title="Giveaway! 🥳 ", description=f"{prize}", color=discord.Color.blurple())
        e.add_field(name="Hosted By:", value=ctx.author.mention)
        e.set_footer(text=f"Ends in {answers[1]} from now!")
        mymsg = await channel.send(embed=e)
        await mymsg.add_reaction("🎉")
        await asyncio.sleep(time)
        nmsg = await channel.fetch_message(mymsg.id)
        users = await nmsg.reactions[0].users().flatten()
        users.pop(users.index(self.nyx.user))
        winner = random.choice(users)
        await channel.send(f"🥳 Congratulations! {winner.mention} you won the **{prize}**!")

    @commands.command()
    @commands.has_role("🚀 Owner")
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        try:

            nmsg = await channel.fetch_message(id_)
        except:
            await ctx.send("Incorrect Message ID!")
            return

        users = await nmsg.reactions[0].users().flatten()
        users.pop(users.index(self.nyx.user))
        winner = random.choice(users)

        await channel.send(f"Congratulations! The new winner is {winner.mention}!")


def setup(nyx):
    nyx.add_cog(Giveaway(nyx))
