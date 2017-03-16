import discord
from discord.ext import commands
import steamapi as steam
import bot_tools as tools

bot = commands.Bot(command_prefix=commands.when_mentioned_or("*"), description="An online gaming status checker")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(*args):
    await bot.say("Hello, world!")

@bot.command()
async def yes(*args):
	await bot.say("YES, YES, YES!")

@bot.command()
async def hey(*args):
	await bot.say("something")

# @bot.event
# async def on_message(message):
#     if message.content.startswith('$greet'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         await bot.send_message(message.channel, msg)

bot.run(tools.get_key())