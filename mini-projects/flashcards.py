# Flashcard-style quiz for learning Python concepts

import random

# Dictionary of flashcards: term => definition
flashcards = {
    "print()": "Used to output text to the console",
    "len()": "Returns the number of items in a list or string",
    "if": "Conditional statement",
    "for": "Looping over an iterable",
    "def": "Defines a function"
}

# Shuffle the flashcard keys
keys = list(flashcards.keys())
random.shuffle(keys)

# Ask user each question
for term in keys:
    input(f"What does '{term}' do? Press Enter to see the answer...")
    print("Answer:", flashcards[term])
    print("-" * 40)
