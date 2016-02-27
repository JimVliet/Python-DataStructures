class OrderedList:
	def __init__(self):
		self.front = None
		self.size = 0

	def add(self, addedItem):
		self.size += 1
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
		self.size -= 1
		itemLinks = self.getItemLinksWithValue(objectToRemove)
		if itemLinks is None:
			return False

		if itemLinks[0] == None:
			self.front = nextItem.next
			return True

		itemLinks[0].next = itemLinks[1].next
		return True

	def getItemLinksWithValue(self, valueToCheck):
		previousItem = None
		nextItem = self.front
		while nextItem is not None:
			if nextItem.storedItem == valueToCheck:
				return (previousItem, nextItem)
			previousItem = nextItem
			nextItem = nextItem.next
		return None

	def pop(self, index = -1):
		self.size -= 1
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

	def search(self, objectToLookFor):
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

	def isEmpty(self):
		return self.front is None


class OrderedListItem:
	def __init__(self, item, next):
		self.storedItem = item
		self.next = next

	def updateNext(self, newNext):
		self.next = newNext