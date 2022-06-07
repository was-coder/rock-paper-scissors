import random

# game scores
won = 0
lost = 0
tie = 0
total = 0


# printing player and computer choices
def get_value():
    print("\nComputer Picks : ", computer)
    print("You Pick : ", player)


isPlayAgain = True

while isPlayAgain:
    print("\n**** LET'S ROCK THIS PAPER WITH A SCISSORS ****")

    pickChoices = ["rock", "paper", "scissors"]

    computer = random.choice(pickChoices)

    # making sure player choice in list
    player = None
    while player not in pickChoices:
        print("\nOption should be a string among the choices")
        player = input("Pick a choice from : \nRock\nPaper\nScissors\n").lower()

    # game options
    if player == computer:
        get_value()
        print("It is a tie")
        tie += 1
        total += 1

    elif player == "rock":
        if computer == "paper":
            get_value()
            print("You lose")
            lost += 1
            total += 1
        if computer == "scissors":
            get_value()
            print("You win")
            won += 1
            total += 1

    elif player == "paper":
        if computer == "rock":
            get_value()
            print("You win")
            won += 1
            total += 1
        if computer == "scissors":
            get_value()
            print("You lose")
            lost += 1
            total += 1

    elif player == "scissors":
        if computer == "rock":
            get_value()
            print("You lose")
            lost += 1
            total += 1
        if computer == "paper":
            get_value()
            print("You win")
            won += 1
            total += 1

    print("\nGames Won : %d, Games Lost : %d, Games Tied : %d, Total Games Played : %d" % (won, lost, tie, total))

    # continue or stop game
    play_again = input("\nDo you want to play again?\nYes\nNo\n").lower()
    if play_again != "yes":
        break

print("\nGame Over... Try Again Next Time")
