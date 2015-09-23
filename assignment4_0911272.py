print("Witch exercise u wanna see? 1, 2 or 3?")
sChoice = input("> ")
if sChoice == 1:
   # a:
    fahr = float(raw_input("How much Fahrenheit?"))
    Celsius = round((fahr - 32) * 5.0/9.0, 2)
    print(Celsius)

    # b:
    bValidFahr = False;
    while bValidFahr == False:
        Celsius = input("How much Celsius?")
        if Celsius >= -273:
            Kelvin = round((Celsius + 273), 2)
            bValidFahr = True;
        else:
            Kelvin = "Please give a valid tempature"
    print(Kelvin)

    # c:
    number = input("how much?")
    if number < 0:
        number = number * -1;
    print(number)

elif sChoice == 2:
    # a
    sPlayer1choise      = False
    sPlayer2choise      = False
    sPlayer1Question    = "What the choise of player 1? rock, paper, scissors, lizard or spock?"
    sPlayer2Question    = "What the choise of player 2? rock, paper, scissors, lizard or spock?"
    sDrawMessage        = "No one wins"
    sPlayer1WinMessage  = "Player 1 wins"
    sPlayer2WinMessage  = "Player 2 wins"
    sMessage            = ""

    while sPlayer1choise == False or sPlayer2choise == False:
        sPlayer1choise = raw_input(sPlayer1Question).strip('\r')
        sPlayer2choise = raw_input(sPlayer2Question).strip('\r')

        if sPlayer1choise == "rock":
            if sPlayer2choise == "rock":
                sMessage = sDrawMessage
            elif sPlayer2choise == "paper":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "scissors":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "lizard":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "spock":
                sMessage = sPlayer2WinMessage

        elif sPlayer1choise == "paper":
            if sPlayer2choise == "rock":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "paper":
                sMessage = sDrawMessage
            elif sPlayer2choise == "scissors":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "lizard":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "spock":
                sMessage = sPlayer1WinMessage

        elif sPlayer1choise == "scissors":
            if sPlayer2choise == "rock":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "paper":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "scissors":
                sMessage = sDrawMessage
            elif sPlayer2choise == "lizard":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "spock":
                sMessage = sPlayer2WinMessage

        # b
        elif sPlayer1choise == "lizard":
            if sPlayer2choise == "rock":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "paper":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "scissors":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "lizard":
                sMessage = sDrawMessage
            elif sPlayer2choise == "spock":
                sMessage = sPlayer1WinMessage

        elif sPlayer1choise == "spock":
            if sPlayer2choise == "rock":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "paper":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "scissors":
                sMessage = sPlayer1WinMessage
            elif sPlayer2choise == "lizard":
                sMessage = sPlayer2WinMessage
            elif sPlayer2choise == "spock":
                sMessage = sDrawMessage

        else:
            sPlayer1choise = False
            sPlayer2choise = False
            print("please try another input!")

    print(sMessage)
elif sChoice == 3:
    print("Exercise 3!")
else:
    print("Not a valid exercise!")