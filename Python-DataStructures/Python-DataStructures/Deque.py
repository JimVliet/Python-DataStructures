class Deque:
	def __init__(self):
		self.front = None
		self.rear = None
		self.size = 0

	def addFront(self, object):
		newItem = DequeItem(object, previous=self.front)

		if self.rear is None:
			self.rear = newItem
		else:
			self.front.updateNext(newItem)
			newItem.updatePrevious(self.front)

		self.front = newItem
		self.size += 1

	def addRear(self, object):
		newItem = DequeItem(object, next=self.rear)

		if self.front is None:
			self.front = newItem
		else:
			self.rear.updatePrevious(newItem)
			newItem.updateNext(self.rear)

		self.rear = newItem
		self.size += 1

	def popFront(self):
		if self.front is None:
			raise KeyError
		self.size -= 1
		var = self.front.object
		self.front = self.front.previous
		if self.front is None:
			self.rear = None
		return var

	def popRear(self):
		if self.rear is None:
			raise KeyError
		self.size -= 1
		var = self.rear.object
		self.rear = self.rear.next
		if self.rear is None:
			self.front = None
		return var

	def isEmpty(self):
		return self.front is None and self.rear is None

class DequeItem:
	def __init__(self, object, previous=None, next=None):
		self.object = object
		self.next = next
		self.previous = previous

	def updatePrevious(self, previous):
		self.previous = previous

	def updateNext(self, next):
		self.next = next