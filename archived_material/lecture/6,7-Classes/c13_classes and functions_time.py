class Time:
	pass

time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30

def printTime(t):
	return str(t.hours)+":"+str(t.minutes)+":"+str(t.seconds)

# print printTime(time)

# ***********this is Algorithms
def convertToSeconds(t):
	minutes = t.hours * 60 + t.minutes
	seconds = minutes * 60 + t.seconds
	return seconds

# ***********this is Algorithms
def makeTime(seconds):
	time = Time()
	time.hours = seconds // 3600
	time.minutes = (seconds%3600) // 60
	time.seconds = seconds%60
	return time
print printTime(makeTime(2458))

def is_follow(t1,t2):
	return convertToSeconds(t2) - convertToSeconds(t1) == 1 

def increment(time,seconds):
	new_seconds = convertToSeconds(time) + seconds
	return makeTime(seconds)
print printTime(increment(time,3631))

