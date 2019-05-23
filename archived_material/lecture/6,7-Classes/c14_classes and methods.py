class Time:
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def printTime(time):
		print str(time.hours) + ":" + \
			  str(time.minutes) + ":" + \
			  str(time.seconds)

	def convertToSeconds(self):
		minutes = self.hours * 60 + self.minutes
		self.total_seconds = minutes * 60 + self.seconds

	def makeTime(self,total_seconds):
		self.hours = total_seconds // 3600
		self.minutes = (total_seconds%3600) // 60
		self.seconds = total_seconds % 60

	def increment(self,seconds):
		self.convertToSeconds()
		self.total_seconds = seconds + self.total_seconds
		self.makeTime(self.total_seconds)

	def  after(self, time2):
		if self.hours > time2.hours:
			return 1
		if self.hours < time2.hours:
			return 0
		if self.minutes > time2.minutes:
			return 1
		if self.minutes < time2.minutes:
			return 0
		if self.seconds > time2.seconds:
			return 1
		return 0


currentTime = Time(9,14,30)
currentTime.printTime()
currentTime.increment(-600)
currentTime.printTime()
doneTime = Time(9,14,30)
if doneTime.after(currentTime):
	print "the bread is not done yet."


class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)


	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return self.x * other.x + self.y * other.y

	def __rmul__(self,other):
		return Point(other * self.x, other * self.y)

	def reverse(self):
		self.x , self.y = self.y, self.x

# p1 = Point(3,4)
# p2 = Point(5,7)
# p3 = p1-p2
# print p3

class Address:
	def __init__(self, number = 0, street_name = ''):
		self.number = number
		self.street_name = street_name
	def __str__(self):
		return "Number "+str(self.number)+": "+self.street_name

a1 = Address(1,'omg')
print (a1)

class Clock:
	def __init__(self, time):
		self.time = time
	def print_time(self):
		time = "6:30"
		print self.time
clock = Clock("5:30")
clock.print_time()

class Clock:
	def __init__(self, time):
		self.time = time
	def print_time(self, time):
		print time
clock = Clock("5:30")
clock.print_time("10:30")

class Clock:
	def __init__(self, time):
		self.time = time
	def print_time(self):
		print self.time
boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()