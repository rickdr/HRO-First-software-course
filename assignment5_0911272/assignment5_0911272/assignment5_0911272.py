print "Which exercise do u wanna see? 1, 2 or 3?"
iValue = input(">")
if iValue == 1:
    sValue = raw_input("What do u wanna reverse?")
    sEnd = ""

    for sChar in sValue:
        sEnd = sChar + sEnd

    print sEnd

elif iValue == 2:
    sValue = raw_input("Choose a password!")
    sSpecialChars = "~`!@#$%€^&*()_+=-{}[]|\:;'<>?"
    iCountDigit = 0
    iCountUpper = 0
    iCountSpecial = 0

    iCountChar = len(sValue)

    if iCountChar < 6:
        sMessage = "password is to short!"
    else:
        for sChar in sValue:
            if sChar.isdigit():
                iCountDigit = iCountDigit + 1
            elif sChar.isupper():
                iCountUpper = iCountUpper + 1
            elif sChar in sSpecialChars:
                iCountSpecial = iCountSpecial + 1

        if iCountDigit >= 2 and iCountUpper >= 2 and iCountSpecial >= 1:
            sMessage = "Password is strong!"         
        elif iCountDigit >= 1  and (iCountUpper >= 1 or iCountSpecial >= 1):
            sMessage = "Password is medium"
        else:
            sMessage = "Password is weak!"

    print sMessage
elif iValue == 3:
    sCharacters     = raw_input("What letters do u want?")
    iCount          = input("How much steps do u wanna jump in the alpabet?")
    iBegin          = 65
    iEnd            = 90
    iAmountAlpabeth = 26
    sAllcharacters  = ""

    for sChar in sCharacters:
        if not sChar.isalpha():
            sAllcharacters += sChar
        else:
            iNew = ord(sChar) + iCount
            if sChar.islower():
                iBegin = 97
                iEnd   = 122
            if iNew > iEnd:
                iNew -= iAmountAlpabeth
            elif iNew < iBegin:
                iNew += iAmountAlpabeth
            sAllcharacters += chr(iNew)
    print sAllcharacters
else:
    print "This is not a valid exercise"