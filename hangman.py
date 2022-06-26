secret_word = "unicorn"

# Feedback: longer pauses, spend more time asking from students even if there's silence, slow down (it will take them more time)
# Ask more questions about how to implement (so they think about it), "how do I do that?"
# Good job recognizing your own mistake, admitting it, and demonstrating why its wrong
# Maybe instead of directly implementing, let's break down the steps of hangman and come up with template

# Part 2 feedback
#


def hangman(secret_word):
    guess = input("Give me a letter! ")
    correct_letters = set()

    if guess in secret_word:  # letter is in the word
        correct_letters.discard(guess)
    else:
        lives -= 1


hangman("narwhal")
