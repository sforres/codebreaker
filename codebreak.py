code = "pbqrarjovrf ner gur zbfg fhccbegvir pbzzhavgl"
msg1 = "No one can read this secret message"
msg2 = "it is so super secret"
msg3 = "only a CodeNewbie can figure it out"


def decrypt_message(message):
#Code is decrypted by converting to unicode via ord()  note a=97 z=122
#code increase by 13
	decrypted_msg = "" 
	for char in message:
		ord_char = ord(char.lower())
		ord_newchar = ord_char + 13
		if ord_newchar > 122:
			ord_newchar = 97 + (ord_char + 13) - 123
		#account for blanks and keep blanks blanks
		if ord_char == 32:
			ord_newchar =32
		decrypted_msg += str(chr(ord_newchar))
	return(decrypted_msg)	
    
def encrypt_message(message):
#as there are 23 letters in the alphabet conversion is the same as decryption
	return (decrypt_message(message))

print (60 * '*')
print ('Code Breaker')
print (decrypt_message(code))

print (20 * '=')
print (msg1)
print (encrypt_message(msg1))
print (decrypt_message(encrypt_message(msg1)))

print (20 * '=')
print (msg2)
print (encrypt_message(msg2))
print (decrypt_message(encrypt_message(msg2)))

print (20 * '=')
print (msg3)
print (encrypt_message(msg3))
print (decrypt_message(encrypt_message(msg3)))


