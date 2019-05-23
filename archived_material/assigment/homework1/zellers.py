#Zhangjin Xiao

print "Enter your date of birth:"
month = input("Month? Please enter a number ")
B = input("Day? ")
year = input("Year? ")
if month == 1 or month == 2:
	A = month + 10
	year = year-1
else:
	A = month - 2
C = year % 100
D = year / 100

W = (13*A -1) /5
X = C/4
Y = D/4
Z = W+X+Y+B+C-2*D
R = Z % 7

print R