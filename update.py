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
bot.remove_command("help")

@bot.event
async def on_disconnect():
    takenGuild = bot.get_guild(843707273087549450)
    channel = takenGuild.text_channels
    nameChannel = None
    for x in channel:
        
        if x.name == "cập-nhật-thông-tin-server":
            nameChannel = x
            break

    A_mgs = [] #Empty list to put all the messages in the log
    async for x in nameChannel.history(limit = 100):
        A_mgs.append(x)
    await nameChannel.delete_messages(A_mgs)

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]
    msg = ""
    status = None
    statusNgrok_str = None
    statusServer_str = None
    players = 0
    latency = 0
    res = 0

    try :
        res = urllib.request.urlopen("http://localhost:4040/status").getcode()
    except :
        res = 0

    if res == 200:

        os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

        with open('tunnels.json') as data_file:    
            datajson = json.load(data_file)

        msg_spilt = []
        for i in datajson['tunnels']:
            if(str(i['name']) == "minefc"):
                msg = msg + i['public_url']
                msg = msg.replace("tcp://","")
        msg_spilt = msg.split(":")
        msg = "IP hiện tại của server : " + msg
        try :
            server = MinecraftServer(msg_spilt[0], int(msg_spilt[1]))
            status = server.status()
            players = status.players.online
            latency = status.latency
            
            statusServer_str = "<:greendot:844047684955799572> đang hoạt động"
            statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
        except:
            statusServer_str = "<:reddot:844050179845652530> đã dừng"
            statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
    else :
        statusServer_str = "<:reddot:844050179845652530> đã dừng"
        statusNgrok_str = "<:reddot:844050179845652530> đã dừng"

    embed = discord.Embed(title=f"{msg}", description=f"Tình trạng Server Minecraft: {statusServer_str}\n>>>Hiện tại đang có {players}/174 người chơi đang online.\n>>>Ping : {latency} ms\nTình trạng Ngrok: {statusNgrok_str}\nTự động cập nhật sau mỗi 10s.\nNgoài ra bot còn nhiều lệnh khác, nhập !help để biết thêm chi tiết!", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)
    
    embed = await nameChannel.send(embed=embed)

@bot.event
async def on_error(event, *args, **kwargs):
    takenGuild = bot.get_guild(843707273087549450)
    channel = takenGuild.text_channels

    nameChannel = None
    for x in channel:
        
        if x.name == "cập-nhật-thông-tin-server":
            nameChannel = x
            break

    A_mgs = [] #Empty list to put all the messages in the log
    async for x in nameChannel.history(limit = 100):
        A_mgs.append(x)
    await nameChannel.delete_messages(A_mgs)

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]
    msg = ""
    status = None
    statusNgrok_str = None
    statusServer_str = None
    players = 0
    latency = 0
    res = 0

    try :
        res = urllib.request.urlopen("http://localhost:4040/status").getcode()
    except :
        res = 0

    if res == 200:

        os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

        with open('tunnels.json') as data_file:    
            datajson = json.load(data_file)

        msg_spilt = []
        for i in datajson['tunnels']:
            if(str(i['name']) == "minefc"):
                msg = msg + i['public_url']
                msg = msg.replace("tcp://","")
        msg_spilt = msg.split(":")
        msg = "IP hiện tại của server : " + msg
        try :
            server = MinecraftServer(msg_spilt[0], int(msg_spilt[1]))
            status = server.status()
            players = status.players.online
            latency = status.latency
            
            statusServer_str = "<:greendot:844047684955799572> đang hoạt động"
            statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
        except:
            statusServer_str = "<:reddot:844050179845652530> đã dừng"
            statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
    else :
        statusServer_str = "<:reddot:844050179845652530> đã dừng"
        statusNgrok_str = "<:reddot:844050179845652530> đã dừng"

    embed = discord.Embed(title=f"{msg}", description=f"Tình trạng Server Minecraft: {statusServer_str}\n>>>Hiện tại đang có {players}/174 người chơi đang online.\n>>>Ping : {latency} ms\nTình trạng Ngrok: {statusNgrok_str}\nTự động cập nhật sau mỗi 10s.\nNgoài ra bot còn nhiều lệnh khác, nhập !help để biết thêm chi tiết!", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)
    
    embed = await nameChannel.send(embed=embed)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await autoUpdate(bot)

async def autoUpdate(bot):

    start = time.time()

    takenGuild = bot.get_guild(843707273087549450)
    channel = takenGuild.text_channels

    nameChannel = None
    for x in channel:
        
        if x.name == "cập-nhật-thông-tin-server":
            nameChannel = x
            break

    A_mgs = [] #Empty list to put all the messages in the log
    async for x in nameChannel.history(limit = 100):
        A_mgs.append(x)
    await nameChannel.delete_messages(A_mgs)

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]
    msg = ""
    status = None
    statusNgrok_str = None
    statusServer_str = None
    players = 0
    latency = 0
    res = 0

    try :
        res = urllib.request.urlopen("http://localhost:4040/status").getcode()
    except :
        res = 0

    if res == 200:

        os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

        with open('tunnels.json') as data_file:    
            datajson = json.load(data_file)

        msg_spilt = []
        for i in datajson['tunnels']:
            if(str(i['name']) == "minefc"):
                msg = msg + i['public_url']
                msg = msg.replace("tcp://","")
        msg_spilt = msg.split(":")
        msg = "IP hiện tại của server : " + msg
        try :
            server = MinecraftServer(msg_spilt[0], int(msg_spilt[1]))
            status = server.status()
            players = status.players.online
            latency = status.latency
            
            statusServer_str = "<:greendot:844047684955799572> đang hoạt động"
            statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
        except:
            statusServer_str = "<:reddot:844050179845652530> đã dừng"
            statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
    else :
        statusServer_str = "<:reddot:844050179845652530> đã dừng"
        statusNgrok_str = "<:reddot:844050179845652530> đã dừng"

    embed = discord.Embed(title=f"{msg}", description=f"Tình trạng Server Minecraft: {statusServer_str}\n>>>Hiện tại đang có {players}/174 người chơi đang online.\n>>>Ping : {latency} ms\nTình trạng Ngrok: {statusNgrok_str}\nTự động cập nhật sau mỗi 10s.\nNgoài ra bot còn nhiều lệnh khác, nhập !help để biết thêm chi tiết!", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)
    
    embed = await nameChannel.send(embed=embed)
    old_embed = embed

    end = time.time()

    print(f"[INFO] Takes {end - start} seconds to start up bot")

    while True :
        time.sleep(10)
        msg = ""
        status = None
        statusNgrok_str = None
        statusServer_str = None
        players = 0
        latency = 0
        res = 0
        date_time_now = datetime.datetime.now()
        date_time_now = str(date_time_now)
        date_time_now =  date_time_now[:19] + date_time_now[26:]
        try :
            res = urllib.request.urlopen("http://localhost:4040/status").getcode()
        except :
            res = 0
        if res == 200:

            os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

            with open('tunnels.json') as data_file:    
                datajson = json.load(data_file)

            msg_spilt = []
            for i in datajson['tunnels']:
                if(str(i['name']) == "minefc"):
                    msg = msg + i['public_url']
                    msg = msg.replace("tcp://","")
            msg_spilt = msg.split(":")
            msg = "IP hiện tại của server : " + msg
            try :
                server = MinecraftServer(msg_spilt[0], int(msg_spilt[1]))
                status = server.status()
                players = status.players.online
                latency = status.latency
                
                statusServer_str = "<:greendot:844047684955799572> đang hoạt động"
                statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
            except:
                statusServer_str = "<:reddot:844050179845652530> đã dừng"
                statusNgrok_str = "<:greendot:844047684955799572> đang hoạt động"
        else :
            statusServer_str = "<:reddot:844050179845652530> đã dừng"
            statusNgrok_str = "<:reddot:844050179845652530> đã dừng"
        embed = discord.Embed(title=f"{msg}", description=f"Tình trạng Server Minecraft: {statusServer_str}\n>>>Hiện tại đang có {players}/174 người chơi đang online.\n>>>Ping : {latency} ms\nTình trạng Ngrok: {statusNgrok_str}\nTự động cập nhật sau mỗi 10s.\nNgoài ra bot còn nhiều lệnh khác, nhập thelp để biết thêm chi tiết!", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)
        
        await old_embed.edit(embed=embed)

bot.run(TOKEN)
client.run(TOKEN)