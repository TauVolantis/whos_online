from os.path import isfile, isdir, join

BKEY_FOLDER = "keys/"
BOT_NAME = "whos_online"

def get_key():
	"""
	Returns the bot key stored in a file under BKEY_FOLDER/<name>.key
	"""
	try:
		with open(join("../" + BKEY_FOLDER, "{}.key".format(BOT_NAME)), 'r') as file:
			return file.readline().strip()
	except Exception:
		raise IOError("Error occured while trying to get Bot Key")
	return False