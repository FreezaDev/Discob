import discord
import random
from discord.ext import commands
import asyncio

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


bot.run("Token")
