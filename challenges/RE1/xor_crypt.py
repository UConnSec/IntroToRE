#!/bin/python
import sys
#takes 2 arguments: KEY_FILE,FILE
#This is similar to a vignere cypher
if (len(sys.argv) != 4):
	sys.exit('Usage: %s <KEY_FILE> <ENC_FILE> <RESULT_FILE_NAME>' % sys.argv[0])

#open the files as bytes instead of chars with 'rb'
keyFile = open(sys.argv[1],'rb')
cyphertextFile = open(sys.argv[2],'rb')

#copy the files contents into strings
key = keyFile.readline()
if key[-1] == ord('\n'):
	key = key[:-1]
#for the sake of this program plaintext/cyphertext file is named cyphertext
cyphertext = cyphertextFile.read()

#plaintextList stores the characters as theyre <de/en>crypted
plaintextList = []

keyIndex = 0
#iterate through the cyphertext xoring characters
for cypherChar in cyphertext:

	#^ is xor so the two integers are xored
	#bytes objects interpret each char as an 8-bit integer, aka: a byte
	plaintextList.append(cypherChar ^ key[keyIndex])

	#if index extends past key then it should reset to first char
	#real encryption methods dont do this, because you should only do 1-time pad
	keyIndex = (keyIndex + 1) % len(key)

#convert list object to bytes object
plaintextList = bytes(plaintextList)

#convert the list to a string and write to result file
result = open(sys.argv[3],'wb')
result.write(plaintextList)
result.close()
keyFile.close()
cyphertextFile.close()

	
