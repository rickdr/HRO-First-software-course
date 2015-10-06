print("Witch figure do u wanna see? 1 to 6?")
sChoice = input("> ")
iNumber         = input("Choose a number!")
sAsterisks      = ""

if sChoice == 1:
    for i in range (iNumber):
        for o in range (iNumber):
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
    print "5"
else:
    print "No figure in this number!"