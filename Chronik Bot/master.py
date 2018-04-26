#Chronik Bot by 2toetommy
import config
import logging
import discord
import scrape
from discord.ext import commands


#Logs errors if any then prints
logging.basicConfig(level=logging.INFO)

description = 'Chronik Bot by 2toetommy'
bot = commands.Bot(command_prefix='!!', description=description)
url = 'https://steemit.com/@chronik-n-coffee'

@bot.event #on load
async def on_ready():
    print('Logged in as ')
    print(bot.user.name)
    print(bot.user.id)
    print(f'discord.py v{discord.__version__}')




@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.say("{} loaded.".format(extension_name))


@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.say("{} unloaded.".format(extension_name))

#commands

@bot.command()
async def post(ctx):
    embed = discord.Embed(title=scrape.steemPostTitle(), discription="ChronikBot Post", color=0x00ff00)
    embed.set_author(name="NEW POST")
    embed.set_image(url=scrape.steemPostImg())
    embed.add_field(name='___', value=scrape.steemPostDesc(), inline=False)
    ctx.send(embed=embed)


        


@bot.event
async def on_member_join(ctx, member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await bot.send_message(server, fmt.format(member, server))
bot.run(config.token)
