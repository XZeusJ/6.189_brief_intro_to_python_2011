#2.5 Python Style

#2.5.1 Normalize a vector
def mag(v):
	return math.sqrt(sum([vi**2 for vi in v]))
def normalize3(v):
	magv = mag(v)
	return [vi/magv for vi in v]

# 2.5.2 Perimeter of a polygon
def perim(vertices):
	result = 0
	for i in range(len(vertices)-1):
		result = result + pointDist(vertices[i],vertices[i+1])
	return result + pointDist(vertices[-1],vertices[0])
def pointDist(p1,p2):
	return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))

def pointDist(p1,p2):
	return math.sqrt(sum([(c1 - c2)**2 for (c1, c2) in zip(p1, p2)]))
# For this to make sense, you have to understand zip, example:
# zip([1, 2, 3],[4, 5, 6])
# [(1, 4), (2, 5), (3, 6)]

# 2.5.3  Bank transfer 
acctName = 0
acctBalance = 1
acctFee = 2
def deposit(a, amt):
	a[acctBalance] = a[acctBalance] + amt - a[acctFee]
def transfer(a1, a2, amt):
	deposit(a1, -amt)
	deposit(a2, amt)

# 2.5.4  Coding examples
#the return is true if a is a subset of b
def isSubset(a,b):
	return reduce(operator.and_, [x in b for x in a]) 



# An?alternative?is?to?do?it?recursively:?
def isSubset(a, b):
	if a == []:
		return True
	else:
		return a[0] in b and isSubset(a[1:], b)
# We?could?go?even?farther?in?compressing?the?recursive?solution:?
def isSubset(a, b):
	return a == None or a[0] in b and isSubset(a[1:], b)

def isSubset(a, b):
	for x in a:
		if not x in b:
			return False
	return True

def isSubset(a, b):
	result = True
	for x in a:
		result = result and x in b
	return result

# If you ever find yourself writing: 
# if condition:
# 	return True
# else:
# 	return False
# You could always replace that with 
# return condition
# which is shorter and clearer. 

#EXERCISE 2.4.
def issubset(a,b):
	i = 0
	j = 0
	while i < len(a):
		c = False
		while j < len(b):
			if a[i] == b[j]:
				c =True
				# print c,i,j
				break
			j = j+1
		if c:
			c = False
			j = 0
			i = i+1
		else:
			return False
	return True
print issubset([1,2],[1,3,2])
# print isSubset([1,2],[1,3,2])

def issubset(a,b):
	foundAllAsSoFar = True
	for i in a:
		foundThisA = False
		for j in b:
			foundThisA = foundThisA or i == j
		foundAllAsSoFar = foundThisA and foundAllAsSoFar
	return foundAllAsSoFar
print issubset([1,2,3],[3,2,1])
