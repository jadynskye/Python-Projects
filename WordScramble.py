"""
    Word Scramble Guessing Game
    ----------------------------------------------
    In this game, the computer randomly selects a word from a list of words, it
    scrambles the letters, and then shows the scrambled word to the player.
    The player has to guess what the original word is.
    They only get a limited number of attempts to guess correctly.
    The game gives feedback after each guess and shows the correct answer if the player runs out of tries.
    This helps practice string manipulation, loops, conditionals, and randomness in Python. Enjoy!!! 
    Coded by : Jadyn Reid

"""
import random


word_list = [
    "apple", "banana", "orange", "python", "jungle", "wizard", "pizza", "garden", "sunset", "mirror",
    "cactus", "winter", "galaxy", "rocket", "bubble", "ocean", "rainbow", "laptop", "cookie", "secret",
    "castle", "desert", "dragon", "future", "pirate", "island", "coffee", "window", "panda", "thunder",
    "eclipse", "zipper", "volcano", "button", "hammock", "puzzle", "icecream", "monster", "planet", "lantern",
    "violin", "feather", "tunnel", "magic", "soccer", "unicorn", "camera", "popcorn", "robot", "sparkle"
]


#choose random word from list
chosen_word = random.choice(word_list)

#change word to a list to be able to use the shuffle method
list_word = list(chosen_word)

#shuffle word(aka list now)
random.shuffle(list_word)

#make list into string again
final_scramble = ''.join(list_word)


def main():

    attempts = 3

    while attempts > 0:

        print(f"Scrambled word: {final_scramble}")
        users_guess = input("Your guess: ")
        if users_guess == chosen_word:
            print(f"Correct! The word was {chosen_word}")
            return
        else: 
            attempts -= 1
            print(f"Sorry that was not correct. Attempts left: {attempts}")

    print(f"The correct word was {chosen_word}")

main() 