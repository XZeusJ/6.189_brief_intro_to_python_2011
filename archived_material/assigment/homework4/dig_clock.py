from graphics import *


class DigitalClock():

	def __init__(self, hour, minute, second, pos=Point(150,150)):
		self.hour = hour
		self.minute = minute
		self.second = second
		self.all_seconds = hour*3600 + minute * 60 + second
		self.pos = pos


	def time_str(self):
		s = str(self.hour % 12) + ":" + str(self.minute) + ":" + str(self.second) + " "
		# if self.hour >= 12: s += "PM"
		# else: s += "AM"
		self.str = s

	def set_text(self, size = 20, style = 'bold italic'):
		self.fontsize = size

		self.time_str()
		self.text = Text(self.pos, self.str)

		self.text.setStyle(style)
		self.text.setSize(size)

	def draw_face(self,color='green', padding = 30):
		x1 = self.pos.x - self.fontsize * len(self.str) / 2 - padding * 0.5
		x2 = self.pos.x + self.fontsize * len(self.str) / 2 + padding * 0.5
		y1 = self.pos.y - padding
		y2 = self.pos.y + padding

		self.body = Rectangle(Point(x1,y1),Point(x2,y2))
		self.body.setFill(color)

	def makeTime(self):
		if self.all_seconds / 3600 == 24: self.all_seconds = 0
		self.hour = self.all_seconds // 3600
		self.minute = self.all_seconds % 3600 // 60
		self.second = self.all_seconds % 60
		return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second) + " "

	def tick(self,win):
		self.all_seconds += 1
		self.text.setText(self.makeTime())
		
	def animate(self, win, n):
		if n > 0:
			self.tick(win)
			win.after(100, self.animate, win, n-1)
	
	def draw(self, win):
		self.set_text()
		self.draw_face()
		self.body.draw(win)
		self.text.draw(win)
		self.animate(win, 1000)


new_win = GraphWin("Digital Clock", 300, 300)
clock = DigitalClock(15, 30, 23)
clock.draw(new_win)

new_win.mainloop()

