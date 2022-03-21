import glob
import os
import re
from abstractmodels import ChildObject, RecordObject


class Find(ChildObject):
	
	def __init__(self):
		self.events = []
	
	def registerinstance(self, event: ChildObject):
		self.events.append(event)
		
	def notifyevent(self, event):
		for items in self.events:
			items.record(event)
		
	def grep(self, filepath: str, pattern: str):
		pat = re.compile(pattern)
		for files in glob.glob(filepath, recursive=True):
			if os.path.isfile(files):
				try:
					with open(files) as w:
						self.notifyevent(("file opened", files))
						if pat.findall(w.read()):
							self.notifyevent(("match found", files))
				finally:
					self.notifyevent(("files closed", files))
			else:
				continue
				
	
class Presenter(RecordObject):
	def record(self, event):
		event_type, file = event
		if event_type == "match found":
			print(f"Found in: {file}")


if __name__ == '__main__':
	import sys
	if len(sys.argv) > 2:
		f = Find()
		f.registerinstance(Presenter())
		f.grep(sys.argv[1], sys.argv[2])
	else:
		print("Too few Arguments")
