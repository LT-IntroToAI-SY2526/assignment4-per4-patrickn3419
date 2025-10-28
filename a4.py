# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        """Initialize the board with 9 empty spots, marked by asterisks"""
        self.board = ["*"] * 9

    def __str__(self) -> str:
        """Returns string representation of the grid in 3x3 form"""
        rows = [
            " ".join(self.board[0:3]),
            " ".join(self.board[3:6]),
            " ".join(self.board[6:9]),
        ]
        return "\n".join(rows)

    def make_move(self, player: str, position: int) -> bool:
        """Attempt to make a move for player ('X' or 'O') at given position (0–8).

        Returns:
                True if move was successful, False if invalid or spot already taken.
        """
        if position < 0 or position > 8:
            return False
        if self.board[position] != "*":
            return False
        self.board[position] = player
        return True

    def has_won(self, player: str) -> bool:
        """Check if given player has a winning combination."""
        wins = [
            [0, 1, 2],  # rows
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],  # columns
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],  # diagonals
            [2, 4, 6],
        ]
        # check to see if all of any of win positions conatain a player
        return any(all(self.board[i] == player for i in combo) for combo in wins) 

    def game_over(self) -> bool:
        """Return True if the game is over (win or full board)."""
        return self.has_won("X") or self.has_won("O") or "*" not in self.board

    def clear(self) -> None:
        """Reset the board to its initial empty state."""
        self.board = ["*"] * 9


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()
