import discord
from discord.ext import commands
import os
from discord.ext import commands

TOKEN = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)
