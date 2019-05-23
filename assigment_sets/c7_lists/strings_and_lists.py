# Name:
# Section:
# strings_and_lists.py

import operator
# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num
    return total

# Test cases
print "sum_all of [4, 3, 6] is:",sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:",sum_all([1, 2, 3, 4])



def cumulative_sum(number_list):
    # number_list is a list of numbers
    ##### YOUR CODE HERE #####
    c = number_list[0]
    result = [c]
    for i in range(len(number_list)-1):
        c += number_list[i+1]
        result.append(c)
    return result

    #method2
    # return [sum(number_list[:(i+1)]) for i in range(len(number_list))]

#Test cases
##### YOUR CODE HERE #####
print cumulative_sum([4,9,10,1])

# **********  Exercise 2.8 **********
def report_card():
# Test Cases
## In comments, show the output of one run of your function.
    classes = int(raw_input("How many classes did you take? "))
    name = []
    grade = []

    for i in range(classes):
        name.append(raw_input("What was the name of this class? "))
        grade.append(float(raw_input("What was your grade? ")))

    print "..."
    for i in range(classes):
        print name[i],"-",grade[i]
    print "Overall GPA  ", sum(grade)/classes
# Test Cases
## In comments, show the output of one run of your function.
# report_card()


# **********  Exercise 2.9 **********

# Write any helper functions you need here.
VOWELS = ['a','e','i','o','u']

def pig_latin(word):
    # word is a string to convert to pig-latin

    ##### YOUR CODE HERE #####
    if word[0] in VOWELS:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"

# Test Cases
##### YOUR CODE HERE #####
print pig_latin('boot')
print pig_latin('image')

# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####
#1
print [x**3 for x in range(1,11)]
#2
print [first+last for first in ['h','t']\
                for last in ['h','t']]
print [first+last for (first,last) in zip(['h','t'],['h','t'])]
#3
def vowels_in_string(strings):
    return [x for x in strings if x in 'aeiou']
print vowels_in_string('jjjj')
print vowels_in_string('jjsdfjaj')
#4
print [x+y for x in [10,20,30] for y in [1,2,3]]
result = []
for x in [10,20,30]:
    for y in [1,2,3]:
        result.append(x+y)
print result

# **********  Exercise OPT.2 **********
# If you do any work for this problem, submit it here 
#1
test = [12,'abc',None,[1,3,'2'],32]
def find_int_type(list):
    return [x for x in list if isinstance(x,int)]
print find_int_type(test)
#2
print [[x,y] for x in range(-5,6) for y in range(0,11) if y == x**2 +1]
#3
import math
print [[x,y] for x in range(-5,6) for y in range(-5,6) if math.sqrt(x**2+y**2) == 5]
#4...