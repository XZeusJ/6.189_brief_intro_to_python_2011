#concepts about "string" type in python
#record from thinkCSpy.pdf (Users\39438\OneDrive\Mit_ocw\MIT6.189\Python)

'''
Strings
	• are ordered sets of characters
	• only characters type
'''

#7.2 Length
length = len(fruit)
last = fruit[length-1]
last = fruit[-1]

#7.3 Traversal and the for loop
index = 0
while index < len(fruit):
	letter = fruit[index]
	print letter
	index = index + 1
for char in fruit:
	print char
	
#7.4 String slices
#If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.
# Thus:
>>> fruit = "banana"
>>> fruit[:3]
’ban’
>>> fruit[3:]
’ana’
# What do you think s[:] means?

# 7.6 Strings are immutable
# Strings are immutable, which means you can’t change an existing string. The best you can do is create a new string that is a variation on the original:
greeting = "Hello, world!"
newGreeting = ’J’ + greeting[1:]
print newGreeting

# 7.9 The string module
>>> import string
# The string module includes a function named find that does the same thing as the function we wrote. To call it we have to specify the name of the module and the name of the function using dot notation.
>>> fruit = "banana"
>>> index = string.find(fruit, "a")
>>> print index

# 7.10 Character classification
# We can use these constants and find to classify characters. For example, if find(lowercase, ch) returns a value other than -1, then ch must be lowercase:
def isLower(ch):
	return string.find(string.lowercase, ch) != -1
# Alternatively, we can take advantage of the in operator, which determines whether a character appears in a string:
def isLower(ch):
	return ch in string.lowercase
# As yet another alternative, we can use the comparison operator:
def isLower(ch):
	return ’a’ <= ch <= ’z’
