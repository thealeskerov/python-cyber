# Simple number guessing game

import random  # To generate a random number

# Generate a random number between 1 and 10
secret = random.randint(1, 10)

# Ask user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check if user guessed correctly
if guess == secret:
    print("🎉 You guessed it!")
else:
    print("❌ Wrong! The number was:", secret)
