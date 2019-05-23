from graphics import *
from wheel import *

class Car:

	def __init__(self, wheel1_center, wheel1_radius, wheel2_center, wheel2_radius, rect_height):
		self.wheel1 = Wheel(wheel1_center, 0.6*wheel1_radius, wheel1_radius)
		self.wheel2 = Wheel(wheel2_center, 0.6*wheel2_radius, wheel2_radius)
		self.body = Rectangle(Point(wheel1_center.x -22.5 , wheel1_center.y- rect_height ), Point( wheel2_center.x + 22.5, wheel2_center.y ))

	def draw(self, win):
		self.wheel1.draw(win)
		self.wheel2.draw(win)
		self.body.draw(win)

	def undraw(self):
		self.body.undraw()

	def set_color(self, tire_color, wheel_color, body_color ):
		self.wheel1.set_color(wheel_color,tire_color)
		self.wheel2.set_color(wheel_color,tire_color)
		self.body.setFill(body_color)

	def move(self,dx,dy):
		self.wheel1.move(dx,dy)
		self.wheel2.move(dx,dy)
		self.body.move(dx,dy)

	def animate(self, win, dx, dy, n):
		if n > 0:
			self.move(dx, dy)
			win.after(100, self.animate, win, dx, dy, n-1)

def main():

	new_win = GraphWin('A Car', 700, 300)

	car1 = Car(Point(100, 100), 15, Point(200,100), 15, 40)
	car1.draw(new_win)

	car1.set_color('black', 'grey', 'pink')

	car1.undraw()
	# car1.animate(new_win, 1, 0, 400)

	new_win.mainloop()


main()

