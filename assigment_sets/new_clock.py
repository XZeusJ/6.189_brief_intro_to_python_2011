from graphics import *
import math

SECOND = [x for x in range(0,60)]
RAW_THETA = [x for x in range(360, 0, -6)]
THETA = RAW_THETA[45:] + RAW_THETA[:45]
DX = [math.cos(math.radians(THETA[i])) for i in range(len(THETA))]
DY = [-math.sin(math.radians(THETA[i])) for i in range(len(THETA))]

class Clock:
	def __init__(self, hour, minute, second, pos):
		self.hour = hour
		self.minute = minute
		self.second = second
		self.all_seconds = hour*3600 + minute * 60 + second
		self.pos = pos

	def makeTime(self):
		if self.all_seconds / 3600 == 24: self.all_seconds = 0
		self.hour = self.all_seconds // 3600
		self.minute = self.all_seconds % 3600 // 60
		self.second = self.all_seconds % 60

class AnalogClock(Clock):
	def __init__(self, hour, minute, second, pos=Point(150,150)):
		Clock.__init__(self,hour,minute,second,pos)

	def set_face(self, color='pink', radius=100):
		self.radius =  radius
		self.face = Circle(self.pos, radius)
		self.face.setFill(color)

	def get_p2(self):
		self.pointer_length = self.radius * 0.9
		x1 = self.pos.x
		y1 = self.pos.y
		x2 = x1 + DX[self.second] * self.pointer_length
		y2 = y1 + DY[self.second] * self.pointer_length
		return Point(x2,y2)

	def get_pointer(self):
		p2 = self.get_p2()
		self.second_pointer = Line(self.pos, p2)

	def draw_pointer(self,win):
		self.second_pointer.draw(win)

	def undraw_pointer(self):
		self.second_pointer.undraw()

	def tick(self, win):
		# add 1s to time
		self.all_seconds += 1
		self.makeTime()

		self.undraw_pointer()
		self.get_pointer()
		self.draw_pointer(win)

	def animate(self, win,n):
		if n > 0:
			self.tick(win)
			win.after(1000, self.animate, win, n-1)

	def draw(self,win):
		self.set_face()
		self.face.draw(win)

		self.get_pointer()
		self.animate(win,1000)


# TEST about analog clock
new_win = GraphWin("Analog Clock", 300, 300)
aclock = AnalogClock(15, 30, 0)
aclock.draw(new_win)
new_win.mainloop()


class DigitalClock(Clock):
	def __init__(self, hour, minute, second, pos=Point(150,150)):
		Clock.__init__(self,hour,minute,second,pos)

	def time_str(self):
		s = str(self.hour % 12) + ":" + str(self.minute) + ":" + str(self.second) + " "
		self.str = s

	def set_text(self, size = 20, style = 'bold italic'):
		self.fontsize = size

		self.time_str()
		self.text = Text(self.pos, self.str)

		self.text.setStyle(style)
		self.text.setSize(size)

	def set_face(self,color='green', padding = 30):
		x1 = self.pos.x - self.fontsize * len(self.str) / 2 - padding * 0.5
		x2 = self.pos.x + self.fontsize * len(self.str) / 2 + padding * 0.5
		y1 = self.pos.y - padding
		y2 = self.pos.y + padding

		self.body = Rectangle(Point(x1,y1),Point(x2,y2))
		self.body.setFill(color)

	def tick(self,win):
		self.all_seconds += 1
		self.makeTime()
		s = str(self.hour) + ":" + str(self.minute) + ":" + str(self.second) + " "
		self.text.setText(s)

	def animate(self, win, n):
		if n > 0:
			self.tick(win)
			win.after(1000, self.animate, win, n-1)

	def draw(self, win):
		self.set_text()
		self.set_face()
		self.body.draw(win)
		self.text.draw(win)
		self.animate(win, 1000)

# TEST about digital clock
# new_win = GraphWin("Digital Clock", 300, 300)
# clock = DigitalClock(15, 30, 0)
# clock.draw(new_win)
# new_win.mainloop()
