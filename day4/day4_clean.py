with open("day4/input.txt", 'r') as f:
    lines = [line.rstrip().split() for line in f.readlines()]

values = map(int, lines[0][0].split(','))
boards = [[[int(elem) for elem in row] for row in board] for board in [lines[idx:idx+6][1:] for idx in range(1, len(lines), 6)]]

bingo_boards = []

for v in values:
    for board in boards:
        if board not in [board for _,board in bingo_boards]:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == v:
                        board[i][j] = -1

            if (any([True for row in board if sum(row) == -5]) 
                or any([True for col in zip(*board) if sum(col) == -5])):
                bingo_boards.append((v, board))


def calc_score(board):
    return sum([elem for row in board for elem in row if elem != -1])

print(bingo_boards[0][0], calc_score(bingo_boards[0][1]), int(bingo_boards[0][0]) * calc_score(bingo_boards[0][1]))
print(bingo_boards[-1][0], calc_score(bingo_boards[-1][1]), int(bingo_boards[-1][0]) * calc_score(bingo_boards[-1][1]))