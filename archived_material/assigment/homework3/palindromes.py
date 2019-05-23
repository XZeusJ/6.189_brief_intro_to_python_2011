import operator
import copy
def is_palindrome(s):
	split_s = [x for x in s]
	split_s_r = [split_s[-(i+1)] for i in range(len(split_s))]

	# print split_s
	# print split_s_r

	flag = True
	for i in range(len(split_s)):
		flag = flag and split_s[i] == split_s_r[i]
	return flag


print is_palindrome('a b c')
print is_palindrome('aa b cc')
print is_palindrome('ac b ca')
print is_palindrome('yummy')
print is_palindrome('ymdmy')
print is_palindrome('able was i ere i saw elba')
print


