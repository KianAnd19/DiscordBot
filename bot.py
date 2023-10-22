import discord
import os
from discord.ext import commands

TOKEN = 'MTE2NTYzNzYxMzIzMTgyMDgxMA.GKvZ6N.w2o8hrFZPs_1IEkiNOXjlOrw3Ch_iVVv71q9lE'
TOKEN = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

bot.run(TOKEN)
