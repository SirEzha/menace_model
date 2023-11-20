"""
We store the current number of 'gumdrops' as an array, where each element represents corresponding move, and the number
represents the amount of gumdrops of particular color.
"""

import random


class Menace:
    def __init__(self):
        self._menace_system = {}

    def play_game(self):
        board = "_________"
        history = []  # stores tuples of (board, move)
        while self.game_over(board) == -1:
            if board not in self._menace_system:
                self._menace_system[board] = [0] * 9
                for i, elem in enumerate(board):
                    if elem == "_":
                        self._menace_system[board][i] = 10

            possible_moves = []
            for i, elem in enumerate(self._menace_system[board]):
                if elem > 0:
                    for _ in range(elem):
                        possible_moves.append(i)

            move = random.choice(possible_moves)
            history.append((board, move))
            board = self.make_move(board, move)
        winner = self.game_over(board)
        self.update_menace(history, winner)

    def make_move(self, board, move):
        move_count = 0

        for elem in board:
            if elem == "_":
                move_count += 1

        if move_count % 2 == 1:
            board_new = board[:move] + "X" + board[move + 1:]
        else:
            board_new = board[:move] + "O" + board[move + 1:]

        return board_new

    def game_over(self, board):
        """
        :param board:
        :return: 0 = draw, 1 = crosses, 2 = circles
        """

        is_draw = True
        for elem in board:
            if elem == "_":
                is_draw = False
        if is_draw:
            return 0

        # check for horizontal win
        if (board[0] == board[1] == board[2] == "X" or
                board[3] == board[4] == board[5] == "X" or
                board[6] == board[7] == board[8] == "X"):
            return "X"

        if (board[0] == board[1] == board[2] == "O" or
                board[3] == board[4] == board[5] == "O" or
                board[6] == board[7] == board[8] == "O"):
            return "O"

        # check for vertical win
        if (board[0] == board[3] == board[6] == "X" or
                board[1] == board[4] == board[7] == "X" or
                board[2] == board[5] == board[8] == "X"):
            return "X"

        if (board[0] == board[3] == board[6] == "O" or
                board[1] == board[4] == board[7] == "O" or
                board[2] == board[5] == board[8] == "O"):
            return "O"

        # check for diagonal win
        if (board[0] == board[4] == board[8] == "X" or
                board[2] == board[4] == board[6] == "X"):
            return "X"

        if (board[0] == board[4] == board[8] == "O" or
                board[2] == board[4] == board[6] == "O"):
            return "O"

        return -1

    def update_menace(self, history, winner):
        for i, event in enumerate(history):
            if i % 2 == 0:
                if winner == "X":
                    self._menace_system[event[0]][event[1]] += 1
                if winner == "O":
                    self._menace_system[event[0]][event[1]] -= 1
            if i % 2 == 1:
                if winner == "X":
                    self._menace_system[event[0]][event[1]] -= 1
                if winner == "O":
                    self._menace_system[event[0]][event[1]] += 1

    def __str__(self):
        return f"There are {len(self._menace_system)} variants in the system"


if __name__ == "__main__":
    menace = Menace()
    for _ in range(1800):
        menace.play_game()

    print(menace)
