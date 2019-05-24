# Authors: Alden DeMello and Sebastian Deluca
# Date: 5/22/2019
#FileName: DeMello_Deluca_CA.py
#Description: A computerized version of UNO where the user verses a computer and attempts to
#   get to 0 cards. A card can be played when the colour or number matches that of the card
#   in the middle.

import random # Access the random library
import webbrowser #Access the web browser library

def wS(times):# Whitespace function
    for amount in range(times): # Loop that repeats as often as told to
        print('') # Whitespace

def userWinText(): # Function that displays the user winning
    winNum = 'user' # Tell the program the user won
    wS(5) 
    print('YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU')
    print('Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U')
    print('Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U')
    print('Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU')
    print('YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U')
    print('  Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U ')
    print('   Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U') 
    print('    Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U ')
    print('     Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U ')
    print('      Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U ')
    print('      Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U ')
    print('      Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U ')
    print('      Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U ')
    print('   YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU  ')
    print('   Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU ')
    print('   YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU')      
    wS(5)                                                                                                                
    print('WWWWWWWW                           WWWWWWWWIIIIIIIIIINNNNNNNN        NNNNNNNN')
    print('W::::::W                           W::::::WI::::::::IN:::::::N       N::::::N')
    print('W::::::W                           W::::::WI::::::::IN::::::::N      N::::::N')
    print('W::::::W                           W::::::WII::::::IIN:::::::::N     N::::::N')
    print(' W:::::W           WWWWW           W:::::W   I::::I  N::::::::::N    N::::::N')
    print('  W:::::W         W:::::W         W:::::W    I::::I  N:::::::::::N   N::::::N')
    print('   W:::::W       W:::::::W       W:::::W     I::::I  N:::::::N::::N  N::::::N')
    print('    W:::::W     W:::::::::W     W:::::W      I::::I  N::::::N N::::N N::::::N')
    print('     W:::::W   W:::::W:::::W   W:::::W       I::::I  N::::::N  N::::N:::::::N')
    print('      W:::::W W:::::W W:::::W W:::::W        I::::I  N::::::N   N:::::::::::N')
    print('       W:::::W:::::W   W:::::W:::::W         I::::I  N::::::N    N::::::::::N')
    print('        W:::::::::W     W:::::::::W          I::::I  N::::::N     N:::::::::N')
    print('         W:::::::W       W:::::::W         II::::::IIN::::::N      N::::::::N')
    print('          W:::::W         W:::::W          I::::::::IN::::::N       N:::::::N')
    print('           W:::W           W:::W           I::::::::IN::::::N        N::::::N')
    print('            WWW             WWW            IIIIIIIIIINNNNNNNN         NNNNNNN')
    wS(5)
    return winNum # Return this to the program


def userLoseText(): # Function that displays the computer winning
    winNum = 'cpu' # Tell the program the user lost
    print('YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU')
    print('Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U')
    print('Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U')
    print('Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU')
    print('YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U')
    print('  Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U ')
    print('   Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U') 
    print('    Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U ')
    print('     Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U ')
    print('      Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U ')
    print('      Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U ')
    print('      Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U ')
    print('      Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U ')
    print('   YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU  ')
    print('   Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU ')
    print('   YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU') 

    wS(5) # Whitespace
    

    print('LLLLLLLLLLL                  OOOOOOOOO        SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT')
    print('L:::::::::L                OO:::::::::OO    SS:::::::::::::::ST:::::::::::::::::::::T')
    print('L:::::::::L              OO:::::::::::::OO S:::::SSSSSS::::::ST:::::::::::::::::::::T')
    print('LL:::::::LL             O:::::::OOO:::::::OS:::::S     SSSSSSST:::::TT:::::::TT:::::T')
    print('  L:::::L               O::::::O   O::::::OS:::::S            TTTTTT  T:::::T  TTTTTT')
    print('  L:::::L               O:::::O     O:::::OS:::::S                    T:::::T        ')
    print('  L:::::L               O:::::O     O:::::O S::::SSSS                 T:::::T        ')
    print('  L:::::L               O:::::O     O:::::O  SS::::::SSSSS            T:::::T        ')
    print('  L:::::L               O:::::O     O:::::O    SSS::::::::SS          T:::::T        ')
    print('  L:::::L               O:::::O     O:::::O       SSSSSS::::S         T:::::T        ')
    print('  L:::::L               O:::::O     O:::::O            S:::::S        T:::::T        ')
    print('  L:::::L         LLLLLLO::::::O   O::::::O            S:::::S        T:::::T        ')
    print('LL:::::::LLLLLLLLL:::::LO:::::::OOO:::::::OSSSSSSS     S:::::S      TT:::::::TT      ')
    print('L::::::::::::::::::::::L OO:::::::::::::OO S::::::SSSSSS:::::S      T:::::::::T      ')
    print('L::::::::::::::::::::::L   OO:::::::::OO   S:::::::::::::::SS       T:::::::::T      ')
    print('LLLLLLLLLLLLLLLLLLLLLLLL     OOOOOOOOO      SSSSSSSSSSSSSSS         TTTTTTTTTTT      ')

    wS(5)
    return winNum # Return the winner to the program
def unoText(): # Function that displays the title of the game
    input('Please maximize your IDLE before continuing...[Press enter to continue]') # Make the title look complete
    wS(100) # Whitespace

    print('UUUUUUUU    UUUUUUUU     NNNNNNNN        NNNNNNNN          OOOOOOOOO')     
    print('U::::::U    U::::::U     N:::::::N       N::::::N        OO:::::::::OO')   
    print('U::::::U    U::::::U     N::::::::N      N::::::N      OO:::::::::::::OO') 
    print('UU:::::U    U:::::UU     N:::::::::N     N::::::N     O:::::::OOO:::::::O')
    print('U:::::U     U:::::U      N::::::::::N    N::::::N     O::::::O   O::::::O')
    print('U:::::D     D:::::U      N:::::::::::N   N::::::N     O:::::O     O:::::O')
    print('U:::::D     D:::::U      N:::::::N::::N  N::::::N     O:::::O     O:::::O')
    print('U:::::D     D:::::U      N::::::N N::::N N::::::N     O:::::O     O:::::O')
    print('U:::::D     D:::::U      N::::::N  N::::N:::::::N     O:::::O     O:::::O')
    print('U:::::D     D:::::U      N::::::N   N:::::::::::N     O:::::O     O:::::O')
    print('U:::::D     D:::::U      N::::::N    N::::::::::N     O:::::O     O:::::O')
    print('U::::::U   U::::::U      N::::::N     N:::::::::N     O::::::O   O::::::O')
    print('U:::::::UUU:::::::U      N::::::N      N::::::::N     O:::::::OOO:::::::O')
    print(' UU:::::::::::::UU       N::::::N       N:::::::N      OO:::::::::::::OO')
    print('   UU:::::::::UU        N::::::N        N::::::N        OO:::::::::OO')   
    print('    UUUUUUUUU           NNNNNNNN         NNNNNNN          OOOOOOOOO')        
    wS(2)

def welcomeScreen(winCount, loseCount): # A function that welcomes the user
    unoText() #Remove later
    choiceFlag = True # Activate a flag for the menu
    menuHeader1 = '┍-----------------------------┒\n'
    menuHeader2 = '|       WELCOME TO UNO!       |\n'
    menuHeader3 = '┕-----------------------------┙\n'
    menuPt1 = '┍-----------------------------┒\n'
    menuPt2 = '|         |         |         |\n'
    menuPt3 = '| H: Help | P: Play | Q: Quit |\n'
    menuPt4 = '|         |         |         |\n'
    menuPt5 = '┕-----------------------------┙\n'
    menuPt9 = '┍-----------------------------┒\n'
    menuPt6 = '| Opponent Wins: ' + str(loseCount) +'            |\n'
    menuPt7 = '| User Wins: ' + str(winCount) + '                |\n'
    menuPt8 = '┕-----------------------------┙\n'
    
    print(menuHeader1 + menuHeader2 + menuHeader3 + menuPt1 + menuPt2 + menuPt3 + menuPt4 + menuPt5 + menuPt9 + menuPt6 + menuPt7 + menuPt8) #Display the menu
    wS(1) # Whitespace
    while choiceFlag == True: #While the flag is true
        userChoice = input('Enter one of the choices below! \n>>')#Get the user's input
        userChoice = userChoice.lower() #Lowercase the user's input
        if userChoice == 'p': #If condition types p
            choiceFlag = False #Disable flag forthe choice
            winner = unoGame() #Call the uno game function
            return winner # Return this to the program
        elif userChoice == 'h':#If condition types h
            choiceFlag = False #Disable flag forthe choice
            helpMenu() #Call the help menu function
        elif userChoice == 'q':#If condition types q
            choiceFlag = False #Disable flag forthe choice
            choice = quitMenu() #Call the quit menu function
            return choice #Return the choice to the program
        else: #Else 
            print('Please enter a choice from the ones listed above!') #Inform the user what to do
        
def compPlay(topCard, compDeck, gameDeck): #Computer's play function

    possibleChoices = [] #Empty list of possible choices the computer can play

    possLen = len(possibleChoices) #Create a variable for the length of the array possible choices

    colorChoices = ['Rz', 'Gz', 'Bz', 'Yz'] # Create a list of possible choices
    
    print('Your Opponent\'s turn!') #Tell the user that the computer is playing
    try:  # Try to get the length of the deck
        compDeckLen = len(compDeck) #Get the length of the computer's deck
    except TypeError:  # If there is a type error
        compDeckLen = 0 # Make deckLen 0

    ################### FOR TESTING ####################


    playableCards = detPlayables(topCard, compDeck) # Determine what cards the computer can play

    if type(playableCards) == None: # If there is no playbale cards
        compCardPick = True # Activate a flag
    else: 
        for cards in playableCards: # Loop that runs over all playable cards

            possibleChoices.append(cards) # Append playable cards to the list
        
        #computer needs to draw card when none are playable
        try: # Try to let the user pick a card they can play
            compCardPick = random.choice(possibleChoices)
        except IndexError: # If there is an index error
            try: # Try to get a new card
                compCardPick = getNewCard(gameDeck) # Get a new card
            except IndexError: # If there is an index error
                gameDeck = genDeck # Recreate the gamedeck

        wS(1) # Whitespace
        print('Your opponent played a card!') # Tell the user the opponent played
        return compCardPick # Return the card the computer picked to the program

def userPlay(topCard, userDeck): # Function for the user's playing
    wS(1) # Whitespace
    
    print('You have ' + str(len(userDeck)) + ' card(s)! \n \nThese are your card(s):') # Tell the user what their cards are
    try:
        deckLen = len(userDeck) # get the length of the user deck
    except TypeError: # If there is a type error
        deckLen = 0 # Set deckLen to 0
    
    for cards in userDeck: # Display the cards
    
        print('\n ┍--------┑ \n |' + cards + '      | \n |        | \n |        | \n |      ' + cards + '| \n ┕--------┙' , end=' ') #Print the users cards
    wS(1) # Whitespace
    input('OKAY!') # Allow user to continue on their own time
    
    wS(50) # Clear screen
    
    playableCards = detPlayables(topCard, userDeck) # Determine the cards in their deck that can be played
    
    wS(1) # Whitespace
    if playableCards == []: # If there is no playable cards
        cardPick = True # Set a boolean
        return cardPick # Return this to the program
    else:
        print('These are the cards you can play:') # Tell the user what card they can play
        
        counter = 0 # Set a running total
        
        for cards in playableCards: # Display the cards
        
            counter += 1 # Add 1
        
            print(str(counter) + '\n ┍--------┑ \n |' + cards + '      | \n |        | \n |        | \n |      ' + cards + '| \n ┕--------┙' , end=' ') # Print the user's playable cards
                
            wS(1) # Whitespace
        

        inputFlag = True # Activate an input flag
        while inputFlag == True: # When the flag is active
            try: # Get the user card
                wS(1) # Whitespace
            
                print('Which card would you like to play? (1-' + str(counter) + ')') # Prompt the user for input
                
                userCard = int(input('#: ')) # Get the user input for which card to play
                userCard = int(userCard) - 1 # Cast user input into an integer
                cardPick = playableCards[userCard]
                inputFlag = False # Stop the input flag
            except ValueError: # If there is a value error
                print('You did not pick a valid card. Please try again.') # Tell the user to retry
            
            except IndexError: # If there is a value error
                print('You did not pick a valid card. Please try again.') # Tell the user to retry       
    return cardPick # Return the card that was picked back to the program
def detPlayables(topCard, playerDeck): # Function that determines what cards can be played
    
    playableCards = [] # Set a base list
    
    deckNum = topCard[1] # Slice the number out of the card
    
    deckClr = topCard[0] # Slice the colour out of the card
    
    for playables in playerDeck: # Loop that runs over the playable cards
        cardNum = playables[1] #Slice the number out of the card

        cardClr = playables[0] # Slice the colour out of the card
        if cardClr == deckClr and deckNum == 'z': # If the card ends with a z
            playableCards.append(playables) # Add this card to the playable list
        elif deckNum == 'x' or deckNum == '+': # If the card is a plus 4 or colour change
            playableCards = playerDeck.copy() # All cards are playable
        
        elif cardNum == deckNum or cardNum == 'x' or cardNum == '+': # If the numbers are the same
    
            playableCards.append(playables) # Add this card to the list
    
        elif cardClr == deckClr or cardClr == 'C' or cardClr == 'P': # If the colours are the same
    
            playableCards.append(playables) # Add this card to the list
    return playableCards # Return this  list to the program

def getNewCard(deck): # A function that retrieves one singlular card from the deck
    newCard = deck[0] # Take a card from within the deck
    return newCard # Return this card to the program

def unoGame(): # Where the main game is played

    blockFlag = False # Generate a boolean
    
    gameDeck = genDeck() # Generate the card deck for the game
    
    userDeck = distUserCards(gameDeck) # Distribute 7 cards to the user
    
    compDeck = distCompCards(gameDeck) # Distribute 7 cards to the computer
    
    gameDeck = removeDistCards(gameDeck) # Remove the given cards from the deck
    topCard = getNewCard(gameDeck) # Get a card to begin the game with
    
    gameDeck.remove(topCard) # Remove this card from the deck
    wS(1) # Whitespace
    
    gameFlag = True # Activate the gameflag

    rvCounter = 0 # Running total
    
    while gameFlag == True: # When the game is running
        userFlag = True # Activate flag
        compFlag = True # Activate flag
        while userFlag == True and blockFlag == False: # While this is true
            cpuLength = len(compDeck) # Get the length of the computer's deck
            if cpuLength > 1: # If the computer has more than 1 card
                print('Your opponent has ' + str(cpuLength) + ' cards remaining.') # Tell the computer how many cards the computer has
            else: # If the computer has 1 card
                print('Your opponent has ' + str(cpuLength) + ' card remaining.') # Tell the computer how many cards the computer has
            wS(1) # Whitespace
            print('The card in the middle is... ') # Tell the user what card is in the middle
            
            print('\n ┍--------┑ \n |' + topCard + '      | \n |        | \n |        | \n |      ' + topCard + '| \n ┕--------┙' , end=' ') # Print the card that is in the middle
            wS(1) # Whitespace
            print('You go!') # Tell the user that they are going first
            
            input('OKAY!') # Allow user to continue on their own time

#####STACKING IN USERPLAY
            wS(1) # Whitespace
            oldTop = topCard # Save the previous top card
            topCard = userPlay(topCard, userDeck)
            if topCard == True: # If the user didn't have a card
                newCards = getNewCard(gameDeck) # Get the user a new card
                wS(1) # Whitespace
                print('You couldn\'t play, so you picked up a...') # Tell the user
                wS(1) # Whitespace
                print('\n ┍--------┑ \n |' + newCards + '      | \n |        | \n |        | \n |      ' + newCards + '| \n ┕--------┙' , end=' ') # Override print function
                gameDeck.remove(newCards) # Remove the new cards from the game deck
                userDeck.append(newCards) # Add these new cards to the user's cards
                topCard = oldTop # Reset the top card
                wS(1) # Whitespace
                input('OKAY!') # Allow user to continue on their own time
                rvCounter += 1 # Add to total
            else: # If the user did have a card
                userDeck.remove(topCard) # Remove the played card
                rvCounter = 0 # Reset running total
            stackDeck = userDeck.copy() # Copy the userDeck
            counter = 0 # Set a running total
            if len(userDeck) <=1: # If the computer has less than one card
                stackingFlag = False # The flag is not enabled
            else: # If the deck has more than 1 card
                stackingFlag = True # Flag for stacking
            while stackingFlag == True: # When the stack is possible
                for stackCheck in stackDeck: # Checking for stackable cards in the user deck
                    
                    if topCard[1] == stackCheck[1]: # If the numbers on the cards are the same
                        
                        print('You can also play...') # Tell the user there's other options
                        counter += 1 # Add 1
                        print(str(counter) + '\n ┍--------┑ \n |' + stackCheck + '      | \n |        | \n |        | \n |      ' + stackCheck + '| \n ┕--------┙' , end=' ')  # Override print function
                        
                        wS(1) # Whitespace
                        print('Would you like to play your ' + stackCheck + ' card as well? (Y/N)') # Prompt user for stacking
                        stackFlag=  True
                        while stackFlag == True: # When the user is determining whether or not to stack
                            doesStack = input('Y/N: ') # Get user input for if they want to stack their cards
                            doesStack = doesStack.upper() # Uppercase the input

                            if doesStack == 'N': # If the user doesn't want to stack
                                wS(1) # Whitespace
                                print('You did not play your ' + stackCheck + ' card.') # Tell the user they did not take their card
                                wS(1) # Whitespace
                                stackFlag = False# Stop the flag
                            elif doesStack == 'Y': # If the user wants to stack
                                
                                topCard = stackCheck # Set the new card as the card the user is going to play
                                stackFlag = False # stop the flag
                                userDeck.remove(topCard) # Remove the previous card as it will be played anyway
                            else: # If the user doesn't say Y/N
                                wS(1) # Whitespace
                                print('Please enter either \'Y\' or \'N\'.') # Tell the user what went wrong 
                        stackingFlag = False # Stop the flag
                    stackingFlag = False #Stop the flag
            ####################################################################################
            
            if topCard[1] == 'b': # If the user played a block
                print('You blocked your opponent!') # Tell the user they blocked the opponent
                compFlag = False # Stop the computer from playing one round
                
            elif topCard[1] == 'r' and rvCounter == 0: # If the user played a reverse card
                print('The game reverses back to you!') # Tell the user that the game is reversing back to them
                rvCounter +=1 # Add to the running total
                compFlag = False # Stop the computer from playing
            
            elif topCard[1] == '+': # If the user plays a Plus Four
                print('Your opponent must pick up 4 cards')
                for cards in range(4): # A loop that runs 4 times
                    card = getNewCard(gameDeck) # Generate 4 new cards for the user
                    gameDeck.remove(card) # Remove the new card from the deck
                    compDeck.append(card) # Add these cards to the computer deck
                choices = ['Rz', 'Gz', 'Bz', 'Yz'] # List of choices
                print('You get to change the colour of the game! Pick a colour!') # Tell the user to change the colour of the game
                counter = 0 # Running total
                for cards in choices: # Display the cards
                    counter += 1 # Add 1 
                    print(str(counter) +' ┍--------┑ \n  |' + cards + '      | \n  |        | \n  |        | \n  |      ' + cards + '| \n  ┕--------┙' , end=' ') # Show the choices to the user
                    wS(1) # Whitespace
                inputFlag = True # Activate a flag
                while inputFlag == True:
                    try: # Get the user card
                        wS(1) # Whitespace
                    
                        print('Which card would you like to play? (1-' + str(counter) + ')') # Prompt the user for input
                        
                        userCard = int(input('#: ')) # Get the user input for which card to play
                        userCard = int(userCard) - 1 # Cast user input into an integer
                        cardPick = choices[userCard]
                        topCard = cardPick ################
                        inputFlag = False # Stop the input flag
                    except ValueError: # If there is a value error
                        print('You did not pick a valid card. Please try again.') # Tell the user to retry
                    
                    except IndexError: # If there is a value error
                        print('You did not pick a valid card. Please try again.') # Tell the user to 
            elif topCard[1] == 'p': # If the player plays a Plus 2
                print('Your opponent must pick up 2 cards')
                for cards in range(2): # A loop that runs 4 times
                    card = getNewCard(gameDeck) # Generate 4 new cards for the user
                gameDeck.remove(card) # Remove the new card from the deck
                compDeck.append(card) # Add these cards to the computer deck
            elif topCard[1] == 'x': # If the top card is a colour Change
                choices = ['Rz', 'Gz', 'Bz', 'Yz'] # List of choices
                print('You get to change the colour of the game! Pick a colour!') # Tell the user to change game colour
                counter = 0 # Running total
                for cards in choices: # Display the cards
            
                    counter += 1 # Add 1
                    print(str(counter))
                    print(' \n ┍--------┑ \n |' + cards + '      | \n |        | \n |        | \n |      ' + cards + '| \n ┕--------┙ ')# Print the colour change cards
                inputFlag = True # Activate an input flag
                while inputFlag == True: # When the flag is running
                    try: # Get the user card
                        wS(1) # Whitespace
                    
                        print('Which card would you like to play? (1-' + str(counter) + ')') # Prompt the user for input
                        
                        userCard = int(input('#: ')) # Get the user input for which card to play
                        userCard = int(userCard) - 1 # Cast user input into an integer
                        cardPick = choices[userCard] # Slice the user's choice from the card choices
                        topCard = cardPick ################
                        inputFlag = False # Stop the input flag
                    except ValueError: # If there is a value error
                        print('You did not pick a valid card. Please try again.') # Tell the user to retry
                    
                    except IndexError: # If there is a value error
                        print('You did not pick a valid card. Please try again.') # Tell the user to retry
            wS(1) # Whitespace
            
            userFlag = False  # Stop the flag
        if len(userDeck) == 1: # If the player has 1 card left
            print('You have one card remaining! Call UNO!') # Tell the user to call Uno!
            input('\'UNO!\' ') # Get the user to call uno

        #USER UNO CHECKo
        if len(userDeck) == 0: # If the player runs out of cards
            gameFlag = False # Stop the game.
            print('You: UNO Out!') # Print the final statement
            wS(1) # Whitespace
            win = userWinText() # Print 'YOU WIN'
            input('Enter to continue...') # Allow the user to continue
            compFlag = False # Stop the computer from playing
            gameFlag = False # Stop the game
        blockFlag = False # Allow the user to play again
#####COMPUTER GAMEPLAY##############################################
        while compFlag == True:
            print('Now your opponent will play!') # Tell the user that the computer is going to play

            input('OKAY!') # Allow user to continue on their own time
            
            topCard = compPlay(topCard, compDeck, gameDeck) # Allow the computer to play
            oldTop = topCard # Save the previous top card
            ############################
            wS(1)
            if topCard == True: # If the user didn't have a card
                newCards = getNewCard(gameDeck) # Get the user a new card
                wS(1) # Whitespace
                for newCard in newCards: # Create a loop
                    print('Your opponent picked up a card! Your turn!') # Tell the user they picked up a new card
                gameDeck.remove(newCards) # Remove the new cards from the game deck
                compDeck.append(newCards) # Add these new cards to the cpu's cards
                compDeck.remove(topCard) # Remove the played card
                topCard = oldTop # Reset to the previous top card
                userFlag = False # Stop the user's turn
                
            if topCard[1] == 'b': # If the cpu played a block
                wS(1) # Whitespace
                print('Your turn has been blocked!')
                blockFlag = True # Stop the user from playing one round
                compDeck.remove(oldTop) # Remove the played card
            elif topCard[1] == 'r': # If the cpu played a reverse card
                print('The game reverses back to your opponent!')
                compDeck.remove(topCard) # Remove the played card
                blockFlag = True # Stop the user from playing
                
            elif topCard[1] == '+': # If the cpu plays a Plus Four
                print('You must pick up 4 cards!') # Tell the user they need to pick up cards
                for cards in range(0,4): # A loop that runs 4 times
                    card = getNewCard(gameDeck) # Generate 4 new cards for the user
                    gameDeck.remove(card) # Remove the new card from the deck
                    userDeck.append(card) # Add these cards to the computer deck
                try:
                    compDeck.remove(oldTop) # Remove the top card from the computer deck
                except:
                    compFlag = False # Stop the computers turn
                    wS(1) # Whitespace
                    print('Something went wrong. You play again!') # Tell the user there was an error
                colorChangeChoices = ['Rz', 'Gz', 'Bz', 'Yz'] # Set a list
                compColourChoice = random.choice(colorChangeChoices) # Pick a random thing from the list
                wS(1) # Whitespace
                if compColourChoice == 'Rz': # If the computer changed it to red
                    print('Your opponent changed the colour to Red!') # Print the colour change
                elif compColourChoice == 'Bz': # If the computer changed it to blue
                    print('Your opponent changed the colour to Blue!') # Print the colour change
                elif compColourChoice == 'Gz': # If the computer changed it to green
                    print('Your opponent changed the colour to Green!') # Print the colour change
                elif compColourChoice == 'Yz': # If the computer changed it to yellow
                    print('Your opponent changed the colour to Yellow!') # Print the colour change
                topCard = compColourChoice # Pick the new topcard
                
            elif topCard[1] == 'p': # If the cpu plays a Plus 2
                print('You must pick up 2 cards!') # Tell the user they need to pick up cards
                for cards in range(0,2): # A loop that runs 4 times
                    card = getNewCard(gameDeck) # Generate 4 new cards for the user
                    gameDeck.remove(card) # Remove the new card from the deck
                    userDeck.append(card) # Add these cards to the user deck
                try:
                    compDeck.remove(oldTop) # Remove the top card from the computer deck
                except:
                    compFlag = False # Stop the computers turn
                    wS(1) # Whitespace
                    print('Something went wrong. You play again!') # Tell the user there was an error

            elif topCard[1] == 'x': # If the top card is a colour Change
                choices = ['Rz', 'Gz', 'Bz', 'Yz'] # List of choices
                compDeck.remove(topCard) # Remove the topcard from the computer deck
                topCard = random.choice(choices) # Make the top card a random choice
                wS(1) # Whitespace
                if topCard == 'Rz': # If the computer changed it to red
                    print('Your opponent changed the colour to Red!') # Print the colour change
                elif topCard == 'Bz': # If the computer changed it to blue
                    print('Your opponent changed the colour to Blue!') # Print the colour change
                elif topCard == 'Gz': # If the computer changed it to green
                    print('Your opponent changed the colour to Green!') # Print the colour change
                elif topCard == 'Yz': # If the computer changed it to yellow
                    print('Your opponent changed the colour to Yellow!') # Print the colour change
            compFlag = False # Stop the computers turn
            if topCard in compDeck: # If the card is still in then
                compDeck.remove(topCard) # Remove the top card from the computer deck

        if len(compDeck) == 1: # If the computer has one card
            wS(1) # Whitespace
            print('Opponent: UNO!') # The computer says uno

        if len(compDeck) == 0: # If the computer runs out of cards
            gameFlag = False # Stop the game.
            print('Opponent: UNO Out!') # Print the final statement
            wS(1) # Whitespace
            win = userLoseText() # Print 'YOU WIN'
            input('Enter to continue...') # Allow the user to continue
            userFlag = False # Stop the user from playing
            gameFlag = False # Stop the game
    return win # Return the winner
def genDeck(): # Function that creates the game deck

    # List of Red Cards 
    red = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'Rr', 'Rb', 'Rp']

    # List of Green Cards
    green = ['G0','G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9','G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'Gr', 'Gb', 'Gp'] 
    # List of Blue Cards

    blue = ['B0','B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B7', 'B8', 'B9','B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B7', 'B8', 'B9', 'Br', 'Bb', 'Bp'] 
    
    # List of Yellow Cards
    yellow = ['Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Yr', 'Yb', 'Yp'] 
    
    # List of Colour-Change Cards
    colorChange = ['Cx', 'Cx', 'Cx', 'Cx'] 
  
    #List of Plus Four Cards
    plusFour = ['P+', 'P+', 'P+', 'P+']

    defaultDeck = red + green + blue + yellow + colorChange + plusFour# Concatenate all of the cards into one list

    deck = random.sample(defaultDeck, len(defaultDeck)) # Retrieve random cards

    return deck # Return this list to the program

def distUserCards(shuffledDeck): # Function that gives the user cards
    
    usersDeck = [] # Create blank list
    for items in shuffledDeck[:7]: # Retrieve the first 7 cards
        usersDeck.append(items) # Append these cards to the user's deck
    return usersDeck # Return this list to the program

def distCompCards(shuffledDeck): # Function that distributes computer cards
    
    compsDeck = [] # Create an empty list
    for items in shuffledDeck[7:14]: # For loop giving the computer the next 7 cards in the deck
        compsDeck.append(items) # shuffled deck
    return compsDeck # Return the cards

def removeDistCards(shuffledDeck): # Removes the cards

    del(shuffledDeck[:14]) # Delete the distributed cards
    wS(1) # Whitespace
    return shuffledDeck # Return this value to the program

def helpMenu(): # Function that explains the game to the user via website
    
    url = 'https://uno-website--aldendemello.repl.co'
    webbrowser.open(url)

    input('Press any key to continue...') # Allow user to continue on their own time
    wS(100) # Whitespace
    welcomeChoice = welcomeScreen(winCount, loseCount) # Display the welcome menu
    return welcomeChoice # Return the user's choice to the program

def quitMenu(): # Function that allows the user to quit
    print('Thank you for playing UNO!') # Thank the user for playing
    quit = True # Create a boolean
    return quit # Return this to the program
winCount = 0 # Running Total
loseCount = 0 # Running total
programLoop = True # Loop for the program to run
while programLoop == True: # When the program is running
    welcomeChoice = welcomeScreen(winCount, loseCount) # Display the welcome menu
    if welcomeChoice == 'user': # If the user won
        winCount += 1 # Add 1 to the running total
    elif welcomeChoice == 'cpu': # If the user lost
        loseCount += 1 # Add 1 to the running total
    if welcomeChoice == True: # If the user quits
        programLoop = False # Stop the game
