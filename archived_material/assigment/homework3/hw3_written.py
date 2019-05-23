# def negate(num):
# 	return -num
# def large_num(num):
# 	return (num > 10000)
# b = 20
# num = negate(b)
# neg_b = num
# print "b:", b, "neg_b:", neg_b
# big = large_num(b)
# print "b is big:", big


print "Think of a number between 1 and 100, but don't tell me what you choose."
min_n = 1
max_n = 100
right_answer = False

while not right_answer:
	mid_n = (max_n + min_n + 1)/2
 	answer = raw_input('Is it ' + str(mid_n) + '? ')
 	if answer[0] == 'y':
 		right_answer = True
 	elif answer.startswith('higher'):
 		min_n = mid_n + 1
 	elif answer.startswith('lower'):
 		max_n = mid_n - 1
 	else:
 		print "Sorry, I don't understand your answer."

print "Woohoo! I got it!"