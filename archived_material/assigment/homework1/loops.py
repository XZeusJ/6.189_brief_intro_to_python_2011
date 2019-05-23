#Zhangjin Xiao
#MECS

for num in range(7,15):
	print num

print "**"

for num in range(2,12,2):
	print num

print "**"

for num in range(12,2,-2):
	print num

# A while loop example

# Initialize a counter
count = 1
print "Count is initially", count
# Want to keep looping until the counter is bigger than 100
while count < 100:
   count = count * 9
   print "Now count is", count

# When we get here, the while loop is done - so count must be > 100
print "the counter is", count

#1
for num in range(1,11):
	print 1.0/num

#2
num = input("Please input your countdown number:")

if num > 0:
	while num >= 0:
		print num
		num -= 1
elif num < 0:
	while num <= 0:
		print num
		num += 1
else:
	print "The Number is Already 0!"

#3
base = input("what's base?")
exp = input("what's exp?")

result = base
for num in range(1,exp):
	result *= base
print result

#4
num = input("Please enter a nuber that is divisible by 2: ")
while num % 2.0 != 0:
	num = input("You Nerd! Enter a nuber that is divisible by 2! ")
print "Thanks God, You do it right!"