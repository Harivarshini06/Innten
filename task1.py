import random

def hangman():
    # List of possible words
    word_list = ["python", "programming", "hangman", "challenge", "computer"]
    
    # Randomly choose a word
    word = random.choice(word_list)
    guessed_letters = set()
    correct_letters = set(word)
    tries = 6  # Maximum incorrect guesses allowed

    print("Welcome to Hangman!")
    print("_ " * len(word))  # Display blanks for letters

    while tries > 0 and correct_letters != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("Correct!")
        else:
            tries -= 1
            print(f"Wrong! You have {tries} tries left.")

        # Display current progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

    # Game result
    if correct_letters == guessed_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
