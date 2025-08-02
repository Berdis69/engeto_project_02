"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Berounský
email: berounsky.pavel@gmail.com
"""

import random

import time

separator = "-"
length_separator = 60
length_secret_number = 4

def print_intro():
    print("Hi there!")
    print(separator * length_separator)
    print(f"I've generated a random {length_secret_number} digit number for you.")
    print("Let's play a Bulls and Cows game.")
    print(separator * length_separator)

def generate_secret_number():
    """
    The function returns a random number 
    - each digit is unique
    - first digit is not 0
    Return value:
    list: List of 4 unique digits [1, 2, 3, 4]
    """
    num_digits = length_secret_number
    digit_pool = 10 # total number of digits (0-9)
    replacement_index = random.sample(range(1, length_secret_number), 1)[0]
    number = random.sample(range(digit_pool), num_digits) 
    if number[0] == 0:
        number[0], number[replacement_index] = number[replacement_index], number[0]
    return number

def validate_input(user_input):
    """
    The function validates user input
    - The input must contain exactly 4 characters - digits only.
    - The input must not start with 0
    - Each digit must be unique
    Return value:
    tuple: (bool, str) - the input is valid, and includes an optional error message.
    """
    if len(user_input) != length_secret_number:
        return False, f"Your guess must be exactly {length_secret_number} digits."
    if not user_input.isdigit():
        return False, "Only numeric characters are allowed."
    if user_input[0] == "0":
        return False, "The number must not start with zero."
    if len(set(user_input)) != length_secret_number:
        return False, "Digits must be unique."
    return True, ""


def count_bulls_and_cows(secret, guess):
    """
    Calculates the number of bulls and cows between the secret number and the player's guess.

    'Bull' = correct digit in the correct position
    'Cow' = correct digit in the wrong position

    Parameters:
    secret (str): The secret number (example '1234')
    guess (str): The player's guess (example '1324')

    Return value:
    tuple: (bulls, cows) - number of bulls and cows as integers
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def format_result(bulls, cows):
    """
    Text output with bulls and cows evaluation.
    Adjusts singular vs. plural.

    Parameters:
    bulls (int): number of bulls
    cows (int): number of cows

    Return value:
    str: text result, example. '2 bulls, 1 cow'
    """
    
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"


def play_game():
    """
    Starts the main loop of the Bulls & Cows game.
    - generates a secret number
    - accepts user tips
    - prints the number of bulls and cows after each attempt
    - ends the game after a correct tip and displays statistics
    """
    secret = generate_secret_number()
    secret_str = ''.join(str(d) for d in secret)
    guesses = 0
    start_time = time.time()

    while True:
        user_input = input("Enter a number: ")
        is_valid, message = validate_input(user_input)
        if not is_valid:
            print(f"Invalid input: {message}")
            continue

        guesses += 1
        bulls, cows = count_bulls_and_cows(secret_str, user_input)
        print(format_result(bulls, cows))

        if bulls == length_secret_number:
            duration = round(time.time() - start_time)
            print(separator * length_separator)
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print(f"That is amazing! Time taken: {duration} seconds")
            break

if __name__ == "__main__":
    print_intro()
    play_game()

