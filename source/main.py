import discord
from discord.ext import commands
from discord import DMChannel
import random
import time
import keep_alive
import webbrowser
import json
import os
from discord.utils import get
import praw
from discord.voice_client import VoiceClient
import time, datetime
from discord.ext.commands import Bot
from multiprocessing.connection import Client
from discord.ext.commands.cooldowns import BucketType
import platform
import asyncio
from discord import Intents


intents = Intents.all()
intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    channel = client.get_channel(850636097868267540)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.add_field(name = 'Make sure to follow AD Beats on Instagram', 
    value = f"[AD Beats on Instagram](https://instagram.com/ad._beats/ )", inline=False)
    embed.add_field(name = 'Make sure to subscribe AD Beats Youtube', 
    value = f"[AD Beats on Youtube](https://www.youtube.com/channel/UCiQ0pr5kNeO3tXMqyHChyaQ)", inline=False)
    embed.add_field(name = '----------', value = f'Make sure to check the <#849483485394501722>')

    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/844669094560530484/851371871793709096/1623053206445.jpg') # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)
    await member.send(embed = embed)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(851373898385850368)
    embed=discord.Embed(title=f"{member.name} just left :(", description=f"----- {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)




keep_alive.keep_alive()

client.run('')