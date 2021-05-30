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
@bot.command(name='lock')
async def lock(ctx):
    f = open('voice_room.json', "r+", encoding="utf8")
    data = json.load(f)
    for i in data :
        for x in data[str(i)] :
            if ctx.message.author.id == i  :
                x["lock"] = True
                f.seek(0)
                print(data)
                json.dump(data, f, indent = 4, ensure_ascii=False)
                f.close()
    

@bot.command(name='unlock')
async def unlock(ctx):
    f = open('voice_room.json', "r+", encoding="utf8")
    data = json.load(f)
    for i in data :
        for x in data[str(i)] :
            if ctx.message.author.id == i  :
                x["lock"] = False
    f.seek(0)
    json.dump(data, f, indent = 4, ensure_ascii=False)
    f.close()

@bot.command(name='ava')
async def ava(ctx, avamember : discord.Member):

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    try :
        author = ctx.message.author
        get_ava = [
            'Đây là avatar của'
        ]

        response = random.choice(get_ava)

        userAvatarUrl = avamember.avatar_url

        embed = discord.Embed(description=f"{response} {avamember}", color=0x00ff00)
        embed.set_image(url=userAvatarUrl)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)
    except:
        author = ctx.message.author
        get_ava = [
            'Đây là avatar của'
        ]

        response = random.choice(get_ava)

        userAvatarUrl = author.avatar_url
        
        embed = discord.Embed(description=f"{response} {avamember}", color=0x00ff00)
        embed.set_image(url=userAvatarUrl)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

@bot.command(name='avatar')
async def avatar(ctx, avamember : discord.Member):
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    try :
        author = ctx.message.author
        get_ava = [
            'Đây là avatar của'
        ]

        response = random.choice(get_ava)

        userAvatarUrl = avamember.avatar_url

        embed = discord.Embed(description=f"{response} {avamember}", color=0x00ff00)
        embed.set_image(url=userAvatarUrl)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)
    except:
        author = ctx.message.author
        get_ava = [
            'Đây là avatar của'
        ]

        response = random.choice(get_ava)

        userAvatarUrl = author.avatar_url
        
        embed = discord.Embed(description=f"{response} {avamember}", color=0x00ff00)
        embed.set_image(url=userAvatarUrl)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        #print(embed=embed) 
        
        await ctx.send(embed=embed)

@bot.command(name='info')
async def info(ctx):

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    author = ctx.message.author

    embed = discord.Embed(description=f"Đây là thông tin của {avamember}", color=0x00ff00)
    
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

    await ctx.send(embed=embed)

@bot.command(name='role')
async def role_help(ctx):
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]
    
    author = ctx.message.author
    pick_role = [
        ' bạn ơi, có thể nhận role DJ bằng cách nhập `tpickrole DJ` '
    ]

    response = random.choice(pick_role)

    embed = discord.Embed(description=f"{author.mention} {response}", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

    await ctx.send(embed=embed)

@bot.command(name='pickrole')
async def pickrole(ctx, context):
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    if context.find('DJ') != -1:
        author = ctx.message.author
        role = get(ctx.message.guild.roles, name='DJ')
        pick_role = [
            'đã được thêm role'
        ]

        response = random.choice(pick_role)
        await author.add_roles(role)

        embed = discord.Embed(description=f"{author.mention} {response} {role}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

@bot.command(name='pick')
async def pick(ctx, *args):  
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    try :
        substrings = []
        string = ' '.join(args)
        substrings = string.split(',')

        response = random.choice(substrings)

        embed = discord.Embed(description=f"Mình chọn {response}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(description=f"Để xài lệnh `pick` bạn hãy nhập `!pick <vế 1>, <vế 2>, <vế 3>, ...`.\nLưu ý: trong các vế không được có khoảng trống", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

@bot.command(name='caculate')
async def caculate(ctx, *args):
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    string = ' '.join(args)
    print(string)

    if string.find('x') != -1 :
        substrings = string.split('x')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])

            results = results*int(tmp)
            print(results)

        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)
                

    elif  string.find('*') != -1 :
        substrings = string.split('*')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results*int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    elif  string.find('/') != -1 :
        substrings = string.split('/')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    elif  string.find('+') != -1 : 
        substrings = string.split('+')
        results = 0
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results+int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    elif  string.find('-') != -1 :
        substrings = string.split('-')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

@bot.command(name='cal')
async def cal(ctx, *args):
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    string = ' '.join(args)
    print(string)

    if string.find('x') != -1 :
        substrings = string.split('x')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])

            results = results*int(tmp)
            print(results)

        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)
                

    elif  string.find('*') != -1 :
        substrings = string.split('*')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results*int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    elif  string.find('/') != -1 :
        substrings = string.split('/')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    elif  string.find('+') != -1 : 
        substrings = string.split('+')
        results = 0
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results+int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    elif  string.find('-') != -1 :
        substrings = string.split('-')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

@bot.command(name='ship')
async def ship(ctx, arg1, arg2):

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    if arg2 == None or arg1 == None :
        embed = discord.Embed(description=f"!ship chỉ có thể ship được 2 bạn với nhau", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

    else:
        percent = random.randint(1,100)

        embed = discord.Embed(description=f"Tỉ lệ tình yêu giữa 2 bạn {arg1} và {arg2} là : {percent}%", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

        await ctx.send(embed=embed)

@bot.command(name='ping')
async def ping(ctx):

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    embed = discord.Embed(description=f"Ping của mình là : {round(bot.latency*1000)}ms", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

    await ctx.send(embed=embed)

@bot.command(name='uptime')
async def timeup(ctx):

    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    current_time = time.time()
    up_time = int(round(current_time - start_time))
    up_time = datetime.timedelta(seconds=up_time)

    embed = discord.Embed(description=f"Mình đã hoạt động được {up_time}", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

    await ctx.send(embed=embed)

@bot.command(name='help')
async def help(ctx):
    
    date_time_now = datetime.datetime.now()
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    embed = discord.Embed(description=f"Prefix của mình là `!`.\nBạn hãy nhập `!pickrole DJ` để được nhận role DJ nhé.\nBạn có thể xem avatar của người khác bằng cách nhập `!ava !user#id_user` hoặc `!avatar !user#id_user`.\nNgoài ra còn một số lệnh như là : `pick`,  `caculate` hoặc `cal`,  `ship`, `ping`, `uptime`.", color=0x00ff00)
    embed.set_footer(text=f" Made by TKG - {date_time_now} - Theo múi giờ UTC+7 của Đông Lào", icon_url=bot_ava)

    await ctx.send(embed=embed)
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Đông Lào là nhất."))

bot.run(TOKEN)
client.run(TOKEN)