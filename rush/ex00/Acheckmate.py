#!/bin/python3

def checkmate(board):
    # Split the board into rows (each row is a string)
    rows = board.splitlines()

    # Find the position of the King
    def find_king(rows):
        """Find the position of the King on the board."""
        for y in range(len(rows)):  # Iterate over rows
            if 'K' in rows[y]:
                return (rows[y].index('K'), y)  # Return column (x), row (y)
        return None

    # Check if a piece can capture the King
    def can_capture(piece, x, y, king_x, king_y, board):
        """Check if a piece at (x, y) can capture the King."""
        if piece == 'P':  # Pawn
            return can_pawn_capture(x, y, king_x, king_y, board)
        elif piece == 'B':  # Bishop
            return can_bishop_capture(x, y, king_x, king_y, board)
        elif piece == 'R':  # Rook
            return can_rook_capture(x, y, king_x, king_y, board)
        elif piece == 'Q':  # Queen
            return can_bishop_capture(x, y, king_x, king_y, board) or can_rook_capture(x, y, king_x, king_y, board)
        return False

    # Check if a Pawn can capture the King
    def can_pawn_capture(x, y, king_x, king_y, board):
        """Check if a Pawn can capture the King."""
        if y > 0:  # Pawn moves diagonally upward (negative y direction)
            if (x > 0 and board[y-1][x-1] == 'K') or (x < len(board[y]) - 1 and board[y-1][x+1] == 'K'):
                return True
        return False

    # Check if a Bishop can capture the King
    def can_bishop_capture(x, y, king_x, king_y, board):
        """Check if a Bishop can capture the King."""
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= ny < len(board) and 0 <= nx < len(board[ny]):
                nx += dx
                ny += dy
                if 0 <= ny < len(board) and 0 <= nx < len(board[ny]):
                    if (nx, ny) == (king_x, king_y):
                        return True
                    if board[ny][nx] != '.':  # Blocked by another piece
                        break
        return False

    # Check if a Rook can capture the King
    def can_rook_capture(x, y, king_x, king_y, board):
        """Check if a Rook can capture the King."""
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Horizontal and vertical directions
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= ny < len(board) and 0 <= nx < len(board[ny]):
                nx += dx
                ny += dy
                if 0 <= ny < len(board) and 0 <= nx < len(board[ny]):
                    if (nx, ny) == (king_x, king_y):
                        return True
                    if board[ny][nx] != '.':  # Blocked by another piece
                        break
        return False

    # Find the King's position
    king_pos = find_king(rows)
    
    # If the King is not found, print "Fail"
    if not king_pos:
        print("Fail")
        return

    king_x, king_y = king_pos

    # Check each piece on the board to see if it can capture the King
    for y in range(len(rows)):  # Iterate over rows
        for x in range(len(rows[y])):  # Iterate over columns
            piece = rows[y][x]
            if piece != "." and can_capture(piece, x, y, king_x, king_y, rows):
                print("Success")
                return

    print("Fail")
    # Split the board into rows (each row is a string)
    rows = board.splitlines()

    # Find the position of the King
    def find_king(rows):
        """Find the position of the King on the board."""
        for i in range(len(rows)):
            if 'K' in rows[i]:
                return (i, rows[i].index('K'))
        return None

    # Check if a piece can capture the King
    def can_capture(piece, x, y, king_x, king_y, board):
        """Check if a piece at (x, y) can capture the King."""
        if piece == 'P':  # Pawn
            return can_pawn_capture(x, y, king_x, king_y, board)
        elif piece == 'B':  # Bishop
            return can_bishop_capture(x, y, king_x, king_y, board)
        elif piece == 'R':  # Rook
            return can_rook_capture(x, y, king_x, king_y, board)
        elif piece == 'Q':  # Queen
            return can_bishop_capture(x, y, king_x, king_y, board) or can_rook_capture(x, y, king_x, king_y, board)
        return False

    # Check if a Pawn can capture the King
    def can_pawn_capture(x, y, king_x, king_y, board):
        """Check if a Pawn can capture the King."""
        if x > 0:
            if (y > 0 and board[x-1][y-1] == 'K') or (y < len(board[x]) - 1 and board[x-1][y+1] == 'K'):
                return True
        return False

    # Check if a Bishop can capture the King
    def can_bishop_capture(x, y, king_x, king_y, board):
        """Check if a Bishop can capture the King."""
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
                nx += dx
                ny += dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
                    if (nx, ny) == (king_x, king_y):
                        return True
                    if board[nx][ny] != '.':
                        break
        return False

    # Check if a Rook can capture the King
    def can_rook_capture(x, y, king_x, king_y, board):
        """Check if a Rook can capture the King."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
                nx += dx
                ny += dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
                    if (nx, ny) == (king_x, king_y):
                        return True
                    if board[nx][ny] != '.':
                        break
        return False

    # Find the King's position
    king_pos = find_king(rows)
    
    # If the King is not found, print "Fail"
    if not king_pos:
        print("Fail")
        return

    king_x, king_y = king_pos

    # Check each piece on the board to see if it can capture the King
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            piece = rows[i][j]
            if piece != "." and can_capture(piece, i, j, king_x, king_y, rows):
                print("Success")
                return

    print("Fail")
