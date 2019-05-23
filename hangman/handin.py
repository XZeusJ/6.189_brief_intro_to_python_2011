#Zhangjin Xiao

l = [7,8,7,0]
l2 = [7,8,7,7]


import operator
def at_least_less_than_n(l,n):
 	return reduce(operator.or_,[x < n for x in l])

# print at_least_less_than_n(l,6)

def at_least_less_than_n_2(l,n):
	less_than_n = False
	for x in l:
		less_than_n = less_than_n or (x<n)
	return less_than_n
print at_least_less_than_n_2(l,6)
print at_least_less_than_n_2(l2,6)

