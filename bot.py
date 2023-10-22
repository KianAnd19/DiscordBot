import discord
from discord.ext import commands
import os
import youtube_dl

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



# Music Streaming
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@bot.command()
async def play(ctx, url):
    if not ctx.voice_client.is_connected():
        await ctx.author.voice.channel.connect()
    
    with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=URL))

@bot.command()
async def pause(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()

@bot.command()
async def resume(ctx):
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()


bot.run(TOKEN)
