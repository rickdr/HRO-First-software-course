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
    iSpaces = iNumber - 1
    for i in range (0, iNumber):
        for o in range (0, iSpaces):
            sAsterisks += " "
        for k in range(0, iNumber - iSpaces):
            sAsterisks += " *"
        iSpaces -= 1   
        sAsterisks += "\n"

    print sAsterisks
elif sChoice == 5:
    iRadius = iNumber/2
    for i in range (iNumber):
        for o in range(iNumber):
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