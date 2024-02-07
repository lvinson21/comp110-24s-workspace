"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730404818"


location: int = int(input("Pick a secret boat location between 1 and 4: "))


# if location is greater than 4, print "Error! {location} too high!"
if location > 4:
    print(f"Error! {location} too high!") 
    exit()
if location < 1:
    print(f"Error! {location} too low!")
    exit()

guess: int = int(input("Guess a number between 1 and 4: "))

# if guess is greater than 4, print "Error! {guess} too high!"
if guess > 4:
    print(f"Error! {guess} too high!")
    exit()
if guess < 1:
    print(f"Error! {guess} too low!")
    exit()


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if guess == 1:
    if guess == location:
        print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    else:
        print(f"{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")

if guess == 2:
    if guess == location:
        print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
    else:
        print(f"{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}")
      
if guess == 3:
    if guess == location:
        print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
    else:
        print(f"{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}")

if guess == 4:
    if guess == location:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{RED_BOX}")
    else:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")
      
if guess == location:
    print("Correct! You hit the ship.")
if guess != location:
    print("Incorrect! You missed the ship.")