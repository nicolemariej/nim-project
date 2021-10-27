def stonePick():
#set players
    print("Welcome to ")
    print("   /|   /   |       /|   /|")
    print("  / |  /    |      / |  / |")
    print(" /  | /     |     /  | /  |")
    print("/   |/      |    /   |/   |")
    print("\nRules:\n1. The first player will select the amount of stones from 30-50\n2.Players will then take it in turn to remove either 1, 2 or 3 stones.\n3. The player to remove the last stone wins!")
    print("\nOK, now let's get started! please tell me a little bit more about yourself...")


    player1 = input("Player 1: Please enter you name: ").capitalize()
    player1Id = input("Please enter your ID number: ")
    print("Welcome " + player1 +"!")
    player2 = input("Player 2: Please enter your name: ").capitalize()
    player2ID = input("Please enter your ID number: ")
    print("Welcome " + player2 +"!")


    #set amount of stones
    while True:
        amountOfStones = int(input(player1 + " please select a number between 30 - 50 "))
        if amountOfStones in range(30, 51):
            print(f"There are {amountOfStones} stones")
            break
        else:
         print("The number must be between 30-50")


    #set move
    def selectStone(amountOfStones):
        while True:
           try:
                move = int(input("Select how many stones you would like to remove: "))
                if move in range(1, 4) and (amountOfStones - move) >= 0:
                    amountOfStones -= move
                    print(f"There are {amountOfStones} remaining")
                    return amountOfStones
                elif amountOfStones - x < 0:
                    print("There are not that many stones available. Try again.")
                else:
                    print("You can only select 1-3 stones, please try again")
           except:
                print("You can only select 1-3 stones, please try again")

    while amountOfStones > 0:
        print(f"{player1}: Please take your turn: ")
        amountOfStones = selectStone(amountOfStones)
        if amountOfStones == 0:
            print(f"Congratulations {player1}, you have won!")
            break
        print(f"{player2}: Please take your turn: ")
        amountOfStones = selectStone(amountOfStones)
        if amountOfStones == 0:
            print(f"Congratulations {player2}, you have won!")
            break
            print("AI: Please take your turn")
        if amountOfStones == 3:
            amountOfStones -= 3
            print(f"I have taken 3 stones, the remaining amount of stones are {amountOfStones}.")
        if amountOfStones > 0:
            if amountOfStones / 3 == 0:
                amountOfStones -= 2
                print(f"I have taken 2 stones, the remaning amount of stones are {amountOfStones}.")
            else:
                amountOfStones -= 1
                print(f"I have taken 1 stone, the remaining stones are {amountOfStones}")
            if amountOfStones == 0:
                 print("AI has won!!")


while True:
    print("Welcome \n Press any key to continue...")
    stonePick()
    playAgain = input("Would you like to play again?\n (yes)/(y) or (no)/(n) ")
    if playAgain.lower() == 'y' or playAgain.lower() == 'yes':
        print("Great, let's play!")
        continue
    elif playAgain.lower() == 'n' or playAgain.lower() == 'no':
        print("OK, have a nice day!")
    else:
        print("I didn't quite get that... so let's play again!")
