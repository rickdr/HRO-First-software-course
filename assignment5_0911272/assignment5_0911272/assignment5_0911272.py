print "Which exercise do u wanna see? 1, 2 or 3?"

iValue = input(">")
if iValue == 1:
    sValue = raw_input("What do u wanna reverse?")
    begin = None
    einde = None
    reverse_string = slice(begin, einde, -1)
    print sValue[reverse_string]
elif iValue == 2:
    import re
    print "exersice 2"
    sValue = raw_input("Choose a password!")
    if re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[&'(\-_)=~#{[|`\\^@\]}^$*¨£µ%,;:!?./§+]).{6,50}", sValue):
        sMessage = "Password is strong!"         
    elif re.match('(?=.*[a-z])(?=.*[0-9]).{6,50}', sValue):
        sMessage = "Password is medium"
    else:
        sMessage = "Password is weak!"

    print sMessage
elif iValue == 3:
    sCharacters     = raw_input("What letters do u want?")
    iCount          = input("How much steps do u wanna jump in the alpabet?")
    iBegin          = 65
    iEnd            = 90
    iAmountAlpa     = 26
    sAllcharacters  = ""

    for sChar in sCharacters:
        if not sChar.isalpha():
            sAllcharacters += sChar
        else:
            if sChar.islower():
                iBegin = 97
                iEnd   = 122
            if ord(sChar) + iCount in range((iBegin - 1), (iEnd + 1)):
                # When we don't need to go arround we just give the new value
                sAllcharacters += chr(ord(sChar) + iCount)
            else:
                # First ord gives te ascii code of de character than min the begin plus the amount of alpabet and the counter 
                sAllcharacters += chr(((ord(sChar) - iBegin + iAmountAlpa + iCount) % iAmountAlpa) + iBegin)
 
    print sAllcharacters
    # print "exersice 3"
else:
    print "This is not a valid exercise"