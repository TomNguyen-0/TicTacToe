"""
Generate all the possible wins for a tic tac toe game
Used by AI to determine a winning move

Date            Name            Description
05/22/2024      Tom Nguyen      initial create
"""
def check_row(sublist):
    total_1 = 0
    total_2 = 0
    for item in sublist:
        if item == 1:
            total_1 += item
        if item == 2:
            total_2 += item
    if total_2 == 6:
        return 2
    if total_1 == 3:
        return 1
    return False
    
def check_diagonal(board):
    total_2, total_1 = 0,0
    if board[0][0] == 2:
        total_2 += board[0][0]
    if board[1][1] == 2:
        total_2 += board[1][1]
    if board[2][2] == 2:
        total_2 += board[2][2]
    if board[0][0] == 1:
        total_1 += board[0][0]
    if board[1][1] == 1:
        total_1 += board[1][1]
    if board[2][2] == 1:
        total_1 += board[2][2]
    if total_1 == 3:
        return 1
    if total_2 == 6:
        return 2
    total_2, total_1 = 0,0
    if board[0][2] == 2:
        total_2 += board[0][2]
    if board[1][1] == 2:
        total_2 += board[1][1]
    if board[2][0] == 2:
        total_2 += board[2][0]
    if board[0][2] == 1:
        total_1 += board[0][2]
    if board[1][1] == 1:
        total_1 += board[1][1]
    if board[2][0] == 1:
        total_1 += board[2][0]
    if total_1 == 3:
        return 1
    if total_2 == 6:
        return 2
    return False
    
        
def check_vertical(board):
    for number in range(3):
        total_1, total_2 = 0,0
        for row in range(3):
            if board[row][number] == 2:
                total_2 += board[row][number]
            if board[row][number] == 1:
                total_1 += board[row][number]
        else:
            if total_2 == 6:
                return 2
            if total_1 == 3:
                return 1
    else:
        return False
        
            

def check_empty_spaces(board):
    for sublist in board:
        for item in sublist:
            if item == 0:
                return -1
    else:
        return 0

def is_solved(board):
    for sublist in board:
        if check_row(sublist):
            return check_row(sublist)
    if check_diagonal(board):
        return check_diagonal(board)
    if check_vertical(board):
        return check_vertical(board)
    return check_empty_spaces(board)
            
r"""
reference:
    [generate all possible tables]: https://stackoverflow.com/questions/61508393/generate-all-possible-board-positions-of-tic-tac-toe

"""
def generate_all_possible_wins(all_moves = False):
    boards = []
    temp_boards = []
    all_possible_wins = []
    import time
    for i in range(0 , 19683) : 
        c = i
        temp_boards = []
        for ii in range(0 , 9) : 
            temp_boards.append(c % 3)
            c = c // 3
        temp_boards= [temp_boards[0:3], temp_boards[3:6], temp_boards[6:9]]
        boards.append(temp_boards)
    if all_moves:
        return boards
    else:
        for board in boards:
            if is_solved(board) > 0:
                all_possible_wins.append(board)
                
    return all_possible_wins
 