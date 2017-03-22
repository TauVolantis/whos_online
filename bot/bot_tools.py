from os.path import isfile, isdir, join, getsize
import json
import inspect

BKEY_FOLDER = "keys/"
BOT_NAME = "whos_online"
API_KEY_FILE = "steamapi"
HELP_JSON = 'help.json'
USERS_JSON = 'steamusers.json'

def get_key(option):
	"""
	Returns the bot key stored in a file under BKEY_FOLDER/<name>.key
	"""
	try:
		file_name = API_KEY_FILE if option == "steam" else BOT_NAME
		with open(join("../" + BKEY_FOLDER, "{}.key".format(file_name)), 'r') as file:
			return file.readline().strip()
	except Exception:
		raise IOError("Error occured while trying to get Bot Key")
	return False

def get_help():
	"""
	Returns a help message based on the function that calls get_help
	Retrieves 
	"""
	try:
		with open(HELP_JSON) as json_file:
			data = json.load(json_file)
			return data[inspect.stack()[1][3]]
	except Exception as e:
		print(e)

def store_user(steamname, steamid, discorduser=""):
	"""
	Stores a given user data in a json file for later reference
	Binds Steam username to steamid
	Optionally binds a discord user to steam username
	TODO: possibly make it so that a discord user can only be bound
	to one steam user
	TODO: discord name is not bound as a hash, needs to be updated 
	to store a string
	"""
	try:
		data = { steamname : [steamid, discorduser] }
		if isfile(USERS_JSON) and getsize(USERS_JSON) > 0:
			with open(USERS_JSON, 'r+') as out_file:
				file_data = json.load(out_file)
				file_data.update(data)
				out_file.seek(0)
				out_file.truncate()
				out_file.write(json.dumps(file_data))
		else:
			with open(USERS_JSON, 'w') as out_file:
				json.dump(data, out_file)
	except Exception as e:
		print(e)

def remove_user(username, steamid, discorduser=""):
	"""
	Removes a given user from the steam users json file
	"""
	pass

def user_exists(steamname):
	"""
	Returns true if a user is already in the steam users json, false otherwise
	Based on a search of a user's steam name
	"""
	try:
		with open(USERS_JSON) as file:
			file_data = json.load(file)
			return steamname in file_data.keys()
	except Exception as e:
		print(e)
		return False