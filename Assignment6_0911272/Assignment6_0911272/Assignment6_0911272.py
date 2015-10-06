import math
print("Witch figure do u wanna see?\n 1 Is the full square,\n 2 Is the hollow square,\n 3 Is the rectangle triangle,\n 4 Is the pyramid and\n 5 Is the circle ")
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
    for i in range (0, iNumber+2):
        for o in range (0, iNumber):
            iYdist = abs(i - iRadius)
            iXdist = abs(o - iRadius)
            if int(math.ceil(math.sqrt(iYdist**2 + iXdist**2))) < iRadius:
                sAsterisks += "*"
            else:
                sAsterisks += " "
        sAsterisks += "\n"

    print sAsterisks
else:
    print "No figure in this number!"