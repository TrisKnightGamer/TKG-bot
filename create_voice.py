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
    category = get(takenGuild.categories, name = "Kênh đàm thoại")
    channel = None
    if before.channel is None and after.channel is not None :
        if after.channel.id == 848383677670490172 and not member.bot:

            with open("voice_room.json", "r+", encoding='utf8') as file:
                data = json.load(file)
                for i in data :
                    for x in data[str(i)]:
                        if i == member.id:
                            limit = x["limit"]
                            overwrites = {}
                            if x["lock"] == True:
                                overwrites = {
                                    takenGuild.default_role: discord.PermissionOverwrite(read_messages=False),
                                    takenGuild.me: discord.PermissionOverwrite(read_messages=True)
                                }
                            elif x["lock"] == False:
                                overwrites = {
                                    takenGuild.default_role: discord.PermissionOverwrite(read_messages=True),
                                    takenGuild.me: discord.PermissionOverwrite(read_messages=True)
                                }
                            channel_name = x["channel_name"]
                            room = await takenGuild.create_voice_channel(channel_name,category=category, user_limit=limit, overwrites=overwrites )
                            channel = {str(member.id): [ { "username" : member.display_name, "channel_name" : room.name, "channel_id" : room.id, "limit": room.user_limit, "lock" : x["lock"], "hidden": False} ] }
                            data.update(channel)
                            file.seek(0)
                            json.dump(data, file, indent = 4, ensure_ascii=False)
                            await member.move_to(room)
                            return

                room = await takenGuild.create_voice_channel(member.display_name,category=category)
                channel = {str(member.id): [ { "username" : member.display_name, "channel_name" : room.name, "channel_id" : room.id, "limit": room.user_limit, "lock" : False, "hidden": False} ] }
                data.update(channel)
                file.seek(0)
                json.dump(data, file, indent = 4, ensure_ascii=False)
                await member.move_to(room)
                
        else:
            print("")
    else:
        print("")

bot.run(TOKEN)
client.run(TOKEN)