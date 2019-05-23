#coding=utf-8

#Zhangjin Xiao
#6.189 Sample Exam

# 1.(a)
def quad(a, b, c):
	import math
	if a == 0: return "error"
	discriminant = b**2 - 4*a*c
	if discriminant < 0: return "complex num"
	elif discriminant > 0:
		r1 = (-b + math.sqrt(discriminant))/ (2*a)
		r2 = (-b - math.sqrt(discriminant))/ (2*a)
		return r1, r2
	else:
		return (-b + math.sqrt(discriminant)) / (2*a)

# print quad(1,4,1)
# print quad(1,5,1)
# print quad(1,2,3)
# print quad(0,5,1)
# print

# 1.(b)
def cquad(a, b, c):
	import math
	import cmath
	if a == 0: return "error"
	judge = b**2 - 4*a*c
	if judge < 0:
		r1 = (-b + cmath.sqrt(judge))/ (2*a)
		r2 = (-b - cmath.sqrt(judge))/ (2*a)
		return r1, r2
	elif judge > 0:
		r1 = (-b + math.sqrt(judge))/ (2*a)
		r2 = (-b - math.sqrt(judge))/ (2*a)
		return r1, r2
	else:
		return (-b + math.sqrt(judge)) / (2*a)

# print cquad(1,4,1)
# print cquad(1,5,1)
# print cquad(1,2,3)
# print cquad(0,5,1)
# print

#2
def poly(x,list):
	result = 0
	for i in range(len(list)):
		result += list[i] * (x ** (len(list)-1-i))
	return result

# print poly(2,[2,2,3])
# print

#3
def make_change(cost, paid):
    change=paid-cost #calculate the change due
    bills={20:0,10:0,5:0,2:0,1:0} #dictionary that maps each bill to the amount of it
    bill_list=bills.keys() #bill_list is a list of the available bills
    bill_list.sort() #sort it in ascending order
    bill_list.reverse() #now reverse it to be in descending order
                        #this is to make sure you get the smallest number of bills
    for bill in bill_list: 
        while change >=bill: 
            bills[bill]+=1 #increment the amount of that bill
            change-=bill #decrease the change by that bill
            
    print "Change is:"
    for bill in bill_list:
        if bills[bill] == 1:
            print bills[bill], bill, "dollar bill"
        elif bills[bill] > 1:
            print bills[bill], bill, "dollar bills"

    #return bills #return the dictionary with amounts of each bill needed

make_change(1, 6)
make_change(3, 109)

#4 (a)
def sepstr(s, target):
	l = s.split()
	return [i for i in range(len(l)) if l[i] == target]

# print sepstr('we dont dont slkdfjklj sdkfj dont', 'dont')

#4 (b)
def invIndex(s):
	l = s.split()
	dic = {}
	for word in l:
		dic[word] = sepstr(s, word)
	return dic

d = invIndex('we dont dont we slkdfjklj sdkfj dont')
print d
print d['we'] 
