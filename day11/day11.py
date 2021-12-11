from os import error


with open("day11/input", 'r') as f:
    grid = [list(map(int, list(line.rstrip()))) for line in f.readlines()]

# print(nums)
# for num in grid:
#     print(num)


steps = 100

from itertools import product

def flash(i,j, flashed):

    flashed[i][j] = True
    # grid[i][j] = 0


    # this messed me up for like 1h , indexes wrap around obvs :(
    # neighbours = {
    #     (-1,-1),
    #     (-1, 0),
    #     (-1, 1),
    #     ( 0,-1),
    #     ( 0, 1),
    #     ( 1,-1),
    #     ( 1, 0),
    #     ( 1, 1)
    # }

    # for x, y in neighbours:
    #     try:
    #         # if not flashed[i+x][j+y]:
    #             grid[i+x][j+y] += 1
    #     except:
    #         pass

    
    def neighbours(cell):
        for c in product(*(range(n-1, n+2) for n in cell)):
            if c != cell and all(0 <= n < len(grid) for n in c):
                yield c
    
    for x,y in neighbours((i,j)):

        grid[x][y] += 1
    
    return flashed



# for r in grid:
#     print(r)

flashes_cnt = 0
# for s in range(steps):
s = 1
while True:
    # print(s)
    flashed = [[False for i in range(len(grid))] for j in range(len(grid[0])) ]
    stack = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = grid[i][j] + 1

            if grid[i][j] > 9:
                stack.add((i, j))

    # for r in grid:
    #     print(r)
    # print()
 
    while stack != set():

        x, y = stack.pop()

        flashed = flash(x, y, flashed)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9 and flashed[i][j] == False:
                    stack.add((i,j))

        # print(x,y, stack)
        # for r in grid:
        #     print(r)
        # print("")
        # for r in flashed:
        #     print(r)
        # print("")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if flashed[i][j]:
                grid[i][j] = 0

    # for r in grid:
    #     print(r)
    # print()

    flashes_cnt += sum([ x for r in flashed for x in r])

    if sum([ x for r in flashed for x in r]) == len(grid) * len(grid[0]):
        print("step: " + str(s))
        break
    # print(sum([1 for r in grid for x in r if x ==0]))
    s += 1
print(flashes_cnt)
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] >= 9 and not flashed[i][j]:

    #             flashed = flash(i,j,flashed)
                
    #         print(i,j)
    #         for r in grid:
    #             print(r)
    #         print("")
    #         for r in flashed:
    #             print(r)
    #         print("")

