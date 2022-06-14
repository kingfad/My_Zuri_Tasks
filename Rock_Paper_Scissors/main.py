import random

print("""Welcome! 
This is the Rock-Paper-Scissors game.""")

while True:
    # Options for users to enter when the game starts
    list = {
        "R" : "Rock",
        "P" : "Paper",
        "S" : "Scissors"
    }

    #Taking input(as choices) from the users
    user = input("""What's is your choice?
                    R for Rocks
                    P for Paper
                    S for Scissors
                    Choose one: """).upper()
    #possible options to choose from
    possible_options = ["R", "P", "S"]
    #Defining CPU's choice
    computer = random.choice(possible_options)

    #Condition, if it's a tie (user move == computer move)
    if (user == computer):
        print(f"Players' move: Player({list[user]}) : CPU({list[computer]}).\n")
        print(f"\nYou chose {list[user]}, computer chose {list[computer]}, its's a TIE!\n")

    #Condition, to check for win or lose
    elif (user == "R"):
        if (computer == "S"):
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("Rock beats scissors! You WIN!")
            break
        else:
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("""
            Paper beats rock! You LOSE!
            CPU win """)
            break
    elif (user == "P"):
        if (computer == "R"):
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("Paper beats rock! You WIN!")
            break
        else:
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("""
            Scissors beats paper! You LOSE!
            CPU win
             """)
            break
    elif (user == "S"):
        if (computer == "P"):
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("Scissors beats paper! You WIN!")
            break
        else:
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("""
            Rock beats scissors! You LOSE!
            CPU win """)
            break
    else:
        print("""
                You entered an invalid input.
                Play again...!
                """)
        continue


