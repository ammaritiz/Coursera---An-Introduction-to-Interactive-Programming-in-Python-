# implementation of card game - Memory

import simplegui
import random

canvas_width = 800
canvas_height = 100
card_width = canvas_width / 16.0
numbers = tmp = range(8)
numbers.extend(tmp)
exposed = []

# helper function to initialize globals
def new_game():
    global state, exposed, turns
    random.shuffle(numbers)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    exposed = [False for i in numbers]
    
# define event handlers
def mouseclick(pos):
    global state, first_card, second_card, turns
    i = pos[0] // card_width
    if exposed[i]:
        pass
    else:
        if state == 0:
            first_card = i
            state = 1
        elif state == 1:
            second_card = i
            turns += 1
            label.set_text("Turns = " + str(turns))
            state = 2
        else:
            if not numbers[first_card] == numbers[second_card]:
                exposed[first_card], exposed[second_card] = False, False
            state = 1
            first_card = i
        exposed[i] = True
    
def draw(canvas):
    index = 0
    for n in numbers:
        offset = index * card_width
        if exposed[index]:
            canvas.draw_text(str(n), [offset + (card_width / 4), 2.0 * canvas_height / 3], 50, "White")
        else:
            canvas.draw_polygon([(offset, 0), (offset + card_width, 0), (offset + card_width, canvas_height),(offset, canvas_height),], 1, 'Black', 'Green')
        index += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", canvas_width, canvas_height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
