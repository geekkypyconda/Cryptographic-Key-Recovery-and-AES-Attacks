import binascii    #Importing binascii library for coverting integer to hexa or octa
# Note : though i am importing it but i do not used it 

# Hardcoding the key that i found from the previous
globalIntegerKey = [233, 185, 116, 95, 158, 226, 145, 176, 149, 23, 140, 204, 45, 231, 176, 101, 78, 215, 188, 24, 228, 178, 49, 91, 248, 85, 134, 201, 35, 112, 251, 76, 229, 99, 123, 46, 13, 86, 138, 24, 104, 182, 20, 140, 91, 108, 195, 20, 160, 77, 185, 122, 20, 0, 165, 8, 237, 6, 34, 249, 24, 138, 187, 84, 56, 47, 199, 70, 224, 68, 166, 33, 110, 77, 21, 163, 50, 65, 137, 8, 18, 96, 134, 73, 104, 0, 210, 70, 2, 225, 201, 51, 158, 3, 230, 202, 193, 244, 165, 107, 84, 65, 171, 12, 172, 55, 117, 98, 192, 56, 144, 179, 58, 133, 80, 79, 36, 20, 13, 15, 21, 120, 177, 58, 50, 178, 202, 10, 209, 72, 4, 68, 139, 203, 217, 247, 19, 242, 33, 35]

originalMessages = [""] * 12            # List to contain all the original message i text form
hexaCipherTexts = [""] * 12             # List to contain all the ciphertext in hexadecimal string format
integerCipherTexts = []                 # List to contain all the ciphertext in integer format
integerMessages = []                    # List to contain all the original messages in integer format
globalHexaKey = ""                      # variable for storing key in string format(Hex)
   

# Value Checkers
##########################################################################################################

def valueInRange(val):       # Function to check whether the value is human readable character or not
	if (val >= 33 and val <= 90) or (val >= 97 and val <= 122) or  val == 32:
		return True
	else:
		return False

def upperChar(val):         # Function to check whether the value is upper case or not
	if(val >= 65 and val <= 90):
		return True
	else:
		return False

def lowerChar(val):			# Function to check whether the value is lower case or not
	if(val >= 97 and val <= 122):
		return True
	else:
		return False

# Converters : Integer to string(both character and Hexa strins) and viceversa
###########################################################################################################

def convertHexaCiphersToIntegerCiphers():			# Function to convert cipherstext from hexadecimal string to integer list
	for x in range(0,12):
		i = 0                                       # Variable to traverse the xth ciphertext
		tl = []
		while(i < len(hexaCipherTexts[x])):
			s = hexaCipherTexts[x][i] + hexaCipherTexts[x][i + 1]		# Getting two characters from the string
			intVal = int(s,16)											# Converting them to integer
			i += 2
			tl.append(intVal)											# Appending it to a temporary list

		integerCipherTexts.append(tl)									# Appending the temporary list to main Integer cipher text list

def convertStringToInteger(s):						# Function to convert String to an integer List
	l = []											# Temporary list to store integer values
	for i in range(0,len(s)):
		intVal = ord(s[i])
		l.append(intVal)

	return l                                        # Returning the list


def convertIntegerToHexaDecimal(l):					# Function for converting Integer List to a Hexadecimal String
	ans = ""										# String for storing the result
	for i in range(0,len(l)):
		intVal = l[i]								# Getting the integer value in a varible
		h1 = hex(intVal)							# Getting the hexadecimal string from that value
		h2 = h1[2:]									# Removing the 0x from the starting
		ans += h2									# Adding it to the ans string

	return ans

def convertIntegerToString(l):						# Function for converting fomr Integer To String
	s = ""											# String to store the result
	for i in range(0,len(l)):
		if valueInRange(l[i]) == True:				# If the value is in range then add it to s else put a "-"
			s += chr(l[i])
		elif l[i] == 32:
			s += " "
		else:
			s += "-"

	return s 										# Returning the string


def convertFromIntegerListToString(l):              # Function to convert from integer list to String
	resString = ""									# variable to store the result
	for i in range(0,len(l)):
		if(valueInRange(l[i]) == False):
			resString += '-'
		elif l[i] == 32:
			resString += " "
		else:
			resString += chr(l[i])

	return resString 								# returning the string


# Xor functions
################################################################################################3


def xorMessageWithCipherText(mess,cip):				# Function to xor the message with the cipher text
	minRange = min(len(mess),len(cip))				# Going till the range which is minimum of both
	l = []											# Empty list to store the result of XOR
	for i in range(0,140):
		if(i >= minRange):
			return l
		else:
			intVal = mess[i] ^ cip[i]	
			l.append(intVal)

	return l 										# Returning the list


# Printing Arena
####################################################################################################

# Function to print all the messages
def printAllMessages():
	for i in range(0,12):
		print(f"M{i + 1} : " + convertFromIntegerListToString(messageList[i]))

# Function to print the key
def printKey():
	print("The key is : ")
	print(convertFromIntegerListToString(globalKey))

# Function to print the nested list
def printNestedList(l):
	for i in range(0,len(l)):
		print(l[i])

# Function to print empty line after the message
def println(o):
	print(o)
	print()


# main function
###################################################################################################

def main():
	f = open("streamciphertexts.txt","r")					# Reading from the ciphertext file

	x = 0 													# variable for indexing in the hexaciphertext file
	for line in f:											# Reading every line of file and storing it in a variable called line
		hexaCipherTexts[x] = line.rstrip()					# Storing that line in hexaCipherTexts list in xth index
		x += 1                                              # Incrementing the count

	f.close()												# Closing the file

	convertHexaCiphersToIntegerCiphers()					# Calling the function for converting all the cipher text in hexa format to integer format

	#Now Xoring every cipher text with the key
	for i in range(0,12):
		integerMessages.append(xorMessageWithCipherText(globalIntegerKey,integerCipherTexts[i]))    # Appending the message(in int format) to a list
		originalMessages[i] = convertFromIntegerListToString(integerMessages[i])					# Now converting that int message to string and storing it in a list
		println(f"The Message {i + 1} is : " + originalMessages[i]) 								# Printing the message

	println(f"The Key is : \n{globalIntegerKey}")													# Printing the key in integer format
	println(f"The Key in Hexadecimal : {convertIntegerToHexaDecimal(globalIntegerKey)}")			# Printing the key in Hexadecimal format


# Main function
if __name__ == '__main__':
	main()


