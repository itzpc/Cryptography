import math
import numpy

#Enter KEy

key=input(" \n Enter key ( Should be 9 bit long ): ")

if len(key.split(' ')) != 9:
	print("Length Should Be 9")
	exit()
key=key.replace(" ", "")
key=key.upper()

KEY=[ list( key[i:i+3] ) for i in range(0, len(key), 3)]


M=str(input("\n Enter Plain Text :"))
M=M.upper()
M=M.replace(" ", "")
if len(M)%3 == 1:
	M+='XX'
elif len(M)%3 == 2:
	M+='X'

message=[ list( M[i:i+3] ) for i in range(0, len(M), 3)] # converting to 2D list 
i=0

# Making P matrix
PlainText=[[] for i in range(len(message))]
for eachList in message:
	for eachChar in eachList:
		PlainText[i].append(ord(eachChar)-65)
		
	i+=1

#Matrix Mulltiplication

#KEY=[[2, 4, 5], [9, 2, 1], [3, 17, 7]]
KEY=numpy.array(KEY)
PlainText=numpy.array(PlainText)

CipherText= (numpy.dot(KEY,PlainText.T)).tolist()

print("CipherText = Key : \n ",numpy.matrix(KEY),"* \n PlainText \n ",numpy.matrix(PlainText.T),"=  \n",numpy.matrix(CipherText),"\n CipherText = ",end='')

#Displaying Cipher Text
for eachList in CipherText:
	for eachChar in eachList:
		print(chr((eachChar%26)+65),end='')
print("\n")

