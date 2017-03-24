import sys
import time
from subprocess import Popen, PIPE, call
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

"""
This is a script for automatically rerunning the bot script whenever a
code change is made.
"""

class ChangeHandler(PatternMatchingEventHandler):
	patterns = ["*.py"]

	def process(self, event):
		"""
		Runs the discord bot.run command when called
		"""
		print(event.src_path, event.event_type)
		pipe = Popen('ps ax | grep whosonline', shell=True, stdout=PIPE).stdout
		output = pipe.readlines()[0].decode("utf-8")
		if "/bot/whosonline.py" in output:
			call([ 'kill', output.split(" ")[0] ]) 
		Popen(['python3', '../bot/whosonline.py'])

	def on_any_event(self, event):
		self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(ChangeHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()