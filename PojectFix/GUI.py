# python module to create GUI		 
from tkinter import *

		
root = Tk() 
root.title("CRYPTOGRAPHY") 
root.geometry("420x260")
import cipher.caesar_cipher as caesar_cipher
import cipher.vigenere_cipher as vigenere_cipher
def encryptMessage():					 
	message = e1.get() 
	# inbuilt function to encrypt a message
	key1 = 13
	key2 = 'KRIPTOGRAFI'
	key3 = vigenere_cipher.generateKey(message,key2)
	key4 = 15
	key5 = 'AMIKOM'
	key6 = vigenere_cipher.generateKey(message,key5)
	result = caesar_cipher.encrypt(message.upper(), key1)
	message = result
	result2 = vigenere_cipher.encryptVigenere(message.upper(), key3)
	message = result2
	result3 = caesar_cipher.encrypt(message.upper(), key4)
	message = result3
	result4 = vigenere_cipher.encryptVigenere(message.upper(), key6)
	e2.insert(0, result4)
	
def decryptMessage():					 
	message = e3.get() 
	# inbuilt function to decrypt a message
	key1 = 13
	key2 = 'KRIPTOGRAFI'
	key3 = vigenere_cipher.generateKey(message,key2)
	key4 = 15
	key5 = 'AMIKOM'
	key6 = vigenere_cipher.generateKey(message,key5)
	result = caesar_cipher.decrypt(message.upper(), key1)
	message = result
	result2 = vigenere_cipher.decryptVigenere(message.upper(), key3)
	message = result2
	result3 = caesar_cipher.decrypt(message.upper(), key4)
	message = result3
	result4 = vigenere_cipher.decryptVigenere(message.upper(), key6)

	e4.insert(0, result4)
	
# creating labels and positioning them on the grid 
label1 = Label(root, text ='plain text')			 
label1.grid(row = 10, column = 1) 
label2 = Label(root, text ='encrypted text') 
label2.grid(row = 11, column = 1) 
l3 = Label(root, text ="cipher text") 
l3.grid(row = 10, column = 10) 
l4 = Label(root, text ="decrypted text") 
l4.grid(row = 11, column = 10) 

# creating entries and positioning them on the grid 
e1 = Entry(root) 
e1.grid(row = 10, column = 2) 
e2 = Entry(root) 
e2.grid(row = 11, column = 2) 
e3 = Entry(root) 
e3.grid(row = 10, column = 11) 
e4 = Entry(root) 
e4.grid(row = 11, column = 11) 

# creating encryption button to produce the output 
ent = Button(root, text = "encrypt", bg ="red", fg ="white", command = encryptMessage) 
ent.grid(row = 13, column = 2) 

# creating decryption button to produce the output 
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = decryptMessage) 
b2.grid(row = 13, column = 11) 


root.mainloop() 
