class OrderedList:
	def __init__(self):
		self.front = None
		self.size = 0

	def add(self, addedItem):
		self.size += 1
		if self.front is None or addedItem < self.front.storedItem:
			newItem = OrderedListItem(addedItem, self.front)
			self.front = newItem
			return
		
		item = None
		for item in self.nextItemGenerator():
			if addedItem < item.next.storedItem:
				newItem = OrderedListItem(addedItem, item.next)
				item.next = newItem
				return

		if item is None:
			newItem = OrderedListItem(addedItem, None)
			self.front.next = newItem
			return
		newItem = OrderedListItem(addedItem, None)
		item.next.next = newItem

	def remove(self, objectToRemove):
		if self.front is None:
			return False
		if self.front.storedItem == objectToRemove:
			self.front = self.front.next
			self.size -= 1
			return True

		for item in self.nextItemGenerator():
			if item.next.storedItem == objectToRemove:
				self.size -= 1
				item.next = item.next.next
				return True
			#Check if it's still possible to remove the object
			if item.storedItem > objectToRemove:
				return False
		return False

	def pop(self, index=-1):
		if self.size <= index:
			raise IndexError
		if index < 0:
			index = self.size -1

		if index == 0:
			storedVariable = self.front.storedItem
			self.front = self.front.next
			return storedVariable

		gen = self.all_items_in_list_gen()
		for i in range(index-1):
			gen.__next__()
		previous = gen.__next__()
		currentItem = gen.__next__()
		previous.next = currentItem.next
		self.size -= 1
		return currentItem.storedItem

	def search(self, objectToLookFor):
		for item in self.all_items_in_list_gen():
			if item.storedItem == objectToLookFor:
				return True
			if item.storedItem > objectToLookFor:
				return False
		return False

	def index(self, indexNumber):
		try:
			gen = self.all_items_in_list_gen()
			for i in range(indexNumber):
				gen.__next__()
			return gen.__next__().storedItem
		except:
			raise IndexError

	def all_items_in_list_gen(self):
		currentItem = self.front
		while currentItem is not None:
			yield(currentItem)
			currentItem = currentItem.next

	def nextItemGenerator(self):
		#This function doesn't return the last item
		if self.front is not None:
			currentItem = self.front
			while currentItem.next is not None:
				yield currentItem
				currentItem = currentItem.next

	def __str__(self):
		listItems = [x.storedItem for x in self.all_items_in_list_gen()]
		return str(listItems)

	def isEmpty(self):
		return self.front is None


class OrderedListItem:
	def __init__(self, item, next):
		self.storedItem = item
		self.next = next