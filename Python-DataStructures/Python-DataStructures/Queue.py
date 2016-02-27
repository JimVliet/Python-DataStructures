class Queue:
	def __init__ (self):
		self.firstInList = None
		self.lastInList = None
		self.size = 0


	def append(self, object):
		newItem = QueueItem(object, None)
		self.size += 1
		if self.firstInList is None:
			self.firstInList = newItem
			return

		if self.lastInList is None:
			self.firstInList.updateNext(newItem)
			self.lastInList = newItem
			return

		self.lastInList.updateNext(newItem)
		self.lastInList = newItem

	def extend(self, objectList):
		for object in objectList:
			self.size += 1
			newItem = QueueItem(object, None)

			if self.firstInList is None:
				self.firstInList = newItem
				continue

			if self.lastInList is None:
				self.firstInList.updateNext(newItem)
				self.lastInList = newItem
				continue

			self.lastInList.updateNext(newItem)
			self.lastInList = newItem


	def isEmpty(self):
		return self.firstInList is None

	def pop(self):
		if self.firstInList is None:
			raise IndexError
		self.size -= 1
		var = self.firstInList.object
		self.firstInList = self.firstInList.next
		return var

class QueueItem:
	def __init__(self, object, nextQueueObject):
		self.object = object
		self.next = nextQueueObject

	def updateNext(self, nextQueueObject):
		self.next = nextQueueObject