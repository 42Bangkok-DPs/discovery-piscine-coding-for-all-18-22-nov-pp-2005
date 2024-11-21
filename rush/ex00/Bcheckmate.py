#!/bin/python3

def checkmate(board):
    # แปลง board เป็น matrix
    rows = board.split("\n")
    board_matrix = [list(row.strip()) for row in rows]
    

    # ฟังก์ชันหาตำแหน่งของ King
    def find_king(board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'K':
                    return row, col
        return None 
    
    # Queen  Rook
    def check_queen_or_check_rook(board, king_position):
        king_row, king_col = king_position  

        #ขวา
        for col in range(king_col + 1, len(board[king_row])):
            if board[king_row][col] in ('R', 'Q'): 
                return True
            if board[king_row][col] != '.':  
                break
        #ซ้าย
        for col in range(king_col - 1, -1, -1):  
            if board[king_row][col] in ('R', 'Q'):  
                return True
            if board[king_row][col] != '.': 
                break

        #ลง
        for row in range(king_row + 1, len(board)):
            if board[row][king_col] in ('R', 'Q'): 
                return True
            if board[row][king_col] != '.':  
                break
        #บน
        for row in range(king_row - 1, -1, -1):  
            if board[row][king_col] in ('R', 'Q'):  
                return True
            if board[row][king_col] != '.':  
                break

        return False  

    #  Bishop  Queen
    def check_bishop_or_check_queen(board, king_position):
        king_row, king_col = king_position 

        # ตรวจสอบแนวทแยง
        for i in range(1, len(board)):
            # ทแยงขวาบน
            if king_row - i >= 0 and king_col + i < len(board[king_row]):
                if board[king_row - i][king_col + i] in ('B', 'Q'):
                    return True
                if board[king_row - i][king_col + i] != '.':
                    break

            # ทแยงซ้ายล่าง
            if king_row + i < len(board) and king_col - i >= 0:
                if board[king_row + i][king_col - i] in ('B', 'Q'):
                    return True
                if board[king_row + i][king_col - i] != '.':
                    break

            # ทแยงขวาล่าง
            if king_row + i < len(board) and king_col + i < len(board[king_row]):
                if board[king_row + i][king_col + i] in ('B', 'Q'):
                    return True
                if board[king_row + i][king_col + i] != '.':
                    break
            # ทแยงซ้ายบน
            if king_row - i >= 0 and king_col - i >= 0:
                if board[king_row - i][king_col - i] in ('B', 'Q'):
                    return True
                if board[king_row - i][king_col - i] != '.':
                    break

        return False  

    #  Pawn
    def check_pawn(board, king_position):
        king_row, king_col = king_position  

        # ตรวจสอบตำแหน่งที่ Pawn สามารถโจมตีได้
        if king_row + 1 >= 0 :  # ตรวจสอบแถวข้างบน
            # ซ้าย
            if king_col - 1 >= 0 and board[king_row + 1][king_col - 1] == 'P':  
                return True
            # ขวา    
            if king_col + 1 < len(board[king_row]) and board[king_row + 1][king_col + 1] == 'P': 
                return True

        return False  
    
      # ตรวจสอบตำแหน่งของ King
    king_position = find_king(board_matrix)

    if king_position is None:
        print("Not found")
        return

    
     # ตรวจสอบว่า King อยู่ใน Check หรือไม่
    if (check_queen_or_check_rook(board_matrix, king_position) or
        check_bishop_or_check_queen(board_matrix, king_position) or
        check_pawn(board_matrix, king_position)):
        print("Success")
    else:
        print("Fail")