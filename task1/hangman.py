#Hangman Game
import random

# List of predefined words
WORDS = ["python", "keyboard", "hangman", "science", "library"]

# Hangman stages (7 stages: 0 wrong to 6 wrong)
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------""",
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------""",
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------""",
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------""",
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------""",
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------""",
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------"""
]

MAX_WRONG = 6


def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    print("=" * 40)
    print("       WELCOME TO HANGMAN!")
    print("=" * 40)

    # Pick a random word
    secret_word = random.choice(WORDS)

    guessed_letters = []
    wrong_guesses = 0
    game_over = False

    print(f"\nI'm thinking of a word with {len(secret_word)} letters.")
    print("You have 6 incorrect guesses before the hangman is complete!\n")

    # Main game loop
    while not game_over:
        # Show hangman stage
        print(HANGMAN_STAGES[wrong_guesses])

        # Show current word state
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        if guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")

        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")

            # Check win condition
            if all(letter in guessed_letters for letter in secret_word):
                print(HANGMAN_STAGES[wrong_guesses])
                print(f"\nWord: {display_word(secret_word, guessed_letters)}")
                print("\n*** Congratulations! You guessed the word:", secret_word.upper(), "***")
                game_over = True
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

            # Check loss condition
            if wrong_guesses >= MAX_WRONG:
                print(HANGMAN_STAGES[wrong_guesses])
                print(f"\n*** Game Over! The word was: {secret_word.upper()} ***")
                game_over = True

    # Ask to play again
    print("\n" + "=" * 40)
    play_again = input("Play again? (yes/no): ").lower().strip()
    if play_again in ["yes", "y"]:
        play_hangman()
    else:
        print("\nThanks for playing Hangman! Goodbye!")


# Entry point
if __name__ == "__main__":
    play_hangman()
