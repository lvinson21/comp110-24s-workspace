"""number guessing game"""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    if guess > SECRET:
        print(f"Your number is too high, guess again!")
    if guess < SECRET:
        print(f"Your number is too low, guess again")

