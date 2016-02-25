from Stack import Stack

def reverseString(stringToReverse):
	stackList = Stack()
	for char in stringToReverse:
		stackList.push(char)

	newString = ""
	while not stackList.isEmpty():
		newString += stackList.pop()
	return newString