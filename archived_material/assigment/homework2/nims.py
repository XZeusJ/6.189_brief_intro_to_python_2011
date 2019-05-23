# Name:Zhangjin Xiao
# Section:
# nims.py

#judge is there number in the string?
def is_int(s):
	try:
		return int(s)
	except ValueError:
		return s

def play_nims(pile, max_stones):
	#use count to record how much turn the two player played
	count = 0
	while pile != 0:
		valid = False #keep a variable that tracks whether their answer is valid
		stone = is_int(raw_input("what's stones you prefer to take?")) #raw_input can input string, is_int can transfer str to int type
		#judge the valid of question
		while valid == False:			
			if isinstance(stone,int) == False:
				stone = is_int(raw_input("You shold input int type. Please enter again: "))
			elif stone > max_stones or stone < 0:
				stone = is_int(raw_input("Stones shold range from 0 to "+str(max_stones)+". Please enter again: "))
			elif pile - stone < 0:
				stone = is_int(raw_input("There is not so many stones to move. Please enter again: "))
			else:
				valid = True
		pile = pile - stone
		count += 1

	print "Game over"
	if count % 2 == 0:
		print "winner is plyer2"
	else:
		print "winner is plyer1"
play_nims(10,5)
