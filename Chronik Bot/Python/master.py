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
    embed = discord.Embed(title='NEW POST ALERT', discription="ChronikBot Post", color=0x00ff00)

    embed.set_author(name="Chronik N Coffee")
    embed.add_field(name='POST_LINK', value=None, inline=False)
    embed.set_image(url=scrape.steemPostImg())
    embed.set_footer(text=scrape.steemPostDesc())
    await ctx.send(embed=embed)


bot.run(config.token)
