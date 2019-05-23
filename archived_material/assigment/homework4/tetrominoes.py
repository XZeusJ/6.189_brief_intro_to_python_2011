from graphics import *

class Block(Rectangle):
	def __init__(self, position, color):
		# deal with converting the Point into pixels
		i = position.getX()
		j = position.getY()
		len_block = 25
		x1 = (i-1)*len_block
		y1 = (j-1)*len_block
		x2 = i*len_block
		y2 = j*len_block
		
		# initialize the Rectangle superclass
		# and fill the color
		Rectangle.__init__(self,Point(x1,y1), Point(x2,y2))
		self.setFill(color)

class Shape:
	def __init__(self, list_blocks, color):
		self.blocks = [Block(coord, color) for coord in list_blocks]

	def draw(self, win):
		for block in self.blocks:
			block.draw(win)

class I_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 2, center.y),
				  Point(center.x - 1, center.y),
				  Point(center.x    , center.y),
				  Point(center.x + 1, center.y),]
		Shape.__init__(self, coords, "blue")

class J_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x    , center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x + 1, center.y + 1)]
		Shape.__init__(self, coords, "orange")

class L_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x    , center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x - 1, center.y + 1)]
		Shape.__init__(self, coords, "purple")

class O_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x    , center.y),
				  Point(center.x - 1, center.y + 1),
				  Point(center.x    , center.y + 1)]
		Shape.__init__(self, coords, "red")

class S_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y + 1),
				  Point(center.x    , center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x, center.y + 1)]
		Shape.__init__(self, coords, "green")

class T_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x    , center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x    , center.y + 1)]
		Shape.__init__(self, coords, "yellow")

class Z_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x    , center.y),
				  Point(center.x    , center.y + 1),
				  Point(center.x + 1, center.y + 1)]
		Shape.__init__(self, coords, "pink")


def main():

	win = GraphWin("Tetrominoes", 900, 150)
	# a list of shape classes
	tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
	x = 3
	for tetromino in tetrominoes:
		shape = tetromino(Point(x, 2))
		shape.draw(win)
		x += 4
	win.mainloop()

main()