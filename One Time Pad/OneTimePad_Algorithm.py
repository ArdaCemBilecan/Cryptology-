# This algorithm , we will use XOR operation.
import random

def readFile():
    words=[]
    file = open("Top100_words.txt","r")
    for i in file:
        x = i.split("\n")
        words.append(x[0])
    chosen = random.choice(words)
    return chosen

def xor(a,b):
    if(a==b):
        return "0"
    else:
        return "1"

def ConvertToBinary(x):
    # Also we can use bin(ord(x)) instead of this algorithm.
    #But I would like to show that how to calculate convert to binary with algorithm
    binary=""
    while x>=1:
        if(x%2 == 1):
            binary="1"+binary
        else:
            binary = "0"+binary
        x = x//2
        
    while(len(binary)<8):
        binary = "0"+binary    
    return binary

def ConvertToDecimal(decoding):
    splited = [decoding[i:i+8] for i in range(0,len(decoding),8)]
    array=[]
    number = 0
    for j in splited:
          for i in range (len(j)):
              number = number + ( int(j[i])*(2**(7-i)))
          array.append(number)
          number = 0
    return array
    

def Trans_Decimal_To_Letter(array):
       message = ""
       for i in array:
           message = message + chr(i)
       return message

def Trans_Word_To_Binary(message):
    array=[]
    for i in message:
        x = ord(i)
        array.append(x)
    binaryArray=[]
    for i in array:
        x = ConvertToBinary(i)
        binaryArray.append(x)
    return binaryArray
    

def Encoding(binaryArray,key):
    cipherMessage=""
    for i in binaryArray:
        for j in range(len(key)):
            x = xor(i[j],key[j])
            cipherMessage= cipherMessage+x
    return cipherMessage

def Decoding(cipherMessage,key):
    decode=""
    for i in range(len(cipherMessage)):
        x = xor(cipherMessage[i],key[i%8])
        decode = decode+x
    return decode    
        
def CreateToKey():
    arr = ["0","1"]
    key=""
    for i in range(8):
        key=key+random.choice(arr)
    return key    


message=readFile()
binaryArray=Trans_Word_To_Binary(message)

key = CreateToKey() # We created random key
cipherMessage = Encoding(binaryArray,key)
print("----Cipher Message----")
print(cipherMessage)
print()
decoding = Decoding(cipherMessage,key)
print("--Decoding-----")
print(decoding)
array = ConvertToDecimal(decoding)
realMessage = Trans_Decimal_To_Letter(array)
print()
print("Real Message is : ",realMessage)


