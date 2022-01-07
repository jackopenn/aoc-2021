from collections import defaultdict

with open("day22/input_test", 'r') as f:
    steps = [line.rstrip() for line in f.readlines()]




grid = defaultdict(int)


for step in steps:
    print(step)
    step = step.split()
    mode=step[0]
    cords = step[1].split(',')
    x1, x2 = list(map(int, cords[0][2:].split('..')))
    y1, y2 = list(map(int, cords[1][2:].split('..')))
    z1, z2 = list(map(int, cords[2][2:].split('..')))


    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):

                if mode == 'on':
                    grid[(x,y,z)] = 1
                else:
                    grid[(x,y,z)] = 0


print(sum(grid.values()))
