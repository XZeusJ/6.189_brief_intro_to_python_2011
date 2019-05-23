# Write any helper functions you need here.
import string
def split_str(s):
	return s.split()

def pig_latin(word):
    # word is a string to convert to pig-latin
    ##### YOUR CODE HERE #####
    VOWELS = ['a','e','i','o','u']
    NOTATION = [',','.','?','!','?']
    if word[-1] in NOTATION:
    	if word[0] in VOWELS:
    		return word[:-1] + "hay" + word[-1]
    	else:
    		return word[1:-1] + word[0] + "ay" + word[-1]
    else:
    	if word[0] in VOWELS:
        	return word + "hay"
    	else:
        	return word[1:] + word[0] + "ay"

def handle_str(s):
	splited_str = split_str(s)
	return string.join([pig_latin(x) for x in splited_str])

# Test Cases
##### YOUR CODE HERE #####
phrase = raw_input("Enter the sentence: ")
while phrase != 'QUIT':
	print handle_str(phrase)
	phrase = raw_input("Enter the sentence: ")