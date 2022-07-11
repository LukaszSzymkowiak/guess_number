"""Guess a number game!"""

from functions import *


# main
def main():
    while True:
        game_choice = input("User guess = 'u'\n"
                            "Computer guess = 'c'\n"
                            "Your choice: ").lower()
        if game_choice.isalpha() and game_choice in ["u", "c"]:
            if game_choice == "u":
                user_guessing()
                break
            elif game_choice == "c":
                computer_guessing()
                break
        else:
            print("Incorrect command.")
            continue


if __name__ == "__main__":
    main()
