class OrderedList:
	def __init__(self):
		self.front = None

	def add(self, addedItem):
		if self.front is None:
			newItem = OrderedListItem(addedItem, self.front)
			self.front = newItem
			return

		previousItem = None
		nextItem = self.front
		while nextItem is not None:
			if addedItem < nextItem.storedItem:
				newItem = OrderedListItem(addedItem, nextItem)
				if previousItem is not None:
					previousItem.updateNext(newItem)
				else:
					self.front = newItem
				return
			previousItem = nextItem
			nextItem = nextItem.next

		newItem = OrderedListItem(addedItem, None)
		previousItem.updateNext(newItem)

	def remove(self, objectToRemove):
		previousItem = None
		nextItem = self.front
		while nextItem is not None:
			if nextItem.storedItem == objectToRemove:
				if previousItem is None:
					self.front = nextItem.next
					return
				previousItem.next = nextItem.next
				return
			previousItem = nextItem
			nextItem = nextItem.next

	def search(self, objectToLookFor):
		index = 0
		currentItem = self.front
		while currentItem is not None:
			if currentItem.storedItem == objectToLookFor:
				return True
			if currentItem.storedItem > objectToLookFor:
				return False
			currentItem = currentItem.next
		return False

	def index(self, indexNumber):
		if self.front is None:
			return None
		currentItem = self.front
		for pos in range(indexNumber):
			if currentItem.next is None:
				return None
			currentItem = currentItem.next

		return currentItem.storedItem

	def __str__(self):
		listItems = []
		nextItem = self.front
		while nextItem is not None:
			listItems.append(nextItem.storedItem)
			nextItem = nextItem.next

		return str(listItems)

	def size(self):
		currentItem = self.front
		listSize = 0
		while currentItem is not None:
			listSize += 1
			currentItem = currentItem.next
		return listSize

	def pop(self, index = -1):
		if self.front is None:
			return None
		previous = None
		currentItem = self.front
		while currentItem.next is not None:
			if index == 0:
				if previous is None:
					self.front = currentItem.next
				else:
					previous.next = currentItem.next
				return currentItem.storedItem
			index -= 1
			previous = currentItem
			currentItem = currentItem.next
		return currentItem.storedItem

	def isEmpty(self):
		return self.front is None


class OrderedListItem:
	def __init__(self, item, next):
		self.storedItem = item
		self.next = next

	def updateNext(self, newNext):
		self.next = newNext