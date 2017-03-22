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
async def yes(*args):
	await bot.say("YES, YES, YES!")

# @bot.command()
# async def help(*args):
# 	pass

@bot.command()
async def adduser(*args):
	"""
	Add the given steam user to the roster
	Optional: bind a discord user to the steam user
	TODO: add a message indicating a user bound a discord name to steam name
	in the event that a steam user is already registered
	"""
	try:
		arg_length = len(args)
		if(arg_length == 0 or arg_length > 2 or args[0].lower() == "help"):
			return await bot.say(tools.get_help())

		steam.core.APIConnection(api_key=tools.get_key("steam"), validate_key=True)
		person = steam.user.SteamUser(int(args[0]))
		discordname = args[1] if arg_length > 1 else ""

		# the storage function is called every time to handle the case
		# where a user tries to store a discord name with an already stored
		# steam user
		tools.store_user(person.name, args[0], discordname)

		if tools.user_exists(person.name):
			await bot.say("Steam user already registered!")
		else:
			await bot.say(person.name + " has been added!")
	except Exception as e:
		print(e)
		await bot.say("Steam id number required!")

@bot.command()
async def removeuser(*args):
	"""
	Remove the given steam user from the roster
	"""
	pass

@bot.command()
async def getname(*args):
	"""
	Returns the Steam name of the given user (by id or discord username perhaps)
	"""
	pass

@bot.command()
async def steamid(*args):
	"""
	Returns the id of the given user
	"""
	pass

@bot.command()
async def playing(*args):
	"""
	Returns the current game that the given user is playing
	"""
	pass

@bot.command()
async def status(*args):
	"""
	Returns the online status of the given user
	"""
	pass

@bot.command()
async def friends(*args):
	"""
	Returns a list of the given user's friends
	"""
	pass

@bot.command()
async def level(*args):
	"""
	Returns the given user's level
	"""
	pass

@bot.command()
async def games(*args):
	"""
	Returns the given user's list of games
	"""
	pass

@bot.command()
async def owned(*args):
	"""
	Returns a boolean representing the given user owns a given game
	"""
	pass

@bot.command()
async def avatar(*args):
	"""
	Returns the profile picture of the given user
	"""
	pass

@bot.command()
async def when_created(*args):
	"""
	Returns the date of when the given user created their steam profile
	"""
	pass

@bot.command()
async def xp(*args):
	"""
	Returns the ammount of experience the given user has accrued on steam
	"""
	pass

@bot.command()
async def last_logoff(*args):
	"""
	Returns the last time the given user was online
	"""
	pass

bot.run(tools.get_key("bot"))