from asyncio.windows_events import NULL
import json
import os 
import random
from random import randrange
import datetime
import time
import urllib.request
import traceback
import discord
from mcstatus import MinecraftServer
from discord.utils import get
from discord.ext.commands import Bot
from dotenv import load_dotenv
import socket

start_time = time.time()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot_ava = "https://cdn.discordapp.com/avatars/780942434154184755/22e00d58a45d4ce8ae765f1508517361.png"

client = discord.Client()
bot = Bot(command_prefix=['!'])

@bot.event
async def on_voice_state_update(member, before, after):
    takenGuild = bot.get_guild(843707273087549450)
    f = open('voice_room.json', "r+", encoding="utf8")
    data = json.load(f)
    limit = 0
    key = ""
    if before.channel.id is not None :
        print(before.channel.id)
        if before.channel.id != 848383677670490172 :
            if len(before.channel.members) == 0 :
                for i in data :
                    for x in data[str(i)] :
                        print(before.channel.id)
                        x["limit"] = before.channel.user_limit     
                f.seek(0)
                json.dump(data, f, indent = 4, ensure_ascii=False)
                await before.channel.delete()
            else :
                print()
        else:
            print()
    f.close()

bot.run(TOKEN)
client.run(TOKEN)   