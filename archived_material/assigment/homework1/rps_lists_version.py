# rps_example2.py

# This example uses lists to test valid input and see who won

VALID_OPTIONS = ["rock", "paper", "scissors"]

# A list of lists. Describes the three winning combos, where
#  the first item is the winner and the second is the loser.
WINNING_COMBOS = [["paper", "rock"], ["rock", "scissors"], ["scissors", "paper"]]

def rps(player1, player2):
    '''
    Plays a game of Rock, Paper, Scissors.
    player1, player2 must be strings - either "rock", "paper", or
      "scissors". Returns a string displaying who won the round.
    '''

    player1 = player1.lower()
    player2 = player2.lower()
    # Turn player1's input into lowercase and see if it is in the list
    #  VALID_OPTIONS. If not it is invalid.
    if player1 not in VALID_OPTIONS:
        return "Invalid input - must be 'paper', 'rock', or 'scissors'; got '" + str(player1) +"'"
    if player2 not in VALID_OPTIONS:
        return "Invalid input - must be 'paper', 'rock', or 'scissors'; got '" + str(player2) + "'"

    if player1 == player2:
        return "Tie game"
    elif [player1, player2] in WINNING_COMBOS:
        return "player 1 wins!"
    elif [player2, player1] in WINNING_COMBOS:
        return "player 2 wins!"
    else:
        # I think I covered every possible case in the above "if" and "elif"
        # statements, so I don't think it is possible to reach this else
        # statement.
        return "Shouldn't get here" 

print rps("paper","rock")
print rps("paper","paper")
print rps("paper","ROCK")
