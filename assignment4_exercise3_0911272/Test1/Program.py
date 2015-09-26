from Start import *

help = "Press w to move forward, press d to turn right, press a to turn left, press s to go back and press c te clear your drawing."
moveSpeed = 5
turnDegrees = 30

print help
print "Need help? press h"

def Program():
    key = get()
    if key == 119: #W pressed
        forward(moveSpeed)
    if key == 97: #A pressed
        turn(turnDegrees)
    if key == 100: #D pressed
        turn(-turnDegrees)
    if key == 115: #S pressed
        turn(180)
        forward(moveSpeed)
    if key == 99: #C pressed
        clear();
    if key == 104: #H pressed
        print help

run(Program)
from End import *
