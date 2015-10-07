print("Witch exercise do u wanna see?\n 1 is the converter\n 2 is the rock paper scissors\n 3 must be opened by program.py")
sChoice = input("> ")
if sChoice == 1:
   # a:
    fFahr = float(raw_input("How much Fahrenheit?"))
    iCelcius = round((fFahr - 32) * 5.0/9.0, 2)
    print iCelcius

    # b:
    bValidFahr = False;
    while bValidFahr == False:
        iCelcius = input("How much Celsius?")
        if iCelcius >= -273:
            Kelvin = round((Celsius + 273), 2)
            bValidFahr = True;
        else:
            Kelvin = "Please give a valid tempature"
    print Kelvin

    # c:
    number = input("how much?")
    if number < 0:
        number = number * -1;
    print number

elif sChoice == 2:
    # a
    sPlayer1choise      = False
    sPlayer2choise      = False
    sPlayer1Question    = "What the choise of player 1? rock, paper, scissors, lizard or spock?"
    sPlayer2Question    = "What the choise of player 2? rock, paper, scissors, lizard or spock?"
    sDrawMessage        = "No one wins"
    # sPlayer1WinMessage  = "Player 1 wins"
    # sPlayer2WinMessage  = "Player 2 wins"
    rock_paper          = "Paper covers rock"
    rock_scissors       = "Rock crushes scissors"
    rock_lizard         = "Rock crushes lizard"
    rock_spock          = "Spock vaporizes rock"
    paper_scissors      = "Scissors cuts paper"
    paper_lizard        = "Lizard eats paper"
    paper_spock         = "Paper disproves spock"
    scissors_lizard     = "Scissors decapitates lizard"
    scissors_spock      = "Spock smashes scissors"
    lizard_spock        = "Lizard poisons spock"
    sMessage            = ""

    while sPlayer1choise == False or sPlayer2choise == False:
        sPlayer1choise = raw_input(sPlayer1Question).strip('\r')
        sPlayer2choise = raw_input(sPlayer2Question).strip('\r')

        if sPlayer1choise == "rock":
            if sPlayer2choise == "rock":
                sMessage = sDrawMessage
            elif sPlayer2choise == "paper":
                sMessage = rock_paper
            elif sPlayer2choise == "scissors":
                sMessage = rock_scissors
            elif sPlayer2choise == "lizard":
                sMessage = rock_lizard
            elif sPlayer2choise == "spock":
                sMessage = rock_spock

        elif sPlayer1choise == "paper":
            if sPlayer2choise == "rock":
                sMessage = rock_paper
            elif sPlayer2choise == "paper":
                sMessage = sDrawMessage
            elif sPlayer2choise == "scissors":
                sMessage = paper_scissors
            elif sPlayer2choise == "lizard":
                sMessage = paper_lizard
            elif sPlayer2choise == "spock":
                sMessage = paper_spock

        elif sPlayer1choise == "scissors":
            if sPlayer2choise == "rock":
                sMessage = rock_scissors
            elif sPlayer2choise == "paper":
                sMessage = paper_scissors
            elif sPlayer2choise == "scissors":
                sMessage = sDrawMessage
            elif sPlayer2choise == "lizard":
                sMessage = scissors_lizard
            elif sPlayer2choise == "spock":
                sMessage = scissors_spock

        # b
        elif sPlayer1choise == "lizard":
            if sPlayer2choise == "rock":
                sMessage = rock_lizard
            elif sPlayer2choise == "paper":
                sMessage = paper_lizard
            elif sPlayer2choise == "scissors":
                sMessage = scissors_lizard
            elif sPlayer2choise == "lizard":
                sMessage = sDrawMessage
            elif sPlayer2choise == "spock":
                sMessage = lizard_spock

        elif sPlayer1choise == "spock":
            if sPlayer2choise == "rock":
                sMessage = rock_spock
            elif sPlayer2choise == "paper":
                sMessage = paper_spock
            elif sPlayer2choise == "scissors":
                sMessage = scissors_spock
            elif sPlayer2choise == "lizard":
                sMessage = lizard_spock
            elif sPlayer2choise == "spock":
                sMessage = sDrawMessage

        else:
            sPlayer1choise = False
            sPlayer2choise = False
            print("please try another input!")

    print(sMessage)
elif sChoice == 3:
    print("Exercise 3 could be found in folder exercise 3.")
else:
    print("Not a valid exercise!")