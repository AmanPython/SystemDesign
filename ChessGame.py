class ChessGame:
    def __init__(self, helper, chessboard):
        """
        Initialize the chess game with a given helper object for printing and an initial chessboard setup.
        :param helper: Helper object with methods like print and println for output.
        :param chessboard: 2D list representing the initial state of the chessboard.
        """
        self.helper = helper
        self.chessboard = chessboard
        self.current_turn = 0  # 0 for white, 1 for black
        self.game_status = 0   # 0 for ongoing, 1 for white won, 2 for black won

    def move(self, startRow, startCol, endRow, endCol):
        """
        Attempt to move a piece from the start position to the end position.
        :param startRow: int, starting row of the piece.
        :param startCol: int, starting column of the piece.
        :param endRow: int, ending row of the piece.
        :param endCol: int, ending column of the piece.
        :return: str, "invalid" for invalid moves, "" for valid moves without capture, or piece code if captured.
        """
        # Implement movement logic here
        pass

    def getGameStatus(self):
        """
        Check the current status of the game.
        :return: int, 0 if ongoing, 1 if white won, 2 if black won.
        """
        return self.game_status

    def getNextTurn(self):
        """
        Determine whose turn is next.
        :return: int, 0 for white, 1 for black, -1 if the game has ended.
        """
        if self.game_status != 0:
            return -1
        return 1 - self.current_turn


class Helper:
    """
    Helper class for printing messages. This should be implemented as needed.
    """
    def print(self, message):
        print(message)

    def println(self, message):
        print(message)


def run_tests():
    """
    Function to run a series of tests on the ChessGame class.
    """
    helper = Helper()
    initial_board = [
        ["WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR"],
        ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
        ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]
    ]
    game = ChessGame(helper, initial_board)

    # Test moving a pawn from (1, 4) to (2, 4)
    print("Test 1:", game.move(1, 4, 2, 4))  # Expected: ''

    # Test moving a knight in an L shape
    print("Test 2:", game.move(0, 1, 2, 2))  # Expected: ''

    # Test capturing a piece
    print("Test 3:", game.move(6, 0, 4, 0))  # First move pawn
    game.current_turn = 0  # Switch turn to white manually for the test
    print("Test 4:", game.move(1, 0, 3, 0))  # Move pawn forward
    game.current_turn = 1  # Switch turn to black manually for the test
    print("Test 5:", game.move(4, 0, 3, 0))  # Capture white pawn, Expected: 'WP'

    # Test invalid move
    print("Test 6:", game.move(7, 7, 5, 5))  # Invalid rook move, Expected: 'invalid'

    # Test game status after a move
    print("Game Status:", game.getGameStatus())  # Expected: 0 (ongoing)
    print("Next Turn:", game.getNextTurn())      # Expected: 1 (black's turn)

if __name__ == "__main__":
    run_tests()
