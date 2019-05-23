import math

class Point:
	pass

class Rectangle:
	pass


p = Point()
q = Point()

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

p.x = 3.0
p.y = 3.0
q.x = 4.0
q.y = 4.0

def printPoint(p):
	print '(' + str(p.x) + ', ' + str(p.y) + ')'

def distance(p,q):
	dx = p.x - q.x
	dy = p.y - q.y
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result

def findCenter(box):
	p = Point()
	p.x = box.corner.x + box.width/2.0
	p.y = box.corner.y - box.height/2.0
	return p

center = findCenter(box)
printPoint(center)

def growRect(box,dwidth,dheight):
	import copy
	newBox = copy.deepcopy(box)
	newBox.width = newBox.width + dwidth
	newBox.height = newBox.height + dheight

def moveRect(box,dx,dy):
	import copy
	newBox = copy.deepcopy(box)
	newBox.corner.x = dx
	newBox.corner.y = dy