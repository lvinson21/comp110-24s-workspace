"""Functional Battleship Excersize."""


__author__ = "730404818"
import random


def input_guess(num: int, word: str) -> int:
    """This function allows you to add in your guess as a user and sets parameters for each guess."""
    assert word == "row" or word == "column"
    good_guess: bool = True
    while good_guess:
        if word == "row":
            guess = int(input("Guess a row: "))
        else:
            guess = int(input("Guess a column: "))
        if guess > num or guess < 1:
            guess = int(input(f"The grid is only {num} by {num}. Try again: "))
        good_guess = False
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, users_guess: bool) -> None:
    """This function prints out the grid for if you hit or miss."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str
    row_counter: int = 1

    if users_guess:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX
    
    while row_counter <= grid_size:
        emoji_row: str = ''
        column_counter: int = 1
        if row_guess == row_counter:
            """Then go down the column on that row 1 by 1 and evaluate to see where to addd colored box."""
            while column_counter <= grid_size:
                if column_counter == column_guess:
                    emoji_row += result_box
                else:
                    emoji_row += BLUE_BOX
                column_counter += 1
        else:
            """While row guess does not equal counter then just add 4 blue boxes to that row."""
            while column_counter <= grid_size:
                emoji_row += BLUE_BOX
                column_counter += 1
        """Print out the row, add 1 to the row counter, then restart until all 4 rows are complete."""
        print(emoji_row)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Tells you if you guessed correctly or not."""
    return secret_row == row_guess and secret_column == column_guess


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Implements all other function to allow your game to run."""
    num_turns: int = 5
    turn_counter: int = 1
    game_won: bool = False

    while turn_counter <= num_turns and not game_won:
        print(f"=== Turn {turn_counter}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        users_guess = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, users_guess)

        if users_guess:
            game_won = True
            print("Hit!")
            print(f"You won in {turn_counter}/5 turns!")
            turn_counter = 6
        else:
            print("Miss!")
        turn_counter += 1
    if turn_counter > num_turns and not game_won:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))