import random

# List of words
words = ["python","cloud","devops","linux"]

# Select random word
word = random.choice(words)

# Convert word into list
word_letters = list(word)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("=================================")
print("        HANGMAN GAME START        ")
print("=================================")

# Main game loop
while attempts > 0:

    # Display current progress
    display_word = ""

    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", guessed_letters)
    print("Attempts Left:", attempts)

    # Win condition (correct method)
    if all(letter in guessed_letters for letter in word_letters):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet letter")
        continue

    # Already guessed check
    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    guessed_letters.append(guess)

    # Correct / Wrong check
    if guess in word_letters:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# Lose condition
if attempts == 0:
    print("\nYou lost! The word was:", word)

print("\nGame Over")