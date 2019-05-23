#Zhangjin Xiao
#my version about optional recursion exercises

#1
def multiply(a_list):
	if a_list == []:
		return 1
	else:
		return a_list[0] * multiply(a_list[1:])

# print multiply([3,4,2])
# print multiply([3,10])

#1 revised
def RecMult(num_1, num_2):
	if num_1 == 1:
		return num_2
	elif num_1 == 0:
		return 0
	else:
		return num_2 + RecMult(num_1 - 1, num_2)

#2
def power(base,exp):
	if exp == 0:
		return 1
	else:
		return base * power(base, exp-1)

# print power(5,2)
# print power(4,1)
# print power(3,3)

#3
def show_n_to_zero(n):
	if n == 0:
		return n
	else:
		print n
		return show_n_to_zero(n-1)

# show_n_to_zero(10)

#4
def show_zero_to_n(n):
	if n == 0:
		return n
	else:
		print show_zero_to_n(n-1)
		return n
# show_zero_to_n(10)

#5
def reversed_copy(a_str):
	if len(a_str) == 0:
		return ''
	else:
		return a_str[-1] + reversed_copy(a_str[:-1])

# assert reversed_copy("Sxzj") == "jzxS"
# assert reversed_copy("") == ""
	
def RecIsPrime(m):
	def PrimeHelper(m, j):
		if j == 1:
			return True
		else:
			return m % j != 0 and PrimeHelper(m, j - 1)
	return PrimeHelper(m, m-1)

