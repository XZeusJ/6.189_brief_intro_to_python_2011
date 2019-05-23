class Stack:
	def __init__(self, obj = []):
		self.obj = obj

	def __str__(self):
		str_self = ''
		for x in self.obj:
			str_self += str(x) + ' '
		return str_self

	def push(self,num):
		self.obj.append(num)
		print self

	def pop(self):
		length = len(self.obj)
		if length >= 1:
			print self.obj[-1]
			self.obj = self.obj[:-1]
		if length == 0:
			print "The stack is empty"

