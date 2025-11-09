"""
https://www.youtube.com/watch?v=oKO-jx5JKak
"""
import random

def main():
    """
    Main function to run the Russian Alphabet Quiz Game.
    These characters are just the same as in english = AKMOT Remebery it sounds almost like (Akhmat)
    """
    alphabet = [
        {'russian': 'А', 'english': ['a'], 'hint': 'AKMOT'},
        {'russian': 'Б', 'english': ['b'], 'hint': 'brigade, бригада'},
        {'russian': 'В', 'english': ['v'], 'hint': 'ВДВ, Военный, Airborne Troops '},
        {'russian': 'Г', 'english': ['g'], 'hint': 'gun, Горлівка'},
        {'russian': 'Д', 'english': ['d'], 'hint': 'дивизия, Division'},
        {'russian': 'Е', 'english': ['ye', 'ie'], 'hint': 'Еда, "yeda" = food, looks like a fork'},
        {'russian': 'Ё', 'english': ['yo', 'io'], 'hint': 'Two egg "yolks" on top'},
        {'russian': 'Ж', 'english': ['zh'], 'hint': 'pleasure, Запоріжжя'},
        {'russian': 'З', 'english': ['z'], 'hint': 'zapad, Запоріжжя'},
        {'russian': 'И', 'english': ['i'], 'hint': 'machine, Not N'},
        {'russian': 'Й', 'english': ['y'], 'hint': 'toy, май (May), baby yoda'},
        {'russian': 'К', 'english': ['k'], 'hint': 'AKMOT'},
        {'russian': 'Л', 'english': ['l'], 'hint': 'lamp, Лагерь = lager'},
        {'russian': 'М', 'english': ['m'], 'hint': 'AKMOT'},
        {'russian': 'Н', 'english': ['n'], 'hint': 'no, нос = Nose'},
        {'russian': 'О', 'english': ['o'], 'hint': 'AKMOT'},
        {'russian': 'П', 'english': ['p'], 'hint': 'pet "полк" = polk/regiment'},
        {'russian': 'Р', 'english': ['r'], 'hint': "Россия = Russia"},
        {'russian': 'С', 'english': ['s'], 'hint': 'see, C-400 = S-400'},
        {'russian': 'Т', 'english': ['t'], 'hint': 'AKMOT'},
        {'russian': 'У', 'english': ['u'], 'hint': 'boot, Украина = Ukraine'},
        {'russian': 'Ф', 'english': ['f'], 'hint': 'fan, ".РФ" = for russian feredarion'},
        {'russian': 'Х', 'english': ['kh', 'h'], 'hint': 'bach, Херсон'},
        {'russian': 'Ц', 'english': ['ts'], 'hint': 'tooks like tsar hat, цель = target'},
        {'russian': 'Ч', 'english': ['ch'], 'hint': 'church, Чернігів = Chernihiv'},
        {'russian': 'Ш', 'english': ['sh'], 'hint': 'shut, штурм = shturm'},
        {'russian': 'Щ', 'english': ['shch', 'sch'], 'hint': "sounds like 'sh' and 'ch' together, ща = shcha/soon "},
        {'russian': 'Э', 'english': ['e'], 'hint': 'met, EUR '},
        {'russian': 'Ю', 'english': ['yu', 'iu'], 'hint': 'IO you'},
        {'russian': 'Я', 'english': ['ya', 'ia'], 'hint': 'Ялта, yalta'},
    ]
    
    print("For an easy start, watch this video: https://www.youtube.com/watch?v=oKO-jx5JKak ")
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

            if user_input in [e.lower() for e in english_equivalent]:
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
