from random import randint
from time import sleep
from os import system


# Decorator
def decor():
    print("-" * 24)

# Introduce the game
def game_intro():
    print("""========== Welcome to Rock, Paper, Scissors! ==========

    You will be playing against the computer.
    """)
    sleep(1)
    print("Let's begin!")
    sleep(1)
    decor()
    print("""| The rules are simple:|
| Rock beats Scissors  |
| Scissors beats Paper |
| Paper beats Rock     |""")
    decor()

    # Verify if the player knows the rules
    while True:
        check_understanding = input("Do you understand the rules? [y/n] ")
        if check_understanding == "y":
            break
        elif check_understanding == "n":
            print("Read the rules again!")
            sleep(1)
        else:
            print("Invalid option!")
            sleep(1)
            print("Please try again!")
            sleep(1)
    decor()
    sleep(2)

# Pick up user's choice
def user_comp_choice():
    while True:
        print("""Select your option:
    [0] Rock
    [1] Paper
    [2] Scissors""")
        user_choice = int(input("> "))
        if user_choice not in range(0, 3):
            print("Invalid option!")
            sleep(1)
            print("Please try again!")
            sleep(1)
        else:
            break

    comp_choice = randint(0, 2)
    choices = ["Rock", "Paper", "Scissors"]
    decor()
    print(f"You chose: {choices[user_choice]}")
    sleep(2)
    print(f"The computer chose: {choices[comp_choice]}")
    decor()
    sleep(1)

    # Return both choices
    choices = [user_choice, comp_choice]
    return choices

# Save and print points
points = {
    "player": 0,
    "computer": 0,
    "ties": 0
}
def print_points():
    print("""    ------------------------------
    |========== Points ==========|
    |                            |""")
    print(f"    | {'Player:'.ljust(10)} {str(points['player']).center(2)} pts {'|'.rjust(10)}")
    print(f"    | {'Computer:'.ljust(10)} {str(points['computer']).center(2)} pts {'|'.rjust(10)}")
    print(f"    | {'Ties:'.ljust(10)} {str(points['ties']).center(2)} pts {'|'.rjust(10)}")
    print("    ------------------------------")

# Check if the player has won
def winner(user, comp):
    winning_combinations = [[0, 2], [1, 0], [2, 1]]
    for option in winning_combinations:
        if user == option[0] and comp == option[1]:
            points["player"] += 1
            return "YOU WON!"
        elif user == comp:
            points["ties"] += 1
            return "IT'S A TIE!"
        elif user == option[1] and comp == option[0]:
            points["computer"] += 1
            return "THE COMPUTER WON!"

# Replay the game
def replay():
    choice_replay = ""
    while choice_replay != "n":
        print("Do you want to play again? [y/n]")
        choice_replay = input("> ")
        sleep(1)
        if choice_replay == "y":
            system("cls")
            decor()
            return main()
        elif choice_replay == "n":
            print_points()
            print("========== Thank you for playing! ==========\n")
            sleep(1)
            break
        else:
            print("Invalid option!")
            sleep(1)
            print("Please try again!")
            sleep(1)

# main function
system("cls")
game_intro()
def main():
    try:
        choice_players = user_comp_choice()
        sleep(1)
        print(winner(choice_players[0], choice_players[1]))
        sleep(3)
        system("cls")
        replay()
    except:
        print("Something went wrong!")
        sleep(1)
        print("Please try again!")
        sleep(2)
        system("cls")
        main()

# Run the game
main()

# End of file
