from random import *


def user_guessing_game():
    tries = 0
    while True:
        try:
            start_range = int(input("Set start range for game: "))
            end_range = int(input("Set end range for game: "))
            if start_range and end_range:
                break
        except ValueError:
            print("Type a number")
    random_number = randint(start_range, end_range)
    print(f"Guess a number in range {start_range}-{end_range}.")
    while True:
        try:
            user_number = int(input("Guess a number: "))
            tries += 1
            if user_number == random_number:
                break
            elif user_number > random_number:
                print("Too high")
            elif user_number < random_number:
                print("Too low")
        except ValueError:
            print("Type a number")

    print(f"Correct!\n"
          f"Tries: {tries}")


def computer_guessing_game():
    tries = 0
    while True:
        try:
            low_range = int(input("Choose low range for game: "))
            high_range = int(input("Choose high range for game: "))
            user_number = int(input(f"Choose a number in range {low_range} - {high_range}: "))
            if low_range and high_range and user_number:
                break
        except ValueError:
            print("Type a number")
    user_answer = None
    while user_answer != "c" and low_range != high_range:
        print(f"Your number is {user_number}")
        computer_number = randint(low_range, high_range)
        tries += 1
        print(f"Computer number is: {computer_number}")
        while user_answer != "c":
            user_answer = input("Correct - 'c'\n"
                                "Too high - 'h'\n"
                                "Too low - 'l'\n").lower()
            if user_answer.isdigit() or user_answer not in ("h", "l", "c"):
                print(f"Your number: {user_number}\nComputer number: {computer_number}\nType a correct letter.")
                continue
            if user_answer == "h":
                high_range = computer_number - 1
                break
            elif user_answer == "l":
                low_range = computer_number + 1
                break
    print(f"Correct!\n"
          f"Computer tries: {tries}")
