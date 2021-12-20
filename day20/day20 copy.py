from collections import defaultdict
from itertools import product

with open("day20/input", 'r') as f:
    alg, input = f.read().split('\n\n')
    input = [list(row) for row in input.split('\n')]



def print_image(image):
    min_i = min(image.keys(), key=lambda x: x[0])[0]
    min_j = min(image.keys(), key=lambda x: x[1])[1]

    max_i = max(image.keys(), key=lambda x: x[0])[0]
    max_j = max(image.keys(), key=lambda x: x[1])[1]

    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            print(image[(i,j)], end='')
        print('\n', end='')
    print()

image = defaultdict(lambda: '.')

for i, r in enumerate(input):
    for j, e in enumerate(r):
        image[(i,j)] = e

# neighbours = set(product((-1,0,1), repeat=2))
# neighbours.remove((0,0))
neighbours = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

# print(neighbours)

def do(image, pad):
    
    image_copy = image.copy()
    new_image = defaultdict(lambda: pad)

    min_i = min(image.keys(), key=lambda x: x[0])[0]
    min_j = min(image.keys(), key=lambda x: x[1])[1]

    max_i = max(image.keys(), key=lambda x: x[0])[0]
    max_j = max(image.keys(), key=lambda x: x[1])[1]

    for i in range(min_i-1, max_i+2):
            for j in range(min_j-1, max_j+2):
                alg_index = [image_copy[(i+x,j+y)] for x, y in neighbours]
                alg_index_bianry =  int("".join([ ('1' if c == '#' else '0') for c in alg_index]), 2)
                new_image[(i, j)] = alg[alg_index_bianry]
                # print(i, j, alg_index, alg_index_bianry, alg[alg_index_bianry])

    
    # print_image(new_image)
    return new_image

steps=50
for s in range(steps):
    if alg[0] == '.':
        pad = '.'
    else:
        pad = '#' if s % 2 == 0 else '.'
    
    print(pad)
    
    image = do(image, pad)

# print(image)
count_lit = sum([1 for pixel in image.values() if pixel == '#'])
print(count_lit)