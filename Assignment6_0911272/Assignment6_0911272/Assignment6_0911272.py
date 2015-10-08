import math
print("Witch figure do u wanna see?\n 1 Is the full square\n 2 Is the hollow square\n 3 Is the rectangle triangle\n 4 Is the pyramid and\n 5 Is the circle\n 6 Is the ugly smiley face.")
sChoice = input("> ")
iNumber         = input("Choose a number!")
sAsterisks      = ""

if sChoice == 1:
    for i in range (0, iNumber):
        for o in range (0, iNumber):
            sAsterisks += "*"
        sAsterisks += "\n"

    print sAsterisks
elif sChoice == 2:
    for i in range (0, iNumber):
        for o in range (0, iNumber):
            # when the for is in the square there only wil ben printed spaces so the square is hollow
            if o > 0 and o < (iNumber - 1) and i > 0 and i < (iNumber - 1):
                sAsterisks += " "
            else:
                sAsterisks += "*"
        sAsterisks += "\n"

    print sAsterisks
elif sChoice == 3:
    for i in range (0, iNumber):
        for o in range(0, (i+1)):
            sAsterisks += "*"
        sAsterisks += "\n"

    print sAsterisks
elif sChoice == 4:
    for i in range (0, iNumber):
        # the pyramid needs to grow two times so we need to double it by 2 and add one to do the first asterisks right
        iAmount = (i * 2) + 1
        # minus i is for putting the pyramid in the center else de pyramid will stay on the right side.
        for o in range(1, iNumber - i):
            sAsterisks += " "
        for k in range(0, iAmount):
            sAsterisks += "*"
        sAsterisks += "\n"

    print sAsterisks
elif sChoice == 5:
    iRadius = iNumber/2
    for i in range (iNumber):
        for o in range(iNumber):
            # = √(i − radius)2 + (o − radius)2
            # i is the point where we are in the visual field and radius, the distance from i to radius is the distance to the center of the circle.
            iDistx = i - iRadius
            iDisty = o - iRadius
            iDist = math.sqrt((iDisty**2) + (iDistx**2))
            if iDist < iRadius:
                sAsterisks += "*"
            else:
                sAsterisks += " "
        sAsterisks += "\n"
    print sAsterisks
elif sChoice == 6:
    iRadius = iNumber/2
    for i in range (iNumber):
        for o in range(iNumber):
            # = √(i − radius)2 + (o − radius)2
            # i is the point where we are in the visual field and radius, the distance from i to radius is the distance to the center of the circle.
            iDistx = i - iRadius
            iDisty = o - iRadius
            iDist = math.sqrt((iDisty**2) + (iDistx**2))
            if iDist < iRadius and iDist > (iNumber/2.6):                
                sAsterisks += "*"
            elif (i == iRadius and o == iRadius):
                sAsterisks += "#"
            elif (i == iNumber/3 and o == iNumber/3+1) or (i == iNumber/3 and o == iNumber/3*2+1):
                sAsterisks += "~"
            elif (i == iNumber/3+1 and o == iNumber/3+1) or (i == iNumber/3+1 and o == iNumber/3*2+1):
                sAsterisks += "0"
            elif (i == iNumber/4*3 and iDist < iNumber/3.5):
                sAsterisks += "-"
            else:
                sAsterisks += " "
        sAsterisks += "\n"
    print sAsterisks
else:
    print "No figure in this number!"