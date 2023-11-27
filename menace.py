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

    def check_symmetry(self, board):
        """
        Generally we have 7 symmetries of any board. These are symmetry by vertical axis, horizontal
        and diagonals. There are also 3 rotational symmetries. When we encounter a board, we want to
        find, which type of symmetry compared to the base version is it and store the formula for
        transforming the coordinates according to it.
        """

        symm_dict = {
            "rotation_90": [7, 4, 1, 8, 5, 2, 9, 6, 3],
            "rotation_180": [9, 8, 7, 6, 5, 4, 3, 2, 1],
            "rotation_270": [3, 6, 9, 2, 5, 8, 1, 4, 7],
            "vertical": [3, 2, 1, 6, 5, 4, 9, 8, 7],
            "horizontal": [7, 8, 9, 4, 5, 6, 1, 2, 3],
            "diagonal_main": [1, 4, 7, 2, 5, 8, 3, 6, 9],
            "diagonal_sub": [9, 6, 3, 8, 5, 2, 7, 4, 1]
        }

        # rotational

        # 90 deg
        new_board = ''.join([str(board[x-1]) for x in symm_dict["rotation_90"]])
        # here we check for a suitable turn
        # ________________________________
        # now we do the reverse
        new_board = ''.join([str(returned_board[x-1]) for x in symm_dict["rotation_270"]])

        # 180 deg
        new_board = ''.join([str(board[x - 1]) for x in symm_dict["rotation_180"]])
        # here we check for a suitable turn
        # ________________________________
        # now we do the reverse
        new_board = ''.join([str(returned_board[x - 1]) for x in symm_dict["rotation_180"]])

        # 270 deg
        new_board = ''.join([str(board[x - 1]) for x in symm_dict["rotation_270"]])
        # here we check for a suitable turn
        # ________________________________
        # now we do the reverse
        new_board = ''.join([str(returned_board[x - 1]) for x in symm_dict["rotation_90"]])


    def __str__(self):
        return f"There are {len(self._menace_system)} variants in the system"


if __name__ == "__main__":
    menace = Menace()
    menace.check_symmetry("XOOX_____")

    print(menace)
