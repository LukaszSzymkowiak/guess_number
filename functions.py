from random import *


# User guess
def user_guessing():
    tries = 0
    start_range = int(input("Set start range for game: "))
    end_range = int(input("Set end range for game: "))
    random_number = randint(start_range, end_range)
    print(f"Guess a number in range {start_range}-{end_range}.")
    user_number = None
    while user_number != random_number:
        user_number = int(input("Guess a number: "))
        tries += 1
        if user_number > random_number:
            print("Too high")
        elif user_number < random_number:
            print("Too low")
    print(f"Correct!\n"
          f"Tries: {tries}")


# Computer guess
def computer_guessing():
    low_range = int(input("Choose low range for game: "))
    high_range = int(input("Choose high range for game: "))
    user_number = int(input(f"Choose a number in range {low_range} - {high_range}: "))
    user_answer = None
    tries = 0
    while user_answer != "c" and low_range != high_range:
        print(f"Your number is {user_number}")
        computer_number = randint(low_range, high_range)
        tries += 1
        print(f"Computer number is: {computer_number}")
        user_answer = input("Correct - 'c'\n"
                            "Too high - 'h'\n"
                            "Too low - 'l'\n")
        if user_answer == "h":
            high_range = computer_number - 1
        elif user_answer == "l":
            low_range = computer_number + 1
    print(f"Correct!\n"
          f"Tries: {tries}")
