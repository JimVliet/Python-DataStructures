class Stack:
	def __init__(self):
		self.firstInStack = None
		self.size = 0

	def add(self, object):
		self.size +=1
		self.firstInStack = StackItem(object, self.firstInStack)

	def isEmpty(self):
		return self.firstInStack is None

	def pop(self):
		if self.firstInStack is None:
			raise IndexError
		self.size -= 1
		var = self.firstInStack.object
		self.firstInStack = self.firstInStack.next
		return var

class StackItem:
	def __init__(self, object, nextInStack):
		self.object = object
		self.next = nextInStack

	def updateNext(self, nextStackObject):
		self.next = nextStackObject