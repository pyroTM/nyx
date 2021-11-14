import discord
from discord.ext import commands
from simple_chalk import chalk
import requests
import json
import random
import os

os.chdir("C:\\Users\\trisa\\PycharmProjects\\nyx\\economy")


class Economy(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Economy"))

    @commands.command()
    async def balance(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        cash_amount = users[str(user.id)]["cash"]
        bank_amount = users[str(user.id)]["bank"]

        e = discord.Embed(title=f"{ctx.author.name}'s balance", color=discord.Color.blurple())
        e.add_field(name="Cash", value=cash_amount)
        e.add_field(name="Bank", value=bank_amount)
        await ctx.send(embed=e)

    @commands.command()
    async def beg(self, ctx):
        await open_account(ctx.author)
        users = await get_bank_data()

        user = ctx.author
        earnings = random.randrange(71)
        begresp = [f"Someone takes pity on your poor ass and grants you 🪙 {earnings}",
                   f"You give the rich kid a blowjob and earn 🪙 {earnings}",
                   f"You beg Elon Musk and earn 🪙 {earnings}",
                   f"You terrorize some foreign tourists and earn  🪙 {earnings}"]

        e = discord.Embed(description=random.choice(begresp))
        e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

        users[str(user.id)]["cash"] = users[str(user.id)]["cash"] + earnings

        with open("bank.json", "w") as f:
            json.dump(users, f)

    @commands.command()
    async def withdraw(self, ctx, amount=None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("You dont have that much you dumb fuck, get some money then try again")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[1]:
            await ctx.send("You don't have that much money, prick")
            return
        if amount < 0:
            await ctx.send("Did you fail school? you cant take away nothing")
            return

        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1 * amount, "bank")
        await ctx.send(f"You withdrew 🪙 {amount} from your bank!")

    @commands.command()
    async def deposit(self, ctx, amount=None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("You have nothing to deposit, maybe i will give you some if you get on your knees and beg")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[0]:
            await ctx.send("You don't have that much money, prick")
            return
        if amount < 0:
            await ctx.send("Did you fail school? you cant add nothing")
            return

        await update_bank(ctx.author, -1 * amount)
        await update_bank(ctx.author, amount, "bank")
        await ctx.send(f"You deposited 🪙 {amount}!")


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["cash"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="cash"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["cash"], users[str(user.id)]["bank"]]
    return bal


def setup(nyx):
    nyx.add_cog(Economy(nyx))
