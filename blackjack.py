# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
prompt = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card:", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = list()	# create Hand object

    def __str__(self):
        cards = ""
        for card in self.hand:
            cards += " " + card.suit + card.rank
        return "Hand Contains" + cards	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        value = 0
        for card in self.hand:
            value += VALUES[card.rank]
        for card in self.hand:
            if card.rank == 'A' and (value + 10) <= 21:
                value += 10
        return value

    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 100 # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = list()# create a Deck object
        [self.deck.append(Card(suit,rank)) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck) 

    def deal_card(self):
        return self.deck.pop(random.randrange(0, len(self.deck)))# deal a card object from the deck

    def __str__(self):
        cards = ""
        for card in self.deck:
            cards += " " + card.suit + card.rank
        return "Deck Contains" + cards	# return a string representing of the deck

#define event handlers for buttons
def deal():
    global prompt, in_play, deck, player, dealer, outcome, score
    outcome = ""
    if in_play:
        in_play = False
        score -= 1
        outcome = "You Lost"
    prompt = ""
    in_play = True
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    prompt = "Hit or Stand?"

def hit():
    global player, dealer, outcome, score, in_play, prompt
    if player.get_value() <= 21 and in_play:
        player.add_card(deck.deal_card())

    if player.get_value() > 21:
        outcome = "You Busted."
        prompt = "New Deal?"
        if in_play:
            score -= 1
        else:
            outcome = "You already Busted."
        in_play = False

def stand():
    global dealer, player, outcome, prompt, in_play, score
    prompt = "New Deal?"
    if player.get_value() > 21:
        outcome = "You already Busted." # replace with your code below
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "Dealer Busted."
            if in_play:
                score += 1
        elif dealer.get_value() >= player.get_value():
            outcome = "Dealer Won."
            if in_play:
                score -= 1
        else:
            outcome = "You Won."
            if in_play:
                score += 1
        in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack",[125,75],30,"Aqua")
    canvas.draw_text("Player",[100,300],25,"Black")
    canvas.draw_text("Dealer",[100, 125], 25, "Black")
    canvas.draw_text(prompt,[250,300],25,"Black")
    canvas.draw_text(outcome,[250,125],25,"Black")
    player.draw(canvas, [100,325])
    dealer.draw(canvas, [100,150])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    canvas.draw_text("Score : " + str(score), [300,75],25, "Black")
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 500)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()