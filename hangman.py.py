import random
import hangman_words
import hangman_art

# Use the word list from hangman_words.py
word_list = hangman_words.word_list
lives = 6

# Display the Hangman intro art
print(hangman_art.hangman_intro)

# Ask the user if they want instructions
show_instructions = input("Do you want to see the instructions on how to play the game? (yes/no): ").lower()
if show_instructions == "yes":
    print("\nHow to play Hangman:")
    print("1. A random word will be chosen, and you'll see its length as blanks (_).")
    print("2. Guess one letter at a time to fill in the blanks.")
    print("3. If the letter is correct, it will appear in the word.")
    print("4. If the letter is wrong, you lose a life.")
    print("5. You have 6 lives. Try to guess the word before you run out of lives!")
    print("6. You win if you complete the word. Good luck!\n")

# Randomly choose a word
chosen_word = random.choice(word_list)
#print(chosen_word)

# Initialize placeholders and state
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
already_guess = []

while not game_over:

    print(f"************************** {lives}/6 LIVES LEFT **************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in already_guess:
        print(f"You have already guessed the letter: {guess}")
        print(hangman_art.stages[lives])
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        if guess not in already_guess:
            already_guess.append(guess)
            lives -= 1
            
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"************************** IT WAS {chosen_word}. YOU LOSE **************************")

    already_guess.append(guess)
    if "_" not in display:
        game_over = True
        print("************************** YOU WIN **************************")

    # Show the hangman stage
    print(hangman_art.stages[lives])

# Ask the user to press Enter to exit
input("\nPress Enter to exit.")
