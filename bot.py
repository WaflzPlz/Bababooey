import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
	print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="join", help="Makes Bot join your coice chat")
async def join(ctx):
	author = ctx.message.author
	channel = author.voice.channel
	vc = await channel.connect()

@bot.command(name="baba", help="Makes Bot play 'Bababooey'-sound effect")
async def play(ctx):
    guild = ctx.guild
    vc = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('soundfx/baba.mp3')
    if not vc.is_playing():
        vc.play(audio_source, after=None)

@bot.command(name="yankee", help="Makes Bot play 'Yankee with no brim'-sound effect")
async def play(ctx):
    guild = ctx.guild
    vc = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('soundfx/yankee_cut.mp3')
    if not vc.is_playing():
        vc.play(audio_source, after=None)

@bot.command(name="leave", help="Makes Bot leave the voice chat")
async def leave(ctx):
	guild = ctx.guild
	vc = discord.utils.get(bot.voice_clients, guild=guild)
	await vc.disconnect()

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if "-play" and "rockstar" in message.content:
		roast = f"get stick bugged! LOL {message.author.mention}\nposer"
		channel = message.channel
		await channel.send(roast)

	await bot.process_commands(message)

bot.run(TOKEN)