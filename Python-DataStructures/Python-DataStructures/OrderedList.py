class OrderedList:
	def __init__(self):
		self.front = None
		self.size = 0

	def add(self, addedItem):
		self.size += 1
		if self.front is None:
			newItem = OrderedListItem(addedItem, self.front, None)
			self.front = newItem
			return

		for item in self.itemsInListGen():
			if addedItem < item.storedItem:
				newItem = OrderedListItem(addedItem, item, item.previous)
				if item.previous is not None:
					item.previous.next = newItem
				else:
					self.front = newItem
				item.previous = newItem
				return

		newItem = OrderedListItem(addedItem, None, item)
		item.next = newItem

	def remove(self, objectToRemove):
		for item in self.itemsInListGen():
			if item.storedItem == objectToRemove:
				if item.previous is None:
					self.front = item.next
					self.size -= 1
					return True
				self.size -= 1
				item.previous.next = item.next
				return True
			#Check if it's still possible to remove the object
			if item.storedItem > objectToRemove:
				return False
		return False

	def pop(self, index = -1):
		if self.size <= index:
			raise IndexError
		if index < 0:
			index = self.size -1
		gen = self.itemsInListGen()
		for i in range(index):
			gen.__next__()
		currentItem = gen.__next__()
		if currentItem.previous is not None:
			currentItem.previous.next = currentItem.next
		else:
			self.front = currentItem.next
		if currentItem.next is not None:
			currentItem.next.previous = currentItem.previous
		self.size -= 1
		return currentItem.storedItem

	def search(self, objectToLookFor):
		for item in self.itemsInListGen():
			if item.storedItem == objectToLookFor:
				return True
			if item.storedItem > objectToLookFor:
				return False
		return False

	def index(self, indexNumber):
		try:
			gen = self.itemsInListGen()
			for i in range(indexNumber):
				gen.__next__()
			return gen.__next__().storedItem
		except:
			raise IndexError

	def itemsInListGen(self):
		currentItem = self.front
		while currentItem is not None:
			yield(currentItem)
			currentItem = currentItem.next

	def __str__(self):
		listItems = [x.storedItem for x in self.itemsInListGen()]
		return str(listItems)

	def isEmpty(self):
		return self.front is None


class OrderedListItem:
	def __init__(self, item, next, previous):
		self.storedItem = item
		self.next = next
		self.previous = previous