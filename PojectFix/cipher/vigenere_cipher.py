###VIGNERE CIPHER

#def generate key
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    return("".join(key))

#def encrypt vigenere
def encryptVigenere(message, key):
    cipher1=[]
    for i in range(len(message)):
        x=(ord(message[i])+ord(key[i]))%26
        x+=ord('A')
        cipher1.append(chr(x))
    return("".join(cipher1))

#def decrypt vigenere
def decryptVigenere(message, key):
    decipher1 = []
    for i in range(len(message)):
        x= (ord(message[i])-ord(key[i]))%26
        x+= ord('A')
        decipher1.append(chr(x))
    return("".join(decipher1))

print(encryptVigenere('IQBAL SEPTA MAHDI', 'AMIKOMAMIKOMAMIKO'))
print(decryptVigenere('ICJKZFSQXDOFMMPNW', 'AMIKOMAMIKOMAMIKO'))
