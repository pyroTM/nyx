import discord
from discord.ext import commands
from simple_chalk import chalk
import requests
import json
import random
import os

os.chdir("C:\\Users\\trisa\\PycharmProjects\\nyx\\economy")
mainshop = [{"name": "Discord Color Pass", "price": 100, "description": "Access to the Discord Color Roles!"}]


class Economy(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Economy"))

    @commands.command(aliases=["bal", "cash"])
    async def balance(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        await open_account(member)
        user = member
        users = await get_bank_data()

        cash_amount = users[str(user.id)]["cash"]
        bank_amount = users[str(user.id)]["bank"]

        e = discord.Embed(title=f"{member.name}'s balance", color=discord.Color.blurple())
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

    @commands.command(aliases=["w"])
    async def withdraw(self, ctx, amount=None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("You dont have that much you dumb fuck, get some money then try again")
            return
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[1]
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

    @commands.command(aliases=["d", "dep"])
    async def deposit(self, ctx, amount=None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("You have nothing to deposit, maybe i will give you some if you get on your knees and beg")
            return
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[0]
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

    @commands.command(aliases=["send"])
    async def pay(self, ctx, member: discord.Member, amount=None):
        await open_account(ctx.author)
        await open_account(member)

        if amount == None:
            await ctx.send("You cannot send nothing! Please enter an amount to send!")
            return
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[1]

        amount = int(amount)

        if amount > bal[1]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive!")
            return

        await update_bank(ctx.author, -1 * amount, "bank")
        await update_bank(member, amount, "bank")
        await ctx.send(f"You paid {member} 🪙 {amount}!")

    @commands.command(aliases=["gamble"])
    async def slots(self, ctx, amount=None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("You cannot bet nothing!")
            return
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[0]
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive!")
            return

        final = []
        for i in range(3):
            a = random.choice(["🍒", "🌙", "🏅", "🤞", "🏆", "🟥", "🟩"])
            final.append(a)

        await ctx.send(str(final))

        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await update_bank(ctx.author, 2 * amount)
            await ctx.send(f"Congratulations you won 🪙 {1 * amount}!")
        else:
            await update_bank(ctx.author, -1 * amount)
            await ctx.send(f"Better luck next time,  you lost 🪙 {amount}!")

    @commands.command(aliases=["steal"])
    async def rob(self, ctx, member: discord.Member):
        await open_account(ctx.author)
        await open_account(member)
        bal = await update_bank(member)

        if bal[0] < 100:
            await ctx.send("Their also broke :skull:")
            return

        robbings = random.randrange(1, bal[0])

        robresp = [f"You were caught attempting to rob {member}, and have been fined 🪙 {robbings}",
                   f"You robbed 🪙 {robbings} from {member}"]

        robbingse = random.choice(robresp)
        if robbingse == robresp[1]:
            await update_bank(ctx.author, robbings)
            await update_bank(member, -1 * robbings)

        elif robbingse == robresp[0]:
            await update_bank(ctx.author, -1 * robbings)

        e = discord.Embed(description=robbingse)
        e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx, x=10):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["cash"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total, reverse=True)

        em = discord.Embed(title=f":bank:   {ctx.guild.name} Leaderboard", description="Cash & Bank",
                           color=discord.Color.blurple())
        index = 1

        for amt in total:
            id_ = leader_board[amt]
            member = self.nyx.get_user(id_)
            name = member.name
            em.add_field(name=f"{index}. {name} • 🪙 {amt}", value=f"\uFEFF", inline=False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed=em)


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


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "cash")

    return [True, "Worked"]


def setup(nyx):
    nyx.add_cog(Economy(nyx))
