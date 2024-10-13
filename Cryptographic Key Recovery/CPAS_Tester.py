import binascii  #Importing binascii library for coverting integer to hexa or octa
# Note : though i am importing it but i do not used it 


# Storage for items

hexaCipherTexts = [""] * 12
intCipherTexts = []   #List of lists aka 2D list
allXorCipherTexts = []  # List of lists  3D list
messageList = []  # 2D List
globalKey = [-1] * 200		# 1D List
   
# Value Checkers
##########################################################################################################

# Checking whether the value is in range or not
def valueInRange(val):
	if (val >= 65 and val <= 90) or (val >= 97 and val <= 122) or val == 32:
		return True
	else:
		return False

# Checking whether the val lies in the range of upper case letters
def upperChar(val):
	if(val >= 65 and val <= 90):
		return True
	else:
		return False

# Checking whether the val lies in the range of lower case letters
def lowerChar(val):
	if(val >= 97 and val <= 122):
		return True
	else:
		return False

# All other functions
########################################################################################################

# Function to convert Hexa Ciphers to integer cipher list
def convertHexaCipherToIntegerCiphers():
	for i in range(0,12):
		j = 0
		l = []
		while (j < len(hexaCipherTexts[i])):
			s = hexaCipherTexts[i][j] + hexaCipherTexts[i][j + 1]
			intVal = int(s,16)
			j += 2
			l.append(intVal)

		intCipherTexts.append(l)

# Utility Function for xoring all the ciphers texts 
def xorAllCipherTexts_Util(i,j,cip1,cip2):
	minRange = min(len(cip1),len(cip2))
	l = []
	for i in range(0,minRange):
		xorRes = cip1[i] ^ cip2[i]
		l.append(xorRes)

	return l

# Function to xor all the cipher text
def xorAllCipherTexts():
	for i in range(0,12):
		tempList = []
		for j in range(i + 1,12):
			l = xorAllCipherTexts_Util(i,j,intCipherTexts[i],intCipherTexts[j])
			tempList.append(l)
		allXorCipherTexts.append(tempList)


# Print all the cipher text
def printAllXorCipherText():
	for i in range(0,12):
		for y in range(i + 1,12):
			print(f"{i + 1} -Xor- {y + 1}" + convertFromIntegerListToString(allXorCipherTexts[i][y - i - 1]))
		print()

# Heart of this logic
# Utility function for Filling the locations with correct value 
def fillLocations_Util(i,j,x,c1,c2,cx):
	asM1 = 32
	asM2 = 0

	asM2 = (cx + 32) if upperChar(cx) else (cx - 32)

	if (asM1 ^ c1) == (asM2 ^ c2):
		messageList[i][x] = asM1
		messageList[j][x] = asM2
		globalKey[x] = (asM1 ^ c1)
	else:
		t = asM1
		asM1 = asM2
		asM2 = t

		asM2 = (cx + 32) if upperChar(cx) else (cx - 32)

		if (asM1 ^ c1) == (asM2 ^ c2):
			messageList[i][x] = asM1
			messageList[j][x] = asM2
			globalKey[x] = (asM1 ^ c1)
		else:
			print("Condition Fails!")

# Function to fill the indexes correctly 
def fillLocations(i,j):
	c1 = intCipherTexts[i]
	c2 = intCipherTexts[j]
	cx = allXorCipherTexts[i][j - i - 1]
	minRange = len(cx)

	# print(f"C1 is : {c1}")
	# print(f"C2 is : {c2}")
	# print(f"Xor is : {cx}")

	for x in range(0,minRange):
		if valueInRange(cx[x]):
			# print(f"Current Processing for index : {x} Index")
			fillLocations_Util(i,j,x,c1[x],c2[x],cx[x])
			# print("After Processing : ")
			# print(f"M{i + 1}  : " + convertFromIntegerListToString(messageList[i]))
			# print(f"M{j + 1}  : " + convertFromIntegerListToString(messageList[j]))
			# print("Key : " + convertFromIntegerListToString(globalKey) + " \n")
		else:
			pass

# Function to print Nested list 
def printNestedList(l):
	for i in range(0,len(l)):
		print(l[i])


# Function to convert from integer list to String
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


# Function to xor cipher text with key
def xorCipherWithKey(index,cip,key):
	minRange = min(len(cip),len(key))
	for i in range(0,minRange):
		xorRes = cip[i] ^ key[i]
		messageList[index][i] = xorRes

# Function to do xor of all cipher text
def xorWithAllCipherText():
	for i in range(0,12):
		xorCipherWithKey(i,intCipherTexts[i],globalKey)

# Function to print all the messages
def printAllMessages():
	for i in range(0,12):
		print(f"M{i + 1} : " + convertFromIntegerListToString(messageList[i]))

# Function to print the key
def printKey():
	print("The key is : ")
	print(convertFromIntegerListToString(globalKey))

# Function to fill the message list with -1
def fillInitial():
	for i in range(0,12):
		p = []
		for h in range(0,200):
			p.append(-1)
		messageList.append(p)


# Function to print next line after the message
def println(o):
	print(o)
	print()


# Main Function
###############################################################################################################3

def main():
	# Filling the message list with -1
	fillInitial()

	# Opening the file and extracting the cipher text's
	f = open("streamciphertexts.txt","r")
	x = 0
	for line in f:
		hexaCipherTexts[x] = line.rstrip()
		x += 1

	f.close()

	# Calling function to convert hexa cipher texts to integer lists
	convertHexaCipherToIntegerCiphers()
	
	# Xoring all the cipher text with each other
	xorAllCipherTexts()


	#Filling the locations
	for i in range(0,12):
		for j in range(i +  1,12):
			fillLocations(i,j)

	# Printing all the messages and key
	printAllMessages()
	printKey()

	print()
	print()

	# printAllXorCipherText()
	xorWithAllCipherText()

	print("After Xoring the obtained key with all the other cipher texts : \n")

	# Again printing messages and key
	printAllMessages()
	printKey()

# Main Function
if __name__ == '__main__':
	main()