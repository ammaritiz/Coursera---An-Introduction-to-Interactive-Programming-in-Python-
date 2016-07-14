'''
Program would think of a random number in a range [0,100)
or [0,1000).You need to guess that number in a limited
number of guesses. Input will come from buttons and an 
input field.All output for the game will be printed 
in the console
'''
import simplegui
import random
import math

secret_number = 0
guess_limit = 0
range = 100

def new_game(range):
    '''
        Helper function to start and restart the game
    '''
    global secret_number, guess_limit
    secret_number = random.randrange(0,range)
    guess_limit = int(math.ceil(math.log(range, 2)))
    print "New game started with range 0 to", range
    display_remaining_guesses()

def display_remaining_guesses():
    '''
        Displays remaining guesses
    '''
    print "Remaining guesses is", guess_limit
    print ""
    if guess_limit == 0:
        print "Correct guess was", secret_number
        print "You lose\n"
        new_game(range)   
        
# define event handlers for control panel
def range100():
    '''
        Button that changes the range to [0,100) and starts a new game 
    '''
    global range
    range = 100
    new_game(range)

def range1000():
    '''
        Button that changes the range to [0,1000) and starts a new game     
    '''
    global range
    range = 1000
    new_game(range)    
    
def input_guess(guess):
    '''
        Main game logic goes here	
    '''
    guess = int(guess)
    global guess_limit
    print "Guess was",guess
    global secret_number
    if guess == secret_number:
        print "Correct"
        print "You win\n"
        new_game(range)
        return 0
    elif guess > secret_number:
        print "Lower"
    else:
        print "Higher"
    guess_limit -= 1
    display_remaining_guesses()
    
# create frame
frame = simplegui.create_frame('Guess the number?', 200, 200)

# Register event handlers
inp = frame.add_input('Guess: ',input_guess,100)
button1 = frame.add_button('Range is [0,100)', range100)
button2 = frame.add_button('Range is [0,1000)',range1000)
frame.start()

# call new_game 
new_game(range)

