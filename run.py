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

def main():
    # Make 'words' accessible globally
    global words
    correct_guesses = 0

    # Display game description
    print("\033[33mWelcome to Guess the Word!\033[0m\n")
    print("In this game, you will attempt to guess a hidden word letter by letter.")
    print("Each word is a type of fruit, and you have a limited number of attempts to guess the word correctly.")
    print("The difficulty level you choose will determine how many attempts you have to guess each word.")
    print("\n\033[36mGood luck!\033[0m\n")

    # Let the player choose difficulty level
    while True:
        difficulty = input(
            "\033[32mChoose difficulty level:\n"
            "\033[92m1. Easy (8 attempts)\033[0m\n"
            "\033[33m2. Hard (6 attempts)\033[0m\n"
            "\033[31m3. Extreme (4 attempts)\033[0m\n"
            "Type '1', '2', or '3': \033[0m"
        ).lower()

        if difficulty == "1":
            attempts = 8
            break
        elif difficulty == "2":
            attempts = 6
            break
        elif difficulty == "3":
            attempts = 4
            break
        else:
            print("\n\033[31mError: Please choose '1', '2', or '3'.\033[0m")

    # Randomly select 6 words from the words list for this game
    selected_words = random.sample(words, 6)

    while True:
        # If the game returns False (indicating it's over), exit the loop
        if not play_game(selected_words, attempts):
            # Calculate the score by counting the guessed words
            score = len(guessed_words)
            print(f"\n\033[33mYou guessed {score} /6 words correctly.\033[0m")

            # If there are no more words left to play
            if not selected_words:
                print("\n\033[33mThanks for playing. We hope to see you again soon\033[0m")
                break

            # Prompt the user if they want to play again
            play_again = input("\nDo you want to play again? (y/n): ").lower()

            if play_again != 'y':
                print("\033[33mThanks for playing. We hope to see you again soon\033[0m")
                break

            # Reset the 'words' list and 'guessed_words' list for a new game
            selected_words = random.sample(words, 6)
            guessed_words.clear()

main()