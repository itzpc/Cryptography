def readPlainText():
	plain=str(input("Enter PlainText : "))
	plain=plain.upper()
	plain=plain.replace(" ", "")
	return plain

def readKey(textLength):
	key=str(input("Enter Key : "))
	key=key.upper()
	key=key.replace(" ", "")
	if len(key)<textLength:
		key=key+'X'*(textLength-len(key))
	elif len(key)>textLength:
		key=key[:textLength]
	return key

def encryption(plainT,encryptionK):
	i=0
	cipherText=list()
	for eachChar in encryptionK:
		smallKey=(ord((eachChar))-ord('A'))
		cipherText.append(chr(ord(plainT[i])+smallKey))
		i+=1
	return cipherText
	
def decryption(cipherT,encryptionK):
	i=0
	decryptedT=list()
	for eachChar in encryptionK:
		smallKey=(ord((eachChar))-ord('A'))
		decryptedT.append(chr(ord(cipherT[i])-smallKey))
		i+=1
	return decryptedT

def printText(text):
	for eachChar in text:
		print(eachChar,end=' ')
	print("\n")

#read Inputs
plainText=list(readPlainText())
encryptionKey=list(readKey(len(plainText)))

#encryption
cipherText=encryption(plainText,encryptionKey)
print("CipherText : ", end= ' ' ) ; printText(cipherText)

#decrption
decryptedText=decryption(cipherText,encryptionKey)
print("Decrypted Text : ", end= ' ' ) ; printText(decryptedText)