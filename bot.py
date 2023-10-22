import discord
from discord.ext import commands
import os
import youtube_dl
import yt_dlp as ydlp

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
@bot.command(name='join')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name='leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()

def get_video_info(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with ydlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict


@bot.command(name='play')
async def play(ctx, url):
    if not ctx.voice_client.is_connected():
        await ctx.author.voice.channel.connect()

    # We'll use get_video_info function to get the video details
    info = get_video_info(url)
    URL = info['formats'][0]['url']
    ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=URL))

@bot.command(name='pause')
async def pause(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()

@bot.command(name='resume')
async def resume(ctx):
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()


bot.run(TOKEN)
