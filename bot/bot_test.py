import discord
from discord.ext.commands import Bot
import logging

bot = Bot(command_prefix="!")
logger = logging.getLogger('discord')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")

@bot.command()
	async def yes(*args):
	return await bot.say("YES, YES, YES!")

bot.run('token')