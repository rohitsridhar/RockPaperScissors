from random import randint
import time

# create a list of play options
t = {"1": "Rock", "2": "Paper", "3": "Scissors"}

# assign a random play to the computer
computer = randint(1, 3)

# set player to False
player = False

while not player:
    # set player to True
    print("Choose 1 of the following:")
    print("1.Rock \n2.Paper \n3.Scissors \n4.Quit")
    player = input()
    if player == "4":
        print("Thanks for playing!")
        break
    print("You chose:", t.get(player))
    print("Computer chose:", t.get(str(computer)))
    time.sleep(1)
    if player == str(computer):
        print("Tie!")
    elif player == "1":
        if computer == 2:
            print("You lose!", t.get(str(computer)), "covers", t.get(player) + ".")
        else:
            print("You win!", t.get(player), "smashes", t.get(str(computer))+".")
    elif player == "2":
        if computer == 3:
            print("You lose!", t.get(str(computer)), "cuts", t.get(player)+".")
        else:
            print("You win!", t.get(player), "covers", t.get(str(computer))+".")
    elif player == "3":
        if computer == 1:
            print("You lose!", t.get(str(computer)), "smashes", t.get(player)+".")
        else:
            print("You win!", t.get(player), "cut", t.get(str(computer))+".")
    else:
        print("Invalid choice. Choose again.")
    print()
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = randint(1, 3)
