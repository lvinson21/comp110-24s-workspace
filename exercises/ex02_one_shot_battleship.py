"""One Shot Battleship EX02"""

__author__="730404818"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_guess: int = int(input("Guess a row: "))

while row_guess > grid_size or row_guess < 1:
    """makes sure guess is in grid size"""
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess: int = int(input("Guess a column: "))
while column_guess > grid_size or column_guess < 1:
    """makes sure guess is in grid size"""
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


result_box: str


if secret_column == column_guess and secret_row == row_guess:
    """Changes the color of the box to red or white depending on guess"""
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

row_counter: int = 1

while row_counter <= grid_size:
    emoji_row: str = ''
    column_counter: int=1
    if row_guess == row_counter:
        """Then go down the column on that row 1 by 1 and evaluate to see where to addd colored box"""
        while column_counter <= grid_size:
            if column_counter == column_guess:
                """adds a colored box wherever your guess=counter"""
                emoji_row = emoji_row + result_box
            else:
                """Adds generic blue box when guess does not = counter"""
                emoji_row = emoji_row + BLUE_BOX
            column_counter += 1
    else:
        """while row guess does not equal counter then just add 4 blue boxes to that row"""
        while column_counter <= grid_size:
            emoji_row = emoji_row + BLUE_BOX
            column_counter += 1
    """print out the row, add 1 to the row counter, then restart until all 4 rows are complete"""
    print(emoji_row)
    row_counter += 1


if row_guess == secret_row and column_guess == secret_column:
    print("Hit!")
else:
    print ("Miss!")


if row_guess == secret_row and column_guess != secret_column:
    print("Close! Correct row, wrong column.")
if column_guess == secret_column and row_guess != secret_row:
    print("Close! Correct column, wrong row.")








