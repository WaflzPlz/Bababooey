import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

class Baba_Client(discord.Client):
	async def on_ready(self):
		print(f"{self.user} has connected to Discord!")

	async def on_member_join(self, member):
		await member.create_dm()
		await member.dm_channel.send(
			f"Hi {member.name}, welcome to my Discord server!"
		)

	async def on_error(self, event, *args, **kwargs):
		with open("err.log", "a") as f:
			if event == "on_message":
				f.write(f"Unhandled message: {args[0]}\n")

			else:
				raise

	async def on_message(self, message):
		if message.author == client.user:
			return

		brooklyn_99_quotes = [
			"I'm the human form of the 💯 emoji",
			"Bingpot!",
			(
				"Cool. Cool cool cool cool cool cool cool,"
				"no doubt no doubt no doubt no doubt."
			),
		]

		if message.content == "99!":
			response = random.choice(brooklyn_99_quotes)
			await message.channel.send(response)

		elif message.content == "raise-exception":
			raise discord.DiscordException


client = Baba_Client()
client.run(TOKEN)