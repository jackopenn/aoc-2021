
p1_pos = 5
p2_pos = 8

board = list(range(1,11))

dice = list(range(1, 101))

p1_score, p2_score = 0, 0

def slice_(l, s, e):
    s = s % (len(l))
    e = e % (len(l))
    if e>=s:
        return l[s:e]
    else:
        return l[s:]+l[:e]

idx = 0

def new_pos(old_pos, roll):
    v = (old_pos + roll) % len(board)
    return v if v != 0 else len(board)

# for i in range(5):
while True:

    p1_roll = sum(slice_(dice, idx, idx+3))
    p1_pos = new_pos(p1_pos, p1_roll)
    p1_score += p1_pos
    print(p1_roll, p1_pos, p1_score)
    idx+= 3

    if p1_score >= 1000:
        break


    p2_roll = sum(slice_(dice, idx, idx+3))
    p2_pos = new_pos(p2_pos, p2_roll)
    p2_score += p2_pos
    idx += 3

    if p2_score >= 1000:
        break

    print(p2_roll, p2_pos, p2_score)
    print()

print(p1_score, p2_score)
print(idx)
print(min(p1_score, p2_score) * idx)
