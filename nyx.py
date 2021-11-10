import discord
import platform
import os
from simple_chalk import chalk
import sys
import json
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents().all()
nyx = commands.Bot(command_prefix=config["bot_prefix"], intents=intents)


@nyx.event
async def on_ready():
    print("-------------------")
    print(chalk.blueBright.bold(f"Logged in as {nyx.user}"))
    print(chalk.yellow.bold(f"Discord.py API version: {discord.__version__}"))
    print(chalk.red.bold(f"Python version: {platform.python_version()}"))
    print(chalk.cyan.bold(f"Running on: {platform.system()} {platform.release()} ({os.name})"))
    print("-------------------")


@nyx.event
async def on_message(message):
    if message.author == nyx.user or message.author.bot:
        return
    await nyx.process_commands(message)


@nyx.event
async def on_command_error(ctx, error):
    raise error


@nyx.command()
async def enable(ctx, extension):
    nyx.load_extension(f'commands.{extension}')
    print(chalk.green.bold(f"[ENABLED] Command {extension}"))


@nyx.command()
async def disable(ctx, extension):
    nyx.unload_extension(f'commands.{extension}')
    print(chalk.red.bold(f"[DISABLED] Command {extension}"))


@nyx.command()
async def reload(ctx, extension):
    nyx.unload_extension(f'commands.{extension}')
    nyx.load_extension(f'commands.{extension}')


for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        nyx.load_extension(f'commands.{filename[:-3]}')

for filename in os.listdir('./antinuke'):
    if filename.endswith('.py'):
        nyx.load_extension(f'antinuke.{filename[:-3]}')

nyx.run(config["token"])
