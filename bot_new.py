import os
import random
from dotenv import load_dotenv

# 1
import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 2
bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
	print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="join")
async def join(ctx):
	author = ctx.message.author
	channel = author.voice.channel
	vc = await channel.connect()

@bot.command(name="play")
async def play(ctx):
    guild = ctx.guild
    vc = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('baba.mp3')
    if not vc.is_playing():
        vc.play(audio_source, after=None)

@bot.command(name="leave")
async def leave(ctx):
	guild = ctx.guild
	vc = discord.utils.get(bot.voice_clients, guild=guild)
	await vc.disconnect()

@bot.command(name="99!", help="Responds with a random quote from Brookly 99")
async def nine_nine(ctx):
	brooklyn_99_quotes = [
		"I'm the human form of the 💯 emoji",
		"Bingpot!",
		(
			"Cool. Cool cool cool cool cool cool cool,"
			"no doubt no doubt no doubt no doubt."
		),
	]

	response = random.choice(brooklyn_99_quotes)
	await ctx.send(response)

@bot.command(name="roll_dice", help="Simulates rolling dice")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(", ".join(dice))

bot.run(TOKEN)