import binascii  #Importing binascii library for coverting integer to hexa or octa
# Note : though i am importing it but i do not used it 


# Storage for items
originalMessages = [""] * 12
hexaCipherTexts = [""] * 12
integerCipherTexts = []
integerMessages = [] 
globalCharacterKey = ""
globalIntegerKey = []
   
# Range Checkers
##########################################################################################################

# Function to check whether the value is in
def valueInRange(val):
	if (val >= 33 and val <= 90) or (val >= 97 and val <= 122) or  val == 32:
		return True
	else:
		return False

# Function to check whether the val is a upper case or not
def upperChar(val):
	if(val >= 65 and val <= 90):
		return True
	else:
		return False

# Function to check whether the val is a lower case or not
def lowerChar(val):
	if(val >= 97 and val <= 122):
		return True
	else:
		return False

# Converters
########################################################################################################

# Function to convert Hexaciphers to Integer Ciphers
def convertHexaCiphersToIntegerCiphers():
	for x in range(0,12):
		i = 0
		tl = []
		while(i < len(hexaCipherTexts[x])):
			s = hexaCipherTexts[x][i] + hexaCipherTexts[x][i + 1]
			intVal = int(s,16)
			i += 2
			tl.append(intVal)

		integerCipherTexts.append(tl)


# Function to convert from String to a Integer list
def convertStringToInteger(s):
	l = []
	for i in range(0,len(s)):
		intVal = ord(s[i])
		l.append(intVal)

	return l


# Function to convert all the messages to Integer list
def convertAllMessagesToIntegerLists():
	for i in range(0,12):
		tl = convertStringToInteger(originalMessages[i])
		integerMessages.append(tl)


# Function to convert Integer list to a String
def convertIntegerToString(l):
	s = ""
	for i in range(0,len(l)):
		if valueInRange(l[i]) == True:
			s += chr(l[i])
		elif l[i] == 32:
			s += " "
		else:
			s += "-"

	return s


# Function to Convert from integer list to a String
def convertFromIntegerListToString(l):
	resString = ""
	for i in range(0,len(l)):
		if(valueInRange(l[i]) == False):
			resString += '-'
		elif l[i] == 32:
			resString += " "
		else:
			resString += chr(l[i])

	return resString

# Xor Functions
#############################################################################################################

# Function to do the xor the ciphertext with the message
def xorMessageWithCipherText(mess,cip):
	minRange = min(len(mess),len(cip))
	l = []
	for i in range(0,140):
		if(i >= minRange):
			return l
		else:
			intVal = mess[i] ^ cip[i]	
			l.append(intVal)

	return l

# Printing Arena
#############################################################################################################

# Function to print the nested list
def printNestedList(l):
	for i in range(0,len(l)):
		print(l[i])

# Function to Print all the messages
def printAllMessages():
	for i in range(0,12):
		print(f"M{i + 1} : " + convertFromIntegerListToString(messageList[i]))

# Function to print the key
def printKey():
	print("The key is : ")
	print(convertFromIntegerListToString(globalKey))

# Function to print blank line after the message
def println(o):
	print(o)
	print()

# Main Function
###############################################################################################################

def main():

	# Opening the file
	f = open("streamciphertexts.txt","r")

	# Storing hexa cipher texts in a list
	x = 0
	for line in f:
		hexaCipherTexts[x] = line.rstrip()
		x += 1

	# Closing the file
	f.close()

	# Opening the decodingMessages.txt
	f = open("decodingMessages.txt","r")

	x = 0
	
	# Copying the broken messages in a list
	for line in f:
		originalMessages[x] = line.rstrip()
		x += 1

	f.close()

	# Converting all the hexa cipher text to integer list
	convertHexaCiphersToIntegerCiphers()

	# Converting all the messages to integer list
	convertAllMessagesToIntegerLists()

	# Getting the key by xoring the Last message with the last ciphertext
	k = xorMessageWithCipherText(integerMessages[11],integerCipherTexts[11])

	# Now xoring all the cipher text with the key
	for i in range(0,11):
		m = xorMessageWithCipherText(k,integerCipherTexts[i])
		println(f"The Message {i + 1} is : " + convertFromIntegerListToString(m))

	# Printing the last message
	println(f"The Message {12} is : " + convertFromIntegerListToString(integerMessages[11]))
	println(f"The Key is : \n{k}")


# Main Function
if __name__ == '__main__':
	main()