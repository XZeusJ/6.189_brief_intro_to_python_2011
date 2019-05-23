#Zhangjin Xiao

# letter = 'a'

# ascii_code = ord(letter)
# letter_res = chr(ascii_code)

# print ascii_code,letter_res


phrase = raw_input("Enter sentence to encrypt: ")
value = input("Enter shift value: ")
encoded_phrase = ''

for c in phrase:
	ascii_code = ord(c)
	if 65 <= ascii_code <= 90:
		ascii_code = ascii_code+value
		if ascii_code > 90:
			ascii_code = ascii_code % 90 + 64
	elif 97 <= ascii_code <=122:
		ascii_code = ascii_code+value
		if ascii_code > 122:
			ascii_code = ascii_code % 122 + 96
	c = chr(ascii_code)
	encoded_phrase = encoded_phrase + c

print "The encoded phrase is:",encoded_phrase