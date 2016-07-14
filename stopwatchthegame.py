'''
    Stopwatch : The Game"
'''

import simplegui

# Global states
time = 0
successful_stops = 0
total_stops = 0
stopwatch_is_running = False

def attempts():
    return str(successful_stops) + "/" + str(total_stops)

def format(t):
    '''
        Function that returns time in tenths of seconds 
        as a formatted string A:BC.D
    '''
    min = t/600
    sec = (t % 600) / 10
    tenthsec = t - ((t/10)*10)
    return converted_string(min,sec,tenthsec)

def converted_string(m,s,t):
    if s < 10:
        s = "0" + str(s)
    return str(m) + ":" + str(s) + "." + str(t)
    
def start():
    '''
        Event Handler for start button
    '''        
    global stopwatch_is_running
    timer.start()
    stopwatch_is_running = True
    
def stop():
    '''
        Event Handler for stop button
    ''' 
    global successful_stops, total_stops,stopwatch_is_running
    if stopwatch_is_running:
        if time%10 == 0:
            successful_stops +=1
        total_stops +=1 
    timer.stop()
    stopwatch_is_running = False

def reset():
    '''
        Event Handler for reset button
    ''' 
    global time,successful_stops,total_stops
    timer.stop()
    time = 0
    successful_stops = 0
    total_stops = 0

def timer_handle():
    '''
        Event Handler for timer
    ''' 
    global time
    time += 1
    
def draw_time(canvas):
    '''
        Draw Handler
    ''' 
    global time
    if time == 5999:
        timer.stop()
    canvas.draw_text(format(time),[90,160],50,"white")
    canvas.draw_text(attempts(),[210,50],40,"red")
    
# create frame
frame = simplegui.create_frame('Stopwatch',300,300)

# register event handlers
timer = simplegui.create_timer(100,timer_handle)
frame.set_draw_handler(draw_time)
startbutton = frame.add_button('Start', start,100)
stopbutton = frame.add_button('Stop', stop,100)
resetbutton = frame.add_button('Reset',reset,100)

# start frame
frame.start()