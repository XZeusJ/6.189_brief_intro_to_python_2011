# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
def list_intersection(list1,list2):
    raw_list = [x for x in list1 for y in list2 if x == y]
    return  [raw_list[i] for i in range(len(raw_list)) if raw_list[i] not in raw_list[0:i]]


# Test Cases for Exercise 3.1
# print list_intersection([1,3,5],[5,3,1])
# print list_intersection([1,3,6,9],[10,14,3,72,9])
# print list_intersection([2,3],[3,3,3,2,10])
# print list_intersection([2,4,6],[1,3,5])

# **********  Exercise 3.2 **********


# Define your function here
import math
def ball_collide(ball1, ball2):
    x1,y1,r1 = ball1
    x2,y2,r2 = ball2
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return abs(r1+r2) >= dist

# Test Cases for Exercise 3.2
# print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
# print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
# print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {}

def add_class(class_num, desc):
    my_classes[class_num] = desc


# Here, use add_class to add the classes you're taking next term
# add_class('6.189', 'Introduction to Python')
# add_class('6.01', 'Introduction to EECS')

def print_classes(course):
    course = str(course)

    flag = True
    for title in my_classes.keys():
        flag = flag and (title[0] != course)
    if flag:
        print "No Course " + course +" classes taken"
    else:
        for title in my_classes.keys():
            if title[0] == course:
                print title+" - "+my_classes[title]
# print_classes(6) 


# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####


# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    if len(l1) == len(l2):
        for i in range(len(l1)):
            comb_dict[l1[i]]=l2[i]
    else:
        return "Something was wrong!"
    return comb_dict

combined_dict = combine_lists(NAMES, AGES) # Finish this line...
# print combined_dict

def people(age):
    return [x for x in combined_dict if combined_dict[x] == age]

# Test Cases for Exercise 3.4 (all should be True)
# print 'Dan' in people(18) and 'Cathy' in people(18)
# print 'Ed' in people(19) and 'Helen' in people(19) and\
      # 'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
# print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
# print people(21) ==   ['Bob']
# print people(22) ==   ['Kelly']
# print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
    MONTHS_NUMBERS = [11,12,1,2,3,4,5,6,7,8,9,10]
    month_dict = combine_lists(MONTHS,MONTHS_NUMBERS)

    A = month_dict[month]
    B = day
    C = year % 100
    D = (year - year % 100) / 100
    if month == 'January' or month == 'February':
        C -= 1

    W = (13*A - 1) / 5
    X = C / 4
    Y = D / 4
    Z = W + X + Y + B + C - 2*D
    R = Z % 7

    DAYS_NUMBERS = [0,1,2,3,4,5,6]
    DAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    day_dict = combine_lists(DAYS_NUMBERS,DAYS)

    return day_dict[R]

# Test Cases for Exercise 3.5
# print zellers("March", 11, 1940) == "Monday" # This should be True

low= 0
high = 5
import random
for i in range(10):
    x = random.random() * (high-low+1) + low
    # print int(x)

previous = {0:1, 1:1}

def fibonacci(n):
    if previous.has_key(n):
        return previous[n]
    else:
        newValue = fibonacci(n-1) + fibonacci(n-2)
        previous[n] = newValue
        return newValue
print fibonacci(5)
