import discord
from discord.ext import commands
from simple_chalk import chalk
import random


class Pixelate(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command rps"))

    @commands.command()
    async def rps(self, ctx, choice: str):
        author = ctx.author
        rpsbot = {"rock": ":moyai:",
                  "paper": ":page_facing_up:",
                  "scissors": ":scissors:"}
        choice = choice.lower()
        if choice in rpsbot.keys():
            botchoice = random.choice(list(rpsbot.keys()))
            msgs = {
                "win": " You win {}!".format(author.mention),
                "square": " We're Tied {}!".format(author.mention),
                "lose": " You lose {}!".format(author.mention)
            }
            if choice == botchoice:
                await ctx.send(rpsbot[botchoice] + msgs["square"])
            elif choice == "rock" and botchoice == "paper":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "rock" and botchoice == "scissors":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "rock":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "scissors":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "rock":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "paper":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
        else:
            await ctx.send("Choose rock, paper or scissors.")


def setup(nyx):
    nyx.add_cog(Pixelate(nyx))
