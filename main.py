from random import randrange
#set players
print("Welcome to ")
print("   /|   /   |       /|   /|")
print("  / |  /    |      / |  / |")
print(" /  | /     |     /  | /  |")
print("/   |/      |    /   |/   |")
print("\nRules:\n1. The first player will select the amount of stones from 30-50\n2.Players will then take it in turn to remove either 1, 2 or 3 stones.\n3. The player to remove the last stone wins!")
print("\nOK, now let's get started! please tell me a little bit more about yourself...")
player1Name = input("Player 1, what is your name? ")
player1 = player1Name.capitalize()

player1Id = input("Player 1, what is your MIT student ID? ")
print("Welcome", player1)
player2Name = input("Player 2, what is your name? ")
player2 = player2Name.capitalize()
player2Id = input("Player 2, what is your MIT student ID? ")
print("Welcome", player2)

#set amount of stones
while True:
    amountOfStones = int(input(player1 + " please select a number between 30 - 50 "))
    if amountOfStones in [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]:
        break
    print("The number must be between 30-50")
#set move
while True:
    move = int(input("Select how many stones you would like to remove: "))
    if move in [1,2,3]:
        break
    print("Invalid number. You must select a number from 1-3.")

# update state

amountOfStones = amountOfStones - move

# show new state

print("There are", amountOfStones, " remaining")

#set player