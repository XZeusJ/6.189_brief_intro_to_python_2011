#Zhangjin Xiao
#Rock,Scissors & Paper Game

#input player1,2's hand figure
p1 = raw_input("Player 1? ")
p2 = raw_input("Player 2? ")

#trunacte whitespace
while p1[-1] == " ":
	p1 = p1[:-1]
while p2[-1] == " ":
	p2 = p2[:-1]	

#first judge the valid of input
if p1 != "rock" and p1 != "scissors" and p1 != "paper":
	print "This is not a valid object selection"
elif p2 != "rock" and p2 != "scissors" and p2 != "paper":
	print "This is not a valid object selection"
#the rule of RS&P game
elif p1 == p2:
	print "Tie."
elif p1 == "rock":
	if p2 == "scissors":
		print "Player 1 wins."
	else:
		print "Player 2 wins."
elif p1 == "scissors":
	if p2 == "rock":
		print "Player 2 wins."
	else:
		print "Player 1 wins."
elif p1 == "paper":
	if p2 == "rock":
		print "Player 1 wins."
	else:
		print "Player 2 wins."
else:
	print "somewhere has problem."

