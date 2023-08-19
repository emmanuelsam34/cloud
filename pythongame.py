while (1<2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")

    userChoice = input("Choose your weapon [R]ock], [P]aper, [S]cissors, [E]xit: ")

    if (not re.match("[SsRrPpEe]", userChoice)) or (len(userChoice) != 1):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors, [P]aper or [E]xit")
        continue

    print ("You choose: " +userChoice)

    if (userChoice == 'E' or  userChoice == 'e' ):
        print('Exiting Game..')
        break

    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)

    print ("I choose: " + opponentChoice)

    if opponentChoice == str.upper(userChoice):
        print ("Tie! ")


    elif opponentChoice == 'R' and userChoice.upper() == 'S':
        print ("Scissors beats rock, I win! ")
        continue

    elif opponentChoice == 'S' and userChoice.upper() == 'P':
        print ("Scissors beats paper! I win! ")
        continue

    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beat rock, I win! ")
        continue

    else:
        print ("You win!")
        
    
