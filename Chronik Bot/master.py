#Chronik Bot by 2toetommy
import asyncio
import datetime
import json
import logging
import os
import random
import sys
import weakref
from email.utils import parsedate_to_datetime
import dhook
from dhook import Webhook
import aiohttp
import discord
from discord.ext import commands
from pprint import pprint
import scrape



from discord.ext import commands
from discord.ext.commands import Bot

#Logs errors if any then prints

description = 'Chronik Bot by 2toetommy'
logging.basicConfig(level=logging.INFO)


bot = commands.Bot(command_prefix='!!', description=description)
url = 'https://steemit.com/@chronik-n-coffee'

@bot.event #on load
async def on_ready():
    print('Logged in as ')
    print(bot.user.name)
    print(bot.user.id)
    print('__________')


#commands

@bot.command()
async def post():
    await bot.say(scrape.steemPostTitle())

    embed = discord.Embed(title=scrape.steemPostTitle(), discription="ChronikBot Post", color=0x00ff00)
    embed.set_author(name="NEW POST")
    embed.set_image(url=scrape.steemPostImg())
    embed.add_field(name='___', value=scrape.steemPostDesc(), inline=False)
    await bot.say(embed=embed)


        


@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await bot.send_message(server, fmt.format(member, server))
bot.run("YOUR_TOKEN")
