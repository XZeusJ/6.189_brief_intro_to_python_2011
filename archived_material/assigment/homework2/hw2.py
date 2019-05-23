# Name:Zhangjin Xiao
# Section:ECS
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

#input player1,2's hand figure
def rps(p1,p2):
	#Rock,Scissors & Paper Game

	#trunacte whitespace
	while p1[-1] == " ":
		p1 = p1[:-1]
	while p2[-1] == " ":
		p2 = p2[:-1]	

	#first judge the valid of input
	if p1 != "rock" and p1 != "scissors" and p1 != "paper":
		return "This is not a valid object selection"
	elif p2 != "rock" and p2 != "scissors" and p2 != "paper":
		return "This is not a valid object selection"
	#the rule of RS&P game
	elif p1 == p2:
		return "Tie."
	elif p1 == "rock":
		if p2 == "scissors":
			return "Player 1 wins."
		else:
			return "Player 2 wins."
	elif p1 == "scissors":
		if p2 == "rock":
			return "Player 2 wins."
		else:
			return "Player 1 wins."
	elif p1 == "paper":
		if p2 == "rock":
			return "Player 1 wins."
		else:
			return "Player 2 wins."
	else:
		return "somewhere has problem."

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####
print rps('rock','paper')
print rps('rock','rock')
print rps('scissors','paper')

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m,n):
	if n == 0:
		return "Can't not divisible by 0"
	if m % n == 0:
		return True
	else:
		return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(a,b):
	if a == b:
		return False
	else:
		return True

# Test cases for not_equal
##### YOUR CODE HERE #####
print not_equal(1,3)
print not_equal(3,3) #print 3 != 3


# ********** Exercise 2.3 ********** 
import math
## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
	return a*b + c

## 2 - Equations
##### YOUR CODE HERE #####

# Test Cases
angle_test = multadd(1/2.0,math.cos(math.pi/4),math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(2,math.log(12,7),math.ceil(276/19.0))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
	return multadd(x,math.exp(-x),multadd(-1,math.exp(-x),1)**(1/2.0))

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********
import random
## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3(lo,hi):
	if random.randint(lo,hi) % 3 == 0:
		return True
	else:
		return False

# Test Cases
##### YOUR CODE HERE #####
print rand_divis_3(0,100)
print rand_divis_3(0,100)

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(side,dice):
	for num in range(dice):
		print random.randint(1,side)
	return "That's all!"

# Test Cases
##### YOUR CODE HERE #####                            
print roll_dice(6,3)
print roll_dice(8,2)

# ********** Exercise 2.5 **********
import math
import cmath
# code for roots function
##### YOUR CODE HERE #####   
def roots(b,a,c):
	judge = b**2.0 - 4*a*c
	if judge > 0:
		return (-b+math.sqrt(judge))/(2.0*a),(-b-math.sqrt(judge))/(2.0*a)
	elif judge == 0:
		return -b/(2.0*a)
	else:
		return (-b+cmath.sqrt(judge))/(2.0*a),(-b-cmath.sqrt(judge))/(2.0*a)

# Test Cases
##### YOUR CODE HERE #####   
print roots(3,1,1)
print roots(4,1,4)
print roots(3,2,2)