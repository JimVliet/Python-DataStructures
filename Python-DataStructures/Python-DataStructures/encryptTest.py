def encrypt(numbToEncrypt, key):
	base = len(key)
	remList = []

	while numbToEncrypt > 0:
		rem = numbToEncrypt%base
		remList.append(rem)
		numbToEncrypt = numbToEncrypt // base

	newString = ""
	while remList != []:
		newString += key[remList.pop()]

	return newString

def decrypt(stringToDecrypt, key):
	stringToDecrypt = list(stringToDecrypt)
	stringToDecrypt.reverse()
	base = len(key)
	keyList = {}

	for index, letter in enumerate(key):
		keyList[letter] = index
	answer = 0
	for index, letter in enumerate(stringToDecrypt):
		answer += keyList[letter]* (base**index)

	return answer