IP ={1:2,2:6,3:3,4:1,5:4,6:8,7:5,8:7}
IP_inverse={v:k  for k,v in IP.items()}
P10={1:3, 2:5 ,3:2, 4:7, 5:4, 6:10, 7:1 ,8:9, 9:8 ,10:6}
P8={1:6 ,2:3 ,3:7,4:4,5:8,6:5,7:10,8:9}
P4={1:2,2:4,3:3,4:1}
E={1:4,2:1,3:2,4:3,5:2,6:3,7:4,8:1}

S0=[['01','00','11','10'],['11','10','01','00'],['00','10','01','11'],['11','01','11','10']]
S1=[['00','01','10','11'],['10','00','01','11'],['11','00','01','00'],['10','01','00','11']]

def readPlainText():
	plain=str(input("Enter PlainText [ 8-bit long ]: "))
	plain=plain.upper()
	plain=plain.replace(" ", "")
	if len(plain) != 8:
		print(" Plain Text is Not 8 bit long")
		exit()
	else:
		for eachBit in plain:
			if int(eachBit) not in (0,1):
				print("Enter binary Number")
				exit()
	plain={i+1:plain[i] for i in range (len(plain))}
	return plain

def readKey():
	key=str(input("Enter Key [ 10-bit long ]: "))
	key=key.upper()
	key=key.replace(" ", "")
	if len(key) != 10:
		print(" Plain Text is Not 8 bit long")
		exit()
	else:
		for eachBit in key:
			if int(eachBit) not in (0,1):
				print("Enter binary Number")
				exit()
	key={i+1:key[i] for i in range (len(key))}
	return key

def correctingDictIndex(Dict):
	return {i+1:list(Dict.values())[i] for i in range(0,int(len(Dict)))}

def expansion(plainT):
	plainT= correctingDictIndex(plainT) #  because rightPlain text dictionary index starts at 5 ( Correcting Index)
	expandedText={  i+1 : None for i in range(len(E))}
	i=1
	for eachBit in E.values():
		expandedText[i]=plainT[eachBit] 
		i+=1
	return expandedText

def permutation(permutationList,textToBePermutted):
	permuttedText={  i+1 : None for i in range(len(permutationList))}
	for position,eachBit in textToBePermutted.items(): 
		try:
			permuttedText[ list( permutationList.keys() ) [ list( permutationList.values() ).index(position) ] ]=eachBit
		except ValueError:
			pass
	return permuttedText
	
def splitText(text,start,end):
	return  { i+1 : list(text.values())[i] for i in range(start,end)}

def keyPreManipulation(key):
	key=permutation(P10,key)  # Key undergoes P10
	keyLeftHalf=splitText( key,0,int(len(key)/2) )
	keyRightHalf=splitText( key,int(len(key)/2),len(key) )
	return keyLeftHalf , keyRightHalf

def plainPreManipulation(plainText):
	plainText=permutation(IP,plainText)  # Key undergoes P10
	plainTextLeftHalf=splitText( plainText,0,int(len(plainText)/2) ) 
	plainTextRightHalf=splitText( plainText,int(len(plainText)/2),len(plainText) )
	return plainTextLeftHalf , plainTextRightHalf

def leftShift(key,numShift):
	key={i+1 : (list(key.values())[numShift:]+list(key.values())[:numShift])[i] for i in range(len(key))}
	return key

def mergeTwoHalf(leftHalf,rightHalf):
	fullText=leftHalf.copy()
	fullText.update({ len(fullText)+i+1 : list(rightHalf.values())[i] for i in range(0,len(rightHalf))})
	return fullText

def keyGeneration(keyL,keyR,numRound):
	keyL=leftShift(keyL,numRound)
	keyR=leftShift(keyR,numRound)
	keys=mergeTwoHalf(keyL,keyR)
	roundKey= permutation(P8,keys)
	return roundKey,keyL,keyR

def sBox(sBoxMatrix,plainT):
	sBoxCol=list()
	sBoxRow=list(str(list(plainT.values())[0]))
	sBoxRow.append(str(list(plainT.values())[-1]))
	sBoxRow='0b'+''.join(sBoxRow)
	sBoxRow=int(sBoxRow,2)
	for v in list(plainT.values())[1:-1]:
		sBoxCol.append(str(v))
	sBoxCol='0b'+''.join(sBoxCol)
	sBoxCol=int(sBoxCol,2)
	return {i+1:list(sBoxMatrix[sBoxRow][sBoxCol])[i] for i in range (0,int(len(list(S0[sBoxRow][sBoxCol]))))}

def xorOperation(A,B):
	A=correctingDictIndex(A)
	B=correctingDictIndex(B)
	return { i: int(A[i])^int(B[i]) for i in range(1,len(B)+1)}

def formateedPrint(inputDict):
	output=list()
	for v in list(inputDict.values()):
		output.append(str(v))
	output=''.join(output)
	return output 

plainText=dict(readPlainText())
encryptionKey=dict(readKey())
keyLeft,keyRight = keyPreManipulation(encryptionKey) # key PreManipulation 
plainLeft ,plainRight =plainPreManipulation(plainText) # PlainText PreManipulation
nRounds=2 #number of Rounds

for i in range(1,nRounds+1):
	print("ROUND : ",i)
	plainRight_Copy=plainRight.copy()
	plainRight=expansion(plainRight)
	roundKey ,keyLeft,keyRight = keyGeneration(keyLeft,keyRight,i)
	print("Round ",i," KEy  ", formateedPrint(roundKey))
	
	plainRight= xorOperation(plainRight,roundKey)#XOR
	print("After XOR ",formateedPrint(plainRight))
	plainRightL=splitText( plainRight,0,int(len(plainRight)/2) )
	plainRightR=splitText( plainRight,int(len(plainRight)/2),int(len(plainRight)) )
	plainRightL=sBox(S0,plainRightL)
	plainRightR=sBox(S1,plainRightR)
	plainRight=mergeTwoHalf(plainRightL,plainRightR)
	print("After Sbox ",formateedPrint(plainRight))
	plainRight=permutation(P4,plainRight)

	plainRight=xorOperation(plainLeft,plainRight)
	plainLeft=plainRight_Copy.copy()
	print("After ",i,"st Round ",formateedPrint(plainLeft)+formateedPrint(plainRight))
cipherText=mergeTwoHalf(plainRight,plainLeft) # undo the last swap
print("After Last Round ",formateedPrint(plainLeft)+formateedPrint(plainRight))
cipherText=permutation(IP_inverse,cipherText)
print("Cipher Text after S-DES : ",formateedPrint(cipherText) )
