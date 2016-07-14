# Implementation of classic arcade game Pong

import simplegui
import random

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2] 
ball_vel = [0, 0]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == LEFT:
        ball_vel[0] = -random.randrange(120,240) / 60
        ball_vel[1] = -random.randrange(60,180) / 60
    elif direction == RIGHT:
        ball_vel[0] = random.randrange(120,240) / 60
        ball_vel[1] = -random.randrange(60,180) / 60

# define event handlers
def new_game():
    global score1, score2
    score1 = 0
    score2 = 0
    spawn_ball(random.choice([LEFT,RIGHT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, 'White')
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, 'White')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, 'White')
        
    # update ball_position
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]
  
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,'Red','White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos <= (HALF_PAD_HEIGHT) and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos <= (HALF_PAD_HEIGHT) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos >= (HEIGHT - (HALF_PAD_HEIGHT)) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos >= (HEIGHT - (HALF_PAD_HEIGHT)) and paddle2_vel > 0:
        paddle2_vel = 0 
        
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel 
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT)], 2, 'White', 'Blue')
    canvas.draw_polygon([(WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT)], 2, 'White', 'Green')
    
    # determine whether ball collide with top/bottom wall or paddle and ball collide    
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    if ball_pos[0] <= ( BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT):
            score2+=1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT):
            score1+=1
            spawn_ball(LEFT)
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
                         
    # draw scores
    canvas.draw_text(str(score1), (150, 50), 40, "Red")
    canvas.draw_text(str(score2), (450, 50), 40, "Red")
                         
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -5
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
