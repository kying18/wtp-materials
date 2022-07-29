import random


computer_number = random.randrange(1, 101)  # 1, 2, 3, ... 9, 10
guess = int(input("Choose a number between 1 and 100: "))

while computer_number != guess:
    if guess < computer_number-50:
        print("Guess a way larger number.")
    elif guess < computer_number:
        print("Guess a larger number")
    else:
        print("Guess a smaller number.")

    guess = int(input("Choose a number between 1 and 100: "))


print("Congrats! You guessed the number.")
