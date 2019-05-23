# Name:Zhangjin Xiao
# Section: ECS
# Date:03/30/19
# hw1.py
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/assignments/MIT6_189IAP11_hw1.pdf


##### Template for Homework 1, exercises 1.2-1.5 ######

print "********** Exercise 1.2 **********"

# Do your work for Exercise 1.2 here
print "  |  |  \n--------\n  |  |  \n--------\n  |  |  "


print "********** Exercise 1.3 **********"

# Do your work for Excercise 1.3 here. Hint - how many different
# variables will you need?
erect_line = "  |  |  "
horizontal_line = "--------"
change_line = "\n"
print erect_line,change_line,horizontal_line,change_line,erect_line,change_line,horizontal_line,change_line,erect_line


print "********** Exercise 1.4 **********"
print "********* Part II *************"
a = 3*5/(2+3)
b = (7+9)**0.5*2
c = (4-7)**3
d = (-19+100)**0.25
e = 6 % 4
print a,b,c,d,e

print "********* Part III *************"
f1 = (2+3)**2
f2 = 2+3**2
print f1,f2

print "********** Exercise 1.5 **********"
first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
print "Enter your date of birth:"
month = raw_input("Month? ")
day = raw_input("Day? ")
year = raw_input("Year? ")
print last_name, first_name, "was born on", month,day+",", year+"."

