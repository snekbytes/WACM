# This is a simple game to test reaction times. A dot will move across the screen
# and the player must press the 'a' button when it is in the centre. If they get
# it right, the dot moves faster. If they get it wrong, the game ends and their
# score is displayed before starting again. 

from microbit import *

#initialize
while True:
    x = 0
    score=0
    sleeptime=200

    #start the game loop
    while True:
        #show the middle line
        display.show(Image("00900:00900:00000:00900:00900"))
        #show the moving dot
        display.set_pixel((x), 2, 9)
        sleep(int(sleeptime))

        #if they press at the right time, add to score, decrement the time
        if x==2 and button_a.is_pressed():
            score=score+1
            sleeptime=int(sleeptime)-20

        #else lose
        elif button_a.is_pressed():
            break
        #move the dot 1 pixel to the right; if at the right of the display, go back to left side
        x = x+1
        if x>4:
            x=0
    display.scroll(str(score))
