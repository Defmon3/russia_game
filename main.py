"""
https://www.youtube.com/watch?v=oKO-jx5JKak
"""
import random

def main():
    """
    Main function to run the Russian Alphabet Quiz Game.
    
    """
    alphabet = [
        {'russian': 'А', 'english': 'a', 'hint': 'AKMOT'},
        {'russian': 'Б', 'english': 'b', 'hint': 'brigade'},
        {'russian': 'В', 'english': 'v', 'hint': 'van'},
        {'russian': 'Г', 'english': 'g', 'hint': 'looks like a "gun"'},
        {'russian': 'Д', 'english': 'd', 'hint': 'dog'},
        {'russian': 'Е', 'english': 'ye', 'hint': 'yes'},
        {'russian': 'Ё', 'english': 'yo', 'hint': 'Two egg "yolks" on top'},
        {'russian': 'Ж', 'english': 'zh', 'hint': 'pleasure'},
        {'russian': 'З', 'english': 'z', 'hint': 'zapad'},
        {'russian': 'И', 'english': 'i', 'hint': 'machine, Not N'},
        {'russian': 'Й', 'english': 'y', 'hint': 'toy, май (may)'},
        {'russian': 'К', 'english': 'k', 'hint': 'AKMOT'},
        {'russian': 'Л', 'english': 'l', 'hint': 'lamp'},
        {'russian': 'М', 'english': 'm', 'hint': 'AKMOT'},
        {'russian': 'Н', 'english': 'n', 'hint': 'no'},
        {'russian': 'О', 'english': 'o', 'hint': 'AKMOT'},
        {'russian': 'П', 'english': 'p', 'hint': 'pet'},
        {'russian': 'Р', 'english': 'r', 'hint': "a rolled 'r'"},
        {'russian': 'С', 'english': 's', 'hint': 'see'},
        {'russian': 'Т', 'english': 't', 'hint': 'AKMOT'},
        {'russian': 'У', 'english': 'u', 'hint': 'boot'},
        {'russian': 'Ф', 'english': 'f', 'hint': 'fan'},
        {'russian': 'Х', 'english': 'ch', 'hint': 'bach'},
        {'russian': 'Ц', 'english': 'ts', 'hint': 'cats'},
        {'russian': 'Ч', 'english': 'ch', 'hint': 'church'},
        {'russian': 'Ш', 'english': 'sh', 'hint': 'shut'},
        {'russian': 'Щ', 'english': 'sch', 'hint': "sounds like 'sh' and 'ch' together"},
        {'russian': 'Э', 'english': 'e', 'hint': 'met'},
        {'russian': 'Ю', 'english': 'yu', 'hint': 'use'},
        {'russian': 'Я', 'english': 'ya', 'hint': 'yard'},
    ]
    
    print("Welcome to the Russian Alphabet Quiz!")
    print("Enter the English transliteration for the given Russian letter.")
    print("Type 'hint' for a hint, or 'exit'/'quit' to stop the game.")

    correct_guesses = 0
    wrong_guesses = 0
    hints_used = 0

    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)

    for letter in shuffled_alphabet:
        russian_letter_original = letter['russian']
        english_equivalent = letter['english']
        
        while True:
            # Randomly choose between uppercase and lowercase for the displayed letter
            russian_letter_display = russian_letter_original.lower() if random.choice([True, False]) else russian_letter_original.upper()

            user_input = input(f"What is the English equivalent of '{russian_letter_display}'? ").strip().lower()

            if user_input in ['exit', 'quit']:
                print("Thanks for playing!")
                print("\n--- Game Stats ---")
                print(f"Correct Guesses: {correct_guesses}")
                print(f"Wrong Guesses: {wrong_guesses}")
                print(f"Hints Used: {hints_used}")
                return

            if user_input == 'hint':
                print(f"Hint: {letter['hint']}")
                hints_used += 1
                continue

            if user_input == english_equivalent.lower():
                print("Correct!")
                correct_guesses += 1
                break
            else:
                print("Sorry, that's not right. Try again.")
                wrong_guesses += 1
    
    print("\nCongratulations! You have completed the entire Russian alphabet!")
    print("\n--- Final Stats ---")
    print(f"Correct Guesses: {correct_guesses}")
    print(f"Wrong Guesses: {wrong_guesses}")
    print(f"Hints Used: {hints_used}")

if __name__ == "__main__":
    main()
