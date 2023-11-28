import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Please select from rock, paper or scissors : ").lower()
    if computer == player:
        print("computer: " + computer)
        print("player: " + player)
        print("It's a tie")

    elif computer == "rock":
        if player == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("You won!")

        if player == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("You lost!")

    elif computer == "paper":
        if player == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("You won!")

        if player == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("You lost!")

    elif computer == "scissors":
        if player == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("You won!")

        if player == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("You lost!")

    play_again = ["yes", "no"]
    again = None
    while again not in play_again:
        again = input("Play again?yes/no: ").lower()
    if again != "yes":
        break
print("Bye")