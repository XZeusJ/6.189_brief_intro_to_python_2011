# Name:Zhangjin Xiao
# Section: Computer Science
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    flag = True
    for letter in secret_word:
        flag = flag and (letter in letters_guessed)
    return flag
# print word_guessed()

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    character_list = []
    for letter in secret_word:
        if letter in letters_guessed:
            character_list.append(letter)
        else:
            character_list.append("-")

    not_guess_character_list = []
    for letter in 'abcdefghigklmnopqrstuvwxyz':
        if letter not in letters_guessed:
            not_guess_character_list.append(letter)


    return "Already guessed: " + join(character_list,'') + "\nHaven't been guessed for now: " + join(not_guess_character_list,'')

# print print_guessed()


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    not_guess_complete = True
    while not_guess_complete:
        right_now_input = lower(raw_input("Enter a letter, or the word 'guess' to try and guess the full word: "))

        if len(right_now_input) >= 0:
            if right_now_input in letters_guessed:
                print "this letter you already guessed!"
            else:
                letters_guessed.append(right_now_input)
                if right_now_input in secret_word and word_guessed():
                    print print_guessed()," | You've done a great job!!"
                    print "And here is your hangman image :D"
                    print_hangman_image(mistakes_made)
                    not_guess_complete = False
                elif right_now_input not in secret_word:
                    mistakes_made += 1
                    print print_guessed()
                else:
                    print print_guessed()
        # else:
        #     for letter in right_now_input:
        #         if True and letter in letters_guessed:
        #             print "this letter you already guessed!"
        #         else:



    return None

play_hangman()

    
