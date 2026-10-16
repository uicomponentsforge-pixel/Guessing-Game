
import random

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 10.")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = input("Enter your guess (1-10): ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)

    if guess < 1 or guess > 10:
        print("Choose a number between 1 and 10!")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You won!")
        print("The secret number was:", secret_number)
        print("Attempts:", attempts)
        break
