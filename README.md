
# Hangman Game 🎮

This is a console-based Hangman game built in Python. The game randomly selects a word, and the player guesses letters one at a time to complete the word. The player has 6 lives, and each incorrect guess reduces a life. The game ends when the player either completes the word or loses all their lives.

---

## Features
- Interactive console-based gameplay.
- A word list with a variety of words.
- ASCII art for the hangman and game introduction.
- Tracks guessed letters and prevents repeated guesses.

---

## Files in the Project
1. **`hangman.py`**: The main file that contains the game logic.
2. **`hangman_art.py`**: Contains ASCII art for the hangman stages and the game introduction.
3. **`hangman_words.py`**: Contains a list of words for the game.

---

## How to Play
1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the game using the following command:
   ```bash
   python hangman.py
   ```
4. Follow the instructions in the console to guess letters.

---

## Game Rules
- A random word is chosen at the start.
- The player has 6 lives to guess the word.
- Each incorrect guess reduces a life.
- The player wins if they guess the entire word correctly before running out of lives.

---

## Example
```
Word to guess: _ _ _ _ _
Guess a letter: a
Word to guess: a _ _ _ _
************************** 5/6 LIVES LEFT **************************
Guess a letter: b
You guessed b, that's not in the word. You lose a life.
```

---

## Installation
Ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

---

## Contribution
Feel free to fork this repository and submit a pull request if you'd like to contribute or improve the project.

---

## License
This project is open-source and available under the MIT License.

---

Happy Gaming! 🎉
