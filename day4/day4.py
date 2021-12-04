with open("day4/input.txt", 'r') as f:
    nums = [line for line in f.readlines()]

# print(nums)

values = nums[0].rstrip().split(',')

boards = nums[2:]

# print(values)

boards = [boards[i:i+6][:-1] for i in range(0, len(boards), 6)]


clean_boards = []

for board in boards:
    clean_boards.append([row.rstrip().split() for row in board])

# print(clean_boards[0])

check_boards = [[[0] * 5] * 5] * len(boards)

# print(check_boards[0])

# for a in check_boards:
#     print(a)
#     print("")


def print_b(board):
    for row in board:
        print(row)
    print('')

# for b in boards:
#     print_b(b)

def check_board(board):
    for row in board:
        if row.count('X') == 5:
            return True
    for col in zip(*board):
        if col.count('X') == 5:
            return True
    return False

vs=[]
cboards=[]
for v in values:
    # print(v)
    for idx, board in enumerate(clean_boards):
        print("idx, board, v", idx, v)
        print_b(board)
        if board not in cboards:
            for i in range(5):
                for j in range(5):
                    # print("v,idx,i,j",v,idx,i,j)
                    # print_b(board)
                    if v == board[i][j]:
                        board[i][j] = 'X'
                        # break

            if check_board(board):
                print("bingo", v, idx)
                print_b(board)
                vs.append(v)
                cboards.append(board)
                # clean_boards.remove(board)
            


# print(v)
# print(board)

for a,b in zip(vs,cboards):
    print(a)
    print_b(b)

s = 0

for i in range(len(board)):
    for j in range(len(board)):
        if cboards[-1][i][j].isnumeric():
            s += int(cboards[-1][i][j])

v = vs[-1]
print(v, s, int(v)*s)