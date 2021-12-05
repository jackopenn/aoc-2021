from collections import defaultdict

with open("day5/input", 'r') as f:
    lines = [line.rstrip().split(' -> ') for line in f.readlines()]

# print(lines)

line_pairs = [ [tup.split(',') for tup in line] for line in lines ]

# print(line_pairs)
n=10

# grid = [[0] * n] * n
# grid[0][9] = 1
# for r in grid:
#     print(r)

grid = defaultdict(int) #sorry jawood

for start, end in line_pairs:
    x1,y1,x2,y2 = int(start[0]), int(start[1]), int(end[0]), int(end[1])
    # print(x1,y1,x2,y2)


    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2+1):
            grid[(x1, y)] += 1
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for x in range(x1, x2+1):
            grid[(x, y1)] += 1
    else:
        x11, x22 = min(x1, x2), max(x1, x2)
        y11, y22 = min(y1, y2), max(y1, y2)

        r = (x22 - x11) + 1

        if x1 < x2 and y1 < y2:
            for d in range(r):
                grid[(x11 + d, y11 + d)] += 1

        elif x1 > x2 and y1 < y2:
            for d in range(r):
                grid[(x22 - d, y11 + d)] += 1

        elif x1 < x2 and y1 > y2: #
            for d in range(r):
                grid[(x11 + d, y22 - d)] += 1
                
        else:
            for d in range(r):
                grid[(x22 - d, y22 - d)] += 1


    # if x1 == x2:
    #     for y in range(y1, y2+1):
    #         print("y")
    #         grid[x1][y] += 1
    # if y1 == y2:
    #     for x in range(x1, x2+1):
    #         print("x")
    #         print(x, y1)
    #         grid[y1][x] += 1
    #         break
    # for r in grid:
    #     print(r)
    # break

z = 0
for y in grid.values():
    if y > 1:
        z += 1

print(z)