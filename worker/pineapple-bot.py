# https://discordapp.com/oauth2/authorize?&client_id=354100308487569408&scope=bot&permissions=0

import asyncio
import discord
import os
import praw

from hackerrank.HackerRankAPI import HackerRankAPI
from strings import USER_AGENT, help_str, langs
from commands import *

### keys go here
reddit_client_id = os.environ.get("reddit_client_id")
reddit_client_secret = os.environ.get("reddit_client_secret")
hackerrank_key = os.environ.get("hackerrank_key")
discord_key = os.environ.get("discord_key")
giphy_key = os.environ.get("giphy_key")

# hello
client = discord.Client()
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=USER_AGENT)
reddit.read_only = True
compiler = HackerRankAPI(api_key=hackerrank_key)


async def send_response(channel, content):
    try:
        await client.send_message(channel, content)
    except Exception as e:
        print("ERROR: " + str(e))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='/help for commands'))


@client.event
async def on_message(message):
    if message.content.startswith('/help'):
        msg_content = help_str
        await send_response(message.channel, msg_content)

    elif message.content.startswith('/goodbot'):
        msg_content = "Thanks"
        await send_response(message.channel, msg_content)

    elif message.content.startswith('/foodporn'):
        msg_content = get_food_pic('foodporn', reddit)
        await send_response(message.channel, msg_content)

    elif message.content.startswith('/shittyfoodporn'):
        msg_content = get_food_pic('shittyfoodporn', reddit)
        await send_response(message.channel, msg_content)

    elif message.content.startswith('/randomfact'):
        msg_content = random_fact(reddit)
        await send_response(message.channel, msg_content)

    elif message.content.startswith('/gif'):
        search_term = ' '.join(message.content.split()[1:])
        msg_content = gif(search_term, giphy_key)
        await send_response(message.channel, msg_content)

    elif message.content.startswith('/congratulations'):
        msg_content = "https://www.youtube.com/watch?v=1Bix44C1EzY"
        await send_response(message.channel, msg_content)

    elif message.content.startswith("/compile"):
        msg_content = compile(message.content, compiler)
        await send_response(message.channel, msg_content)

    elif message.content.startswith("/languages"):
        msg_content = langs
        await send_response(message.channel, msg_content)

    elif message.content.startswith("/ohgod"):
        msg_content = "https://i.imgur.com/YD7iXwT.gif"
        await send_response(message.channel, msg_content)

client.run(discord_key)
