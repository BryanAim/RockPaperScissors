#

# Create an infinite loop for the application
while True:
    print("Selection: Rock | Paper | Scissors")

    # Ask the users for their selection
    playerOne = input("Player One Input: ")
    playerTwo = input("Player Two Input: ")

    # Compare the input of the two users and determine
    # The winner based on the games rules

    if playerOne == playerTwo:
        print("Its a tie!")
    elif playerOne == "rock" and playerTwo == "scissors" or playerOne == "paper" and playerTwo == "rock" or playerOne == "scissors" and playerTwo == "paper":
        print("Player One Wins!")
    else:
        print("PLayer Two Wins!")
