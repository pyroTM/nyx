import discord
from pycoingecko import CoinGeckoAPI
from discord.ext import commands
import requests
import time
import random
import pyshorteners
import colorama
import pyfiglet

intents = discord.Intents().all()

nyx = commands.Bot(command_prefix='$', intents=intents)

cg = CoinGeckoAPI()


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
    information = getInfo(url)
    uuid = information["id"]

    getid = discord.Embed(title=f"{username} to UUID")
    getid.add_field(name=f"UUID of Player: {username}", value=f"{uuid}")
    getid.set_thumbnail(url=f"https://minotar.net/avatar/{username}")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def crystalball(ctx, *, question):
    url = f"https://8ball.delegator.com/magic/JSON/{question}"
    information = getInfo(url)
    response = information["magic"]["answer"]
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
@commands.has_permissions(administrator=True)
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
    await ctx.send("```" + ascii_output + "```")


@nyx.command()
async def bitcoin(ctx):
    getPrice = cg.get_price(ids='bitcoin', vs_currencies='usd')
    price = getPrice["bitcoin"]["usd"]
    embed = discord.Embed(title=f"Bitcoin Information")
    embed.add_field(name="Symbol", value=f"BTC")
    embed.add_field(name="Price", value=f"{price}")
    embed.set_thumbnail(url=f"https://media2.giphy.com/media/WT9wi81vtEhqt17SE4/giphy.gif?cid"
                            f"=790b761143f20a5641c571a193d1e5221da62f43859cc9b1&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
async def dogecoin(ctx):
    getPrice = cg.get_price(ids='dogecoin', vs_currencies='usd')
    price = getPrice["dogecoin"]["usd"]

    embed = discord.Embed(title=f"Dogecoin Information")
    embed.add_field(name="Symbol", value=f"DOGE")
    embed.add_field(name="Price", value=f"{price}")
    embed.set_thumbnail(url=f"https://media1.giphy.com/media/Ogak8XuKHLs6PYcqlp/giphy.gif?cid"
                            f"=ecf05e47x5w6pcxd2wknaj0he62dp3h2o6sjpwi238wh0jzt&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
async def ethereum(ctx):
    getPrice = cg.get_price(ids='ethereum', vs_currencies='usd')
    price = getPrice["ethereum"]["usd"]

    embed = discord.Embed(title=f"Ethereum Information")
    embed.add_field(name="Symbol", value=f"ETH")
    embed.add_field(name="Price", value=f"{price}")
    embed.set_thumbnail(url=f"https://media4.giphy.com/media/MagSgolK3ScWvtHAB4/giphy.gif?cid"
                            f"=ecf05e47fiizayka89wa8qsal4jn40cnvl8uuav63lievf5n&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
async def litecoin(ctx):
    getPrice = cg.get_price(ids='litecoin', vs_currencies='usd')
    price = getPrice["litecoin"]["usd"]

    embed = discord.Embed(title=f"Litecoin Information")
    embed.add_field(name="Symbol", value=f"LTC")
    embed.add_field(name="Price", value=f"{price}")
    embed.set_thumbnail(url="https://media4.giphy.com/media/9xyQZoR248xR3iONQo/giphy.gif?cid"
                            f"=ecf05e47ls56dii52ckykgxozblv1y80f6lst6ndsap5t8d0&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
async def cardano(ctx):
    getPrice = cg.get_price(ids='cardano', vs_currencies='usd')
    price = getPrice["cardano"]["usd"]

    embed = discord.Embed(title=f"Cardano Information")
    embed.add_field(name="Symbol", value=f"ADA")
    embed.add_field(name="Price", value=f"{price}")
    embed.set_thumbnail(url="https://media1.giphy.com/media/lQh95VIYba5yba2H08/giphy.gif?cid"
                            "=ecf05e47j74f0ntfm0g7njfbe1ztoavd1he4jnajegbhtt5f&rid=giphy.gif&ct=g")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command(aliases=['purge', 'delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = -1):
    if amount == -1:
        await ctx.channel.purge(limit=1000000)
    else:
        await ctx.channel.purge(limit=amount)


format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


@nyx.command()
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(
        color=ctx.guild.owner.top_role.color
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.add_field(name=f"Information About **{ctx.guild.name}**: ",
                    value=f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
    embed.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=embed)


@nyx.command()
async def kanye(ctx):
    url = "https://api.kanye.rest/"
    data = getInfo(url)
    quote = data["quote"]

    getid = discord.Embed(title="Kanye West says...")
    getid.add_field(name=f"Quote", value=f"{quote}")
    getid.set_thumbnail(url=f"https://upload.wikimedia.org/wikipedia/commons/thumb/1/10"
                            f"/Kanye_West_at_the_2009_Tribeca_Film_Festival_%28cropped%29.jpg/1200px"
                            f"-Kanye_West_at_the_2009_Tribeca_Film_Festival_%28cropped%29.jpg")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def qrcode(ctx, urle):
    code = f"http://api.qrserver.com/v1/create-qr-code/?data={urle}&size=100x100"
    getid = discord.Embed(title=f"QRCode Generated for {urle}")
    getid.set_image(url=code)
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def age(ctx, name):
    url = f"https://api.agify.io?name={name}"
    data = getInfo(url)
    age = data["age"]
    getid = discord.Embed(title=f"Predicted Age of: {name}")
    getid.add_field(name=f"Age", value=f"{age}")
    getid.set_thumbnail(url=f"https://melmagazine.com/wp-content/uploads/2021/01/66f-1.jpg")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def gender(ctx, name):
    url = f"https://api.genderize.io?name={name}"
    data = getInfo(url)
    gender = data["gender"]
    probability = data["probability"]
    percent = probability * 100
    getid = discord.Embed(title=f"Predicted Gender of: {name}")
    getid.add_field(name=f"Gender", value=f"{gender}")
    getid.add_field(name=f"Probability", value=f"{percent}")
    if gender == "male":
        getid.set_thumbnail(url=f"https://melmagazine.com/wp-content/uploads/2021/01/66f-1.jpg")

    elif gender == "female":

        getid.set_thumbnail(
            url="https://t3.ftcdn.net/jpg/02/45/34/90/360_F_245349044_TMxmWxPpnSzeuauvvQnuFe03ueXgS57m.jpg")

    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def screenshot(ctx, urle):
    code = f"https://api.apiflash.com/v1/urltoimage?access_key=&url={urle}"
    if "https" or "http" in urle:
        getid = discord.Embed(title=f"Screenshot Taken for {urle}")
        getid.set_image(url=code)
        getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
        await ctx.send(embed=getid)
    else:
        new = "https://" + urle
        newcode = f"https://api.apiflash.com/v1/urltoimage?access_key=&url={new}"
        getid = discord.Embed(title=f"Screenshot Taken for {urle}")
        getid.set_image(url=newcode)
        getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
        await ctx.send(embed=getid)


@nyx.command()
async def joke(ctx):
    url = f"https://karljoke.herokuapp.com/jokes/random"
    data = getInfo(url)
    setup = data["setup"]
    punchline = data["punchline"]
    getid = discord.Embed(title=f"Dad Joke")
    getid.add_field(name=f"Joke", value=f"{setup}")
    getid.add_field(name=f"Punchline", value=f"{punchline}")
    getid.set_thumbnail(
        url=f"https://yt3.ggpht.com/ytc/AKedOLRtJMw3bOqLjOW62ES2PNKpwK42j3bAQ2-TDqFSxg=s900-c-k-c0x00ffffff-no-rj")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def meme(ctx):
    url = f"https://meme-api.herokuapp.com/gimme"
    data = getInfo(url)

    memecap = data["title"]
    memeimg = data["preview"][2]
    getid = discord.Embed(title=memecap)
    getid.set_image(url=memeimg)
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


@nyx.command()
async def shorten(ctx, urles):
    s = pyshorteners.Shortener()
    shortenator = s.tinyurl.short(f"{urles}")
    getid = discord.Embed(title=f"Shortened URL: {urles}")
    getid.add_field(name=f"Original", value=f"{urles}")
    getid.add_field(name=f"Shortened", value=f"{shortenator}")
    getid.set_thumbnail(
        url=f"https://blog.hubspot.com/hs-fs/hubfs/Parts%20of%20a%20URL.png?width=650&name=Parts%20of%20a%20URL.png")
    getid.set_footer(text="Nyx", icon_url="https://i.ibb.co/Jz2wrk3/4866cf9f0e65da8b94f7eb687df08070.jpg")
    await ctx.send(embed=getid)


nyx.run("ODk0ODk5MTM5ODc4NDgxOTYw.YVwtxQ.BrVUJPhzwEwu6BMWlYi2lNY485U")
