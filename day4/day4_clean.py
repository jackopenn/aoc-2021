with open("day4/input.txt", 'r') as f:
    lines = [line.rstrip().split() for line in f.readlines()]

values = lines[0][0].split(',')
boards = [lines[idx:idx+6][1:] for idx in range(1, len(lines), 6)]


def check_board(board):
    for row in board:
        if row.count('X') == len(board):
            return True
    for col in zip(*board):
        if col.count('X') == len(board):
            return True
    return False


bingo_boards = []

for v in values:
    for idx, board in enumerate(boards):
        if board not in [board for _,board in bingo_boards]:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == v:
                        board[i][j] = 'X'
        
            if check_board(board):
                bingo_boards.append((v, board))


def calc_score(board):
    return sum([int(elem) for row in board for elem in row if elem != 'X'])

print(bingo_boards[0][0], calc_score(bingo_boards[0][1]), int(bingo_boards[0][0]) * calc_score(bingo_boards[0][1]))
print(bingo_boards[-1][0], calc_score(bingo_boards[-1][1]), int(bingo_boards[-1][0]) * calc_score(bingo_boards[-1][1]))