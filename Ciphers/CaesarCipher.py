def readPlainText():
	plain=str(input("Enter PlainText : "))
	plain=plain.upper()
	plain=plain.replace(" ", "")
	return plain


def encryption(plainT,smallKey):
	i=0
	cipherText=list()
	for eachChar in plainT:
		cipherText.append(chr(ord(plainT[i])+smallKey))
		i+=1
	return cipherText
	
def decryption(cipherT,smallKey):
	i=0
	decryptedT=list()
	for eachChar in cipherT:
		decryptedT.append(chr(ord(cipherT[i])-smallKey))
		i+=1
	return decryptedT

def printText(text):
	for eachChar in text:
		print(eachChar,end=' ')
	print("\n")

#read Inputs
plainText=list(readPlainText())

encryptionKey=2

#encryption
cipherText=encryption(plainText,encryptionKey)
print("CipherText : ", end= ' ' ) ; printText(cipherText)

#decrption
decryptedText=decryption(cipherText,encryptionKey)
print("Decrypted Text : ", end= ' ' ) ; printText(decryptedText)