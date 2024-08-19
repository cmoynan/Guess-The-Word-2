import random

words = [
    "apple", "banana", "orange", "strawberry", "grape",
    "pineapple", "watermelon", "mango", "melon", "cranberry",
    "blueberry", "kiwi", "pear", "peach", "plum",
    "apricot", "cherry", "pomegranate", "coconut", "papaya"
]
guessed_words = []

def choose_word(words):
    """
    Randomly chooses a word from the array to begin the game.
    """
    chosen_word = random.choice(words)

    # Remove the chosen word from the list to prevent repetition
    words.remove(chosen_word)
    return chosen_word

