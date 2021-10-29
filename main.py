def stonePick():#Function that plays the entire game from the start
#introduction to the game
    print("Welcome to ")
    print("   /|   /   |       /|   /|")
    print("  / |  /    |      / |  / |")
    print(" /  | /     |     /  | /  |")
    print("/   |/      |    /   |/   |") #On the screen, this will display an image of the word "NIM"
    print("\nRules:\n1. The first player will select the amount of stones from 30-50\n2.Players will then take it in turn to remove either 1, 2 or 3 stones.\n3. The player to remove the last stone wins!")
    print("\nOK, now let's get started! please tell me a little bit more about yourself...")

#Players input their details
    player1 = input("Player 1: Please enter you name: ").capitalize()#This variable will be capitalised and called throughout the game in place of player 1
    player1Id = input("Please enter your ID number: ")
    print("Welcome " + player1 +"!")
    player2 = input("Player 2: Please enter your name: ").capitalize()#This variable will be capitalised and called throughout the game in place of player 2
    player2ID = input("Please enter your ID number: ")
    print("Welcome " + player2 +"!")


    #Amount of stones is decided on
    while True:
        amountOfStones = int(input(player1 + " please select a number between 30 - 50 "))#Player 1 is asked to set the amount of stones
        if amountOfStones in range(30, 51): #If they type anything other than a full number ranging from 30-50 and error message will ask them to try again
            print(f"There are {amountOfStones} stones")
            break
        else:
         print("The number must be between 30-50")
#The game will not continue until the player has selected a valid number

    #Players decide on how many stones to remove
    def selectStone(amountOfStones):#Once the game has annonced it is player 1 or 2's turn, this function is called.
        while True:
           try:
                move = int(input("Select how many stones you would like to remove: "))
                if move in range(1, 4) and (amountOfStones - move) >= 0:
                    amountOfStones -= move#Calculates the amount of stones remaining
                    print(f"There are {amountOfStones} remaining")#Announces the amount of stones remaining
                    return amountOfStones
                elif amountOfStones - move < 0:#Ensures a player doesn't enter more stones that are available
                    print("There are not that many stones available. Try again.")
                else:
                    print("ERROR! You can only select 1-3 stones, please try again")#Error messages are printed if anything other than 1, 2 or 3 are selected.
           except:
                print("ERROR! You can only select 1-3 stones, please try again")#This function is
#Loop until there are no stones then a winner is announced
    while amountOfStones > 0: #A loop that continues until there are no stones, asking the players to select a stone number and annoucing the AI's go. Once the amount reaches 0 the loop stops and the winner is announced.
        print(f"{player1}: Please take your turn: ")
        amountOfStones = selectStone(amountOfStones)#Sends the number of stones to the selectStones function
        if amountOfStones == 0: #If amount is 0, the winner is announced
            print(f"Congratulations {player1}, you have won!")
            break
        print(f"{player2}: Please take your turn: ")
        amountOfStones = selectStone(amountOfStones)
        if amountOfStones == 0:
            print(f"Congratulations {player2}, you have won!")
            break
            print("AI: Please take your turn")
#AI algorithm
        if amountOfStones == 3: #If there are 3 stones, the AI will remove 3 stones
            amountOfStones -= 3
            print(f"I have taken 3 stones, the remaining amount of stones are {amountOfStones}.") #this announcement will only run when the AI selects 3 stones
        if amountOfStones > 0:
            if amountOfStones % 3 == 0: # If the remainder of stones divided by 3 is 0, the AI will remove 2 stones
                amountOfStones -= 2
                print(f"I have taken 2 stones, the remaining amount of stones are {amountOfStones}.")#This message will run only when 2 stones are selected
            else:
                amountOfStones -= 1 #The AI will select 1 stone if the previous conditions are not true
                print(f"I have taken 1 stone, the remaining stones are {amountOfStones}") #Then it will announce it
        if amountOfStones == 0:#If AI takes the final stone, it announces it and the next section of code runs
            print("AI has won!!")
            break
#Once game has been completed, the players will be given the option to play again.

while True:
    input("Welcome \n Press enter to continue...")
    stonePick()
    playAgain = input("Would you like to play again?\n (yes)/(y) or (no)/(n) ") #A variable created asking the player if they wish to play again
    if playAgain.lower() == 'y' or playAgain.lower() == 'yes':
        print("Great, let's play!")
        continue
    elif playAgain.lower() == 'n' or playAgain.lower() == 'no':
        print("OK, have a nice day!")
    else:
        print("I didn't quite get that... so let's play again!")

#The game will loop until the player presses "n" or "no" in any case in the final section.