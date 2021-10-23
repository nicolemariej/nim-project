from random import randrange
#set players
print("Welcome to NIM")
print("Hello, I am AI player, please tell me a little bit more about yourself...")
player1 = input("Player 1, what is your name? ")
player1Name = player1.capitalize()

player1Id = input("Player 1, what is your MIT student ID? ")
print("Welcome", player1Name)
player2 = input("Player 2, what is your name? ")
player2Name = player2.capitalize()
player2Id = input("Player 2, what is your MIT student ID? ")
print("Welcome", player2Name)

#set amount of stones
while True:
    amountOfStones = int(input(player1Name + " please select a number between 30 - 50 "))
    if amountOfStones in [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]:
        break
    print("The number must be between 30-50")
#set move

move = int(input("Select how many stones you would like to remove: "))

# update state

amountOfStones = amountOfStones - move

# show new state

print("There are", amountOfStones, " remaining")

#set player
