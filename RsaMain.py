'''
Wojciech Gorzynski
18-05-2025 v1

RSA encryption algorithm implementation for educational purposes
'''

import random

def modinv(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    return old_s % b

def keysGenerator(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = 65537
    d = modinv(e, phi)
    return (e, n), (d , n)

def miller_rabin(n, base):
    d = n-1
    if pow(base, d, n) != 1:
        return False
    while d % 2 == 0:
        d //= 2
        if pow(base, d, n) != 1:
            if pow(base, d, n) == n-1:
                return True
            else: 
                return False
    return True

def isPrime(n, k=10):
    for i in range(k):
        base = random.randint(2, n-2)
        if not miller_rabin(n, base):
            return False
    return True

def pqGenerator():
    p = random.getrandbits(1024)
    while not isPrime(p):
        p = random.getrandbits(1024)
    q = random.getrandbits(1024)
    while not isPrime(q):
        q = random.getrandbits(1024)
    return p, q
       

def encrypt(message, publicKey):
    return [pow(c, publicKey[0], publicKey[1]) for c in message]
        
def decrypt(message, privateKey):
    return [pow(c, privateKey[0], privateKey[1]) for c in message]
   
def encryptString(message, publicKey):
    message_ascii = [ord(s) for s in message]
    return encrypt(message_ascii, publicKey)
    
def decryptString(message, privateKey):
    message_ascii = "".join([chr(s) for s in decrypt(message, privateKey)])
    return message_ascii

if __name__ == "__main__":
    p, q = pqGenerator()
    publicKey, privateKey = keysGenerator(p ,q)
    
    message = input("message: ")
    encrypted = encryptString(message, publicKey)
    
    for i in range(len(message)):
        print(f"{message[i]} : {encrypted[i]}")
    
    message_decrypted = decryptString(encrypted, privateKey)
    print(message_decrypted)
    