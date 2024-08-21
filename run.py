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

def play_game(words, attempts):
    """
    Main game function.
    """
    if not words:
        print("\n\033[31mNo words left to choose from. Game over.\033[0m")
        return False  # Return False to indicate the game ends

    # Display game instructions and hint
    print(f"Try to guess the word within {attempts} attempts.")
    print("You only lose an attempt if the attempt is \033[31mincorrect\033[0m.")
    print(f"\033[32mThere are {len(words)} words")
    print("in total left to guess from.\033[0m")
    print("\n\033[33mOnce all words are guessed, you will be given a score\033[0m.")

    chosen_word = choose_word(words)
    
    # Keep track of correct and incorrect guesses
    guessed_letters = set()
    incorrect_guesses = set()

    while attempts > 0:
        # Display the current state of the word being guessed and the number of attempts left
        display = "".join(
            letter if letter in guessed_letters else "_"
            for letter in chosen_word)

        display = " ".join(display)
        print("\nWord:", display)
        print("\033[31mAttempts left:\033[0m", attempts)

        # Ask the user to guess a letter
        while True:
            print("\033[33mHint: Each word is a type of fruit\033[0m.")
            guess = input("\nGuess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("\n\033[31mError: Please enter only 1 letter and only a letter\033[0m")

        # Check if the guessed letter is already guessed
        if guess in guessed_letters or guess in incorrect_guesses:
            print("\033[31mYou already guessed that letter!\033[0m")
        elif guess in chosen_word:
            print("\n\033[32mCorrect guess!\033[0m")

            # Add the guessed letter to the set of guessed letters
            guessed_letters.add(guess)

            # Check if all letters of the word have been guessed
            if set(guessed_letters) == set(chosen_word):
                print(
                    "\n\033[32mCongratulations! You guessed the word correctly. "
                    f"The word was: {chosen_word}\033[0m\n")

                guessed_words.append(chosen_word)
                return True  # Return True to indicate the game ends

        else:
            # If the guess was incorrect, add it to the set of incorrect guesses
            print("\n\033[31mIncorrect guess!\033[0m")
            incorrect_guesses.add(guess)
            attempts -= 1

    print(
        "\n\033[31mSorry, you have run out of attempts. "
        f"The word was: {chosen_word}\033[0m\n")

    return True  # Return True to indicate the game ends

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

    while True:
        # Let the player choose the difficulty level
        difficulty = input(
            "\033[32mChoose difficulty level:\n"
            "\n\033[92m1. Easy (8 attempts)\033[0m\n"
            "\033[33m2. Hard (6 attempts)\033[0m\n"
            "\033[31m3. Extreme (4 attempts)\033[0m\n"
            "\nType '1', '2', or '3': \033[0m"
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

    while True:
        # Randomly select 6 words from the words list for this game
        selected_words = random.sample(words, 6)

        # Loop through each selected word to play the game
        for _ in range(6):
            if not play_game(selected_words, attempts):
                break

        # Calculate the score by counting the guessed words
        score = len(guessed_words)
        print(f"\n\033[33mYou guessed {score} /6 words correctly.\033[0m")

        # Check if all words have been guessed or prompt for replay
        if score == 6:
            print("\n\033[33mYou've guessed all the words! Game over.\033[0m")
            break

        # Prompt the user if they want to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again != 'y':
            print("\033[33mThanks for playing. We hope to see you again soon!\033[0m")
            break

        # Reset the 'guessed_words' list for a new game
        guessed_words.clear()


if __name__ == "__main__":
    main()