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
from pprint import pprint
from scrape import steemPost



from discord.ext import commands
from discord.ext.commands import Bot

#Logs errors if any then prints
logging.basicConfig(level=logging.INFO)


client = discord.Client()
url = 'https://steemit.com/@chronik-n-coffee'

@client.event #on load
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('__________')

#webhooks

#webhook end

#commands

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!!ping'):
        await client.send_message(message.channel, ':ping_pong: PONG')
    elif message.content.startswith('!!post'):
        await client.send_message(message.channel, 'COMING SOON')
        embed = discord.Embed(
            title='Test',
            color='white',
            description=''
        )
        await client.send_message(message.channel, embed=embed)




    elif message.content.startswith('!!clear'):
        await client.send_message(message.channel, '')

        


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
client.run("NDMxMTkyODE2NDcxNzY5MTI4.Dbpjzg.3IB29fwPLzDHTAqaZy9330_Hq8o")
