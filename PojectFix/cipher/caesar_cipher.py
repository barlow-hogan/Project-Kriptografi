###CAESAR CIPHER
dict1={'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}
dict2={0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H', 8 : 'I', 9 : 'J', 10 : 'K', 11 : 'L', 12 : 'M', 13 :'N', 14 : 'O', 15 : 'P', 16 : 'Q', 17 : 'R', 18 : 'S', 19 : 'T', 20 : 'U', 21 : 'V', 22 : 'W', 23 : 'X', 24 : 'Y', 25 : 'Z'}

#def encrypt caesar cipher
def encrypt(message, key):
    cipher1 = ''
    for letter in message:
        if (letter != ' '):
            num = (dict1[letter] + key )% 26
            cipher1 += dict2[num]
        else :
            cipher1 += ' '
    return cipher1


#def decrypt caesar chiper
def decrypt(message, key):
    decipher1 = ''
    for letter in message:
        if (letter != ' '):
            num = (dict1[letter] - key)%26
            decipher1 += dict2[num]
        else :
            decipher1 += ' '
    return decipher1
print(encrypt('IQBAL SEPTA MAHDI', 13))
