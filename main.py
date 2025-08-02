"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Berounský
email: berounsky.pavel@gmail.com
"""

import random
import time


def print_intro():
    print("Hi there!")
    print("-" * 60)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a Bulls and Cows game.")
    print("-" * 60)


def generate_secret_number():
    """
    Funkce vrací náhodné 4 místné číslo,
    které splňuje tyto podmínky: 
    1. každá číslice je unikátní - neopakuje se
    2. číslo nesmí začínat 0
    Návratová hodnota:
    list: Seznam 4 unikátních číslic, např. [1, 2, 3, 4]
    """
    i = random.sample(range(1, 4), 1)[0]
    number = random.sample(range(10), 4)
    if number[0] == 0:
        number[0], number[i] = number[i], number[0]
    return number

def validate_input(user_input):
    """
    Funkce ověřuje platnost uživatelem zadaných hodnot
    1 - číslo musí obsahovat právě 4 znaky - číslice
    2 - zadaná hodnota nesmí začínat 0
    3 - v zadaném čísle musí být jen unikátní číslice (nesmí se opakovat)
    Návratová hodnota:
    tuple: (bool, str) - zda je vstup validní, a případná chybová zpráva
    """

    if len(user_input) != 4:
        return False, "Your guess must be exactly 4 digits."
    if not user_input.isdigit():
        return False, "Only numeric characters are allowed."
    if user_input[0] == "0":
        return False, "The number must not start with zero."
    if len(set(user_input)) != 4:
        return False, "Digits must be unique."
    return True, ""


def count_bulls_and_cows(secret, guess):
    """
    Spočítá počet bulls a cows mezi tajným číslem a hádaným číslem.

    'Bull' = správná číslice na správné pozici
    'Cow' = správná číslice na jiné pozici

    Parametry:
    secret (str): Tajné číslo (např. '1234')
    guess (str): Tip hráče (např. '1324')

    Návratová hodnota:
    tuple: (bulls, cows) - počet bulls a cows jako celá čísla
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def format_result(bulls, cows):
    """
    Vytvoří textový výstup s ohodnocením bulls a cows.
    
    Přizpůsobuje jednotné vs. množné číslo.

    Parametry:
    bulls (int): počet bulls
    cows (int): počet cows

    Návratová hodnota:
    str: textový výsledek, např. '2 bulls, 1 cow'
    """
    
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"


def play_game():
    """
    Spouští hlavní smyčku hry Bulls & Cows.
    
    - generuje tajné číslo
    - přijímá tipy uživatele
    - vypisuje počet bulls a cows po každém pokusu
    - ukončí hru po správném tipu a zobrazí statistiky
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

        if bulls == 4:
            duration = round(time.time() - start_time)
            print("-" * 60)
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print(f"That’s amazing! Time taken: {duration} seconds")
            break

if __name__ == "__main__":
    print_intro()
    play_game()

