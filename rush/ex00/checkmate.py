#!/bin/python3

def checkmate(board):
    rows = board.split("\n")
    board_matrix = [list(row.strip()) for row in rows]

    def find_king(board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'K':
                    return row, col
        return None 

    def check_queen_or_rook(board, king_position):
        king_row, king_col = king_position  

        # right
        for col in range(king_col + 1, len(board[king_row])):
            if board[king_row][col] in ('R', 'Q'):
                return True
            if board[king_row][col] != '.':
                break

        # left
        for col in range(king_col - 1, -1, -1):
            if board[king_row][col] in ('R', 'Q'):
                return True
            if board[king_row][col] != '.':
                break

        # down
        for row in range(king_row + 1, len(board)):
            if board[row][king_col] in ('R', 'Q'):
                return True
            if board[row][king_col] != '.':
                break

        # up
        for row in range(king_row - 1, -1, -1):
            if board[row][king_col] in ('R', 'Q'):
                return True
            if board[row][king_col] != '.':
                break

        return False

    def check_bishop_or_queen(board, king_position):
        king_row, king_col = king_position

        for i in range(1, len(board)):
            # up right
            if king_row - i >= 0 and king_col + i < len(board[king_row]):
                if board[king_row - i][king_col + i] in ('B', 'Q'):
                    return True
                if board[king_row - i][king_col + i] != '.':
                    break

            # down left
            if king_row + i < len(board) and king_col - i >= 0:
                if board[king_row + i][king_col - i] in ('B', 'Q'):
                    return True
                if board[king_row + i][king_col - i] != '.':
                    break

            # down right
            if king_row + i < len(board) and king_col + i < len(board[king_row]):
                if board[king_row + i][king_col + i] in ('B', 'Q'):
                    return True
                if board[king_row + i][king_col + i] != '.':
                    break

            # up left
            if king_row - i >= 0 and king_col - i >= 0:
                if board[king_row - i][king_col - i] in ('B', 'Q'):
                    return True
                if board[king_row - i][king_col - i] != '.':
                    break

        return False

    def check_pawn(board, king_position):
        king_row, king_col = king_position

        if king_row + 1 < len(board):
            if king_col - 1 >= 0 and board[king_row + 1][king_col - 1] == 'P':
                return True
            if king_col + 1 < len(board[king_row]) and board[king_row + 1][king_col + 1] == 'P':
                return True
        return False

    king_position = find_king(board_matrix)

    if king_position is None:
        print("Not found")
        return

    if (check_queen_or_rook(board_matrix, king_position) or
        check_bishop_or_queen(board_matrix, king_position) or
        check_pawn(board_matrix, king_position)):
        print("Success")
    else:
        print("Fail")