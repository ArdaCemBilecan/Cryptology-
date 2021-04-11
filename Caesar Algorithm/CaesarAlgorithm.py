import random
def DecodingCaesar(message,key):
    realMessage=''
    for letter in message:
        x= (ord(letter)-key) % 127
        realMessage = realMessage+chr(x)
    return realMessage

def EnCodingCaesar(key):
    words=[]
    encodeMessage=''
    file = open('Top100_words.txt','r')
    for i in file:
        i = i.split('\n')
        words.append(i[0])
    Message = random.choice(words)
    for i in Message:
        x = (ord(i)+key) % 127
        encodeMessage = encodeMessage + chr(x)
    
    return encodeMessage


#Main

key = int(input("Write to key : "))
secretMessage = EnCodingCaesar(key)
print(secretMessage)
print("Do you want to see Decoding Message ? 1-yes 2-no : ")
x = int(input())
if(x ==1):
    decodingMessage = DecodingCaesar(secretMessage,key)
    print(decodingMessage)
