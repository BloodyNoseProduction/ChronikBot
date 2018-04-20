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

import aiohttp
import discord
from discord.object import webhooks
from discord.ext import commands
from discord.ext.commands import Bot

#Logs errors if any then prints
logging.basicConfig(level=logging.INFO)


client = discord.Client()

@client.event #on load
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('__________')

#webhooks

#async def foo():
    #async with aiohttp.ClientSession() as session:
        #webhook = Webhook.from_url('http://feeds.feedburner.com/feedburner/2toe', adapter=AsyncWebhookAdapter(session))
        #await webhook.send('RSS' , username='Foo')


#webhook end

#commands

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!!ping'):
        await client.send_message(message.channel, ':ping_pong: PONG')
    elif message.content.startswith('!!post'):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('http://feeds.feedburner.com/feedburner/2toe', adapter=AsyncWebhookAdapter(session))
            await webhook.send('RSS' , username='Foo')
            await client.send_message(message.channel, 'COMING SOON')
        embed = discord.Embed(title="", description="", color=0x00ff00)
        embed.add_field(name="New Post", value="https://steemit.com/chronikncoffee/@chronik-n-coffee/new-brew-tonight-with-chronikncoffee-live-on-msp-waves-radio", inline=False)
        embed.set_thumbnail(url="https://steemitimages.com/DQmQqDJGKB1Pr7KipQgs4quBU5WRRpUpa7HsNWQWeXpRFY1/CNC.jpg")
        await client.send_message(message.channel, embed=embed)


    elif message.content.startswith('!!clear'):
        await client.send_message(message.channel, '')

        


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
client.run("NDMxMTkyODE2NDcxNzY5MTI4.Dbpjzg.3IB29fwPLzDHTAqaZy9330_Hq8o")
