from abc import ABC, abstractmethod

class RecordObject(ABC):
	
	@abstractmethod
	def record(self, signal):
		pass
	
class ChildObject(ABC):
	
	@abstractmethod
	def registerinstance(self, childobject: RecordObject):
		pass
