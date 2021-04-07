# 1) We will choose 2 big enough prime numbers randomly
# 2) n = p * q
# 3 λ(n) = lcm(p − 1, q − 1) hesaplanır,
# 4 1 < e < λ(n) ve gcd(e, λ(n)) = 1  we choose "e" randomly
# 5 d e ≡ 1 (mod λ(n)) then we find the "d" 
# (n,e) Public Key
# (d, p, q, λ(n)) private key
import random

def ReadFile():
    file = open("Top100_words.txt","r")
    words=[]
    for i in file:
        words.append(i)
    return words

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
    
    
def LCM(x, y):
   if x > y:
       greate = x
   else:
       greate = y
   lcm = 1
   while(True):
       if((greate % x == 0) and (greate % y == 0)):
           lcm = greate
           break
       greate += 1

   return lcm

def isPrime(x):
    if(x==1):
        return False
    if(x%2==0):
        return False
    for i in range(2,x//2):
        if(x%i == 0):
            return False
    return True


def CreatePrimeNumbers(n):
    array= [2]
    for i in range(1,n):
        x = isPrime(i)
        if(x == True):
             array.append(i)   
    return array

def ChooseE(PhiN):
    arr=[]
    for i in range(1,PhiN):
            arr.append(i)
    i=0
    # Just try 100 times. If we can't choose randomly egcd(e,PhiN)==1 
    #we will assign the number
    #Beacuse we can wait for along time.
    while(i<100):
        e = random.choice(arr)
        if(egcd(e,PhiN)==1):
            break
        i=i+1
    e = (PhiN//2)-1
    print("We could not select with random so we assigned")
    return e
        
def StringToAscii():
    enciphered_code=[]
    print("Chose Random word")
    words = ReadFile()
    message = random.choice(words)
    #message = message.split(' ')
    enciphered_code = [] 
    for word in message:
        for letter in word:
            asci = ord(letter)
            enciphered_code.append(asci)
    return enciphered_code

def Decipherment(d,n,encodedList):
    decipList=[]
    for i in encodedList:
        clear = (i**d) % n
        decipList.append(clear)
    message =""
    for i in decipList:
        message = message+chr(i)
    return message

        # MAIN
#Choose Random 2 prime numbers
arr =[]
arr = CreatePrimeNumbers(1000) # if you increase the 1000 , Your waiting time increase too

# 1) We will choose 2 big enaugh primal numbers
p = random.choice(arr)
q = random.choice(arr)
print("p -->"+str(p) +"   " "q-->"+str(q))
#-------------------------------------
# # 2) n = p * q
n = p*q
print("n ---->",n)
#-------------------------------------
# 3 λ(n) = lcm(p − 1, q − 1)
PhiN  = LCM(p-1 , q-1)
print("Phin ---->",PhiN)
#-------------------------------------
#4 1 < e < λ(n) ve gcd(e, λ(n)) = 1
e = ChooseE(PhiN)
print("e ---->",e)
#-------------------------------------

# 5 d e ≡ 1 (mod λ(n))
d = modinv(e,PhiN)
print("d -----> ",d)
#-------------------------------------


#ciphering part
asciiList=[]
asciiList = StringToAscii()
encodedList=[]

# m is "i"
for i in asciiList:
    c = (i**e) % n
    encodedList.append(c)
    
print(encodedList)    
    

#--------------------------

#decipherment part
a = int(input("Do you want to see message ? 1-yes 2-no \n"))
if(a ==1):
    message = Decipherment(d,n,encodedList)
    print("Bob's Message is : ",message)
else:
    print("Nothing")










 
