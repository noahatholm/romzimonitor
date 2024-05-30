import discord
from discord.ext import commands
from discord.utils import get
import json
import os
import sys
from discord.ext.commands import CommandNotFound
import ctypes
import requests
import urllib

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW(f"Annoying Self Bot Thing By noah66")
client = discord.Client()
client = commands.Bot(command_prefix ='', help_command=None, self_bot=True)

PREFIX = ("!")
print("Command Prefix Is " + PREFIX)



username = 'imgflip username'
password = 'imgflip password'
romid = "discord userid"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

#Take input from user -- Meme, Text0 and Text1

global status
status = "on"




#Checks for the Config File
try:
    file = open("config.json")
    json_dictionary = json.load(file)
    file.close()
except:
    data_set = {"Token": "None", "TargetID": "None"}
    with open('config.json', 'w') as outfile:
        json.dump(data_set, outfile, indent=2)
    file = open("config.json")
    json_dictionary = json.load(file)

@client.event
async def on_message(ctx):
    if str(ctx.author.id) == str(target):
        user = await client.fetch_user(int(target))
        async for message in ctx.channel.history(limit=1):
            text0 = message.content
        URL = 'https://api.imgflip.com/caption_image'
        print(text0)
        params = {
            'username':username,
            'password':password,
            'template_id':romid,
            'text0':text0,
            'text1':" "
        }
        response = requests.request('POST',URL,params=params).json()
        print(response)
        data = response['data']
        data = data['url']
        if status == "on":
            await ctx.channel.send(data)





@client.command()
async def ping(ctx):
    print("\u001b[33mExecuted Ping\u001b[37m")
    await ctx.message.delete()
    messages = await ctx.send(f'Pong! {round(client.latency * 1000)}ms :ping_pong:')
    await asyncio.sleep(int(timer))
    await messages.delete()


@client.command()
async def restart(ctx):
    await ctx.message.delete()
    message = await ctx.send("Restarting... Allow up to 5 seconds")
    restart_program()


@client.event
async def on_ready():
    print('\u001b[32mWe have logged in as {0.user}'.format(client)+ "\u001b[37m")
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["Token"] = Token
    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent = 2)
    user = await client.fetch_user(target)
    displayname = user.display_name
    discrim = user.discriminator
    print(f"\u001b[32mAnnoying {str(displayname)}#{str(discrim)} \u001b[37m")


file = open("config.json")
json_dictionary = json.load(file)
file.close()
target = (json_dictionary["TargetID"])
if target == "None":
    target = input("Please Enter Target \n")
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["TargetID"] = target
    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent = 2)

Token = (json_dictionary["Token"])

if Token == "None":
    Token = input("Please Enter You Token \n")
try:
    client.run(Token, bot=False)
except:
    print("\u001b[31mInvalid Token \nPlease Restart The Program\u001b[37m")
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["Token"] = "None"
    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent = 2)
