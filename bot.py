import discord
from discord.ext import commands
import os
# import youtube_dl
import yt_dlp as youtube_dl


TOKEN = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    if ctx.author.id == 360341725371170818:
        await ctx.send('Hello, can you stream tinder Kavin?')
    else:
        await ctx.send('Hello!')
 
@bot.command(name='ping')
async def ping(ctx):
    if ctx.author.id == 360341725371170818:
        await ctx.send('Pong, can you stream tinder Kavin?')
    else:
        await ctx.send('Pong!')

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

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict

@bot.command(name='play')
async def play(ctx, *, url: str):
    ffmpeg_path = os.popen("which ffmpeg").read().strip()

    if not ctx.voice_client:  # Bot is not in any voice channel
        await ctx.send("I'm not in a voice channel!")
        return

    if ctx.voice_client.is_playing():
        await ctx.send("Already playing audio!")
        return

    # We'll use get_video_info function to get the video details
    info = get_video_info(url)
    print("Video Info:", info)
    URL = info['formats'][0]['url']
    ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmeg", source=URL))

@bot.command(name='pause')
async def pause(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()

@bot.command(name='resume')
async def resume(ctx):
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()

bot.run(TOKEN)
