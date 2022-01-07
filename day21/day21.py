from itertools import cycle, islice
p1_pos = 4
p2_pos = 8

board = cycle(range(1,11))

dice = cycle(range(1, 101))

# print(board)

# print(dice)

p1_score, p2_score = 0, 0

idx = 0
# while True:
for _ in range(3):

    p1_move = sum((islice(dice, idx, idx+3))) #this increments idx too??
    p1_pos += p1_move

    p1_score += next(islice(board, p1_pos-1, p1_pos))
    print(list(islice(board, p1_pos-1, p1_pos)))
    print(p1_move, p1_pos, p1_score)
    if p1_score >= 1000:
        break

    # idx += 3

    p2_move = sum((islice(dice, idx, idx+3)))
    p2_pos += p2_move
    p2_score += next(islice(board, p2_pos-1, p2_pos))
    print(p2_move, p2_pos, p2_score)

    if p2_score >= 1000:
        break

    print(p1_score, p2_score)
    print()


print(p1_score, p2_score)

