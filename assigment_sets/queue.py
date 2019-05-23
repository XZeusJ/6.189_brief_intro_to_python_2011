class Queue:
	def __init__(self, obj = []):
		self.obj = obj

	def __str__(self):
		str_self = ''
		for x in self.obj:
			str_self += str(x) + ' '
		return str_self

	def insert(self,num):
		self.obj.append(num)
		print self

	def remove(self):
		length = len(self.obj)
		if length >= 1:
			print self.obj[0]
			self.obj = self.obj[1:]
		if length == 0:
			print "The queue is empty"

