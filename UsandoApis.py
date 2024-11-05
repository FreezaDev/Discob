import discord
import random
from discord.ext import commands
import asyncio
import os
import requests

timer = 0.0
running = False
eightballmsg = ["Yes, definetely", "YUH 🔥", "Most likely", "Who knows?",
"[CONFIDENTIAL]", "Nah", "HELL NAW 🔥", "nuh uh", "AUGUST 12 2036 - HEAT DEATH OF THE UNIVERSE"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def dox(ctx):
    await ctx.send("IP: 123.102.024")

@bot.command()
async def roll10(ctx):
    await ctx.send(random.randint(1,10))

@bot.command()
async def rolldice(ctx):
    await ctx.send(random.randint(1,6))

@bot.command()
async def eightball(ctx):
    await ctx.send(random.choice(eightballmsg))

@bot.command()
async def times(ctx):
    global running
    global timer
    if running:
        running = False
        await ctx.send(timer)
    else:
        running = True
        timer = 0.0

    while running:
        await asyncio.sleep(0.1)
        timer += 0.1


@bot.command()
async def mem1(ctx):
    with open('C:/Users/Franco/Documents/[PythonPro/Images/meme1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def mem2(ctx):
    with open('C:/Users/Franco/Documents/[PythonPro/Images/meme2.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def mem3(ctx):
    with open('C:/Users/Franco/Documents/[PythonPro/Images/meme3.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def memr(ctx):
    memes = os.listdir("C:/Users/Franco/Documents/[PythonPro/Images")
    with open(f"C:/Users/Franco/Documents/[PythonPro/Images/{random.choice(memes)}", 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    await ctx.send(file=picture)



def dogg():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]


@bot.command()
async def goofyahhdog(ctx):
    image_url = dogg()
    await ctx.send(image_url)





bot.run("Token")

