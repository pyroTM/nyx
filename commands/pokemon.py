import discord
from discord.ext import commands
from simple_chalk import chalk
import requests


class Pokemon(commands.Cog):

    def __init__(self, nyx):
        self.nyx = nyx

    def getInfo(self, call):
        r = requests.get(call)
        return r.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.green.bold(f"[ENABLED] Command pokemon"))

    @commands.command()
    async def pokemon(self, ctx, pokemon):
        url = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
        info = self.getInfo(url)
        id = info['id']
        type = info['type'][0]
        ability1 = info['abilities'][0]
        ability2 = info['abilities'][1]
        height = info['height']
        desc = info['description']
        generation = info['generation']
        thumb = info['sprites']['animated']
        e = discord.Embed(title=f"{pokemon}",
                          color=discord.Color.blurple(), description=desc)
        e.add_field(name="Name", value=pokemon)
        e.add_field(name="ID", value=id)
        e.add_field(name='Type', value=type)
        e.add_field(name='Abilities', value=f"{ability1}\n{ability2}")
        e.add_field(name="Height", value=height)
        e.add_field(name='Generation', value=generation)

        e.set_thumbnail(url=thumb)
        await ctx.send(embed=e)


def setup(nyx):
    nyx.add_cog(Pokemon(nyx))
