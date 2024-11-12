def solution(board):
    rows = len(board)
    cols = len(board[0])
    max_side = 0  
    
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_side = max(max_side, board[i][j])
    
    if max_side == 0:
        max_side = max(max(row) for row in board)
    
    return max_side * max_side  
