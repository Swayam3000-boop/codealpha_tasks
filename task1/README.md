# 🎯 Hangman Game (Python)

A simple text-based Hangman game built in Python where the player guesses a hidden word one letter at a time.

---

## 📋 Table of Contents

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Concepts Used](#concepts-used)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [License](#license)

---

## About

This is a beginner-friendly Python project that implements the classic Hangman game in the console. A random word is chosen from a predefined list, and the player must guess it one letter at a time before the hangman is fully drawn (6 incorrect guesses allowed).

---

## Demo

```
========================================
       WELCOME TO HANGMAN!
========================================

I'm thinking of a word with 6 letters.
You have 6 incorrect guesses before the hangman is complete!

       ------
       |    |
       |

Word: _ _ _ _ _ _
Wrong guesses left: 6

Enter a letter: p
Good guess! 'p' is in the word.

Word: p _ _ _ _ _
```

---

## Features

- 🎲 Random word selection from a predefined word list
- 💀 ASCII art hangman that builds with each wrong guess (7 stages)
- ✅ Input validation (single letters only, no repeats)
- 📋 Tracks and displays all guessed letters
- 🔁 Option to play again after each round

---

## Concepts Used

| Concept | Usage |
|--------|-------|
| `random` | Picks a random word using `random.choice()` |
| `while loop` | Keeps the game running until win or loss |
| `if-else` | Handles guess checking and win/loss conditions |
| `strings` | Processes the secret word and player input |
| `lists` | Stores the word bank and guessed letters |

---

## Requirements

- Python 3.x
- No external libraries needed — uses only the built-in `random` module

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/hangman-game.git
cd hangman-game
```

**2. Run the game:**
```bash
python hangman.py
```

> On some systems, use `python3` instead of `python`.

---

## How to Play

1. The game picks a secret word and shows blank spaces for each letter.
2. Enter one letter at a time as your guess.
3. A correct guess reveals the letter in the word.
4. An incorrect guess adds a body part to the hangman.
5. You win by guessing all letters before 6 wrong guesses.
6. You lose if the hangman is fully drawn (6 wrong guesses).

---

## Project Structure

```
hangman-game/
│
├── hangman.py     # Main game file
└── README.md      # Project documentation
```

---

## License

This project is open source and free to use for learning purposes.

---

*Built as a beginner Python project to practice core programming concepts.*
