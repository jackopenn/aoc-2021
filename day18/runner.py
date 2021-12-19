from itertools import permutations
import itertools

import time

with open("day18/input_test", 'r') as f:
    nums = [eval(line) for line in f.readlines()]


with open("day18/input_test", 'w') as f:
    for a, b in itertools.permutations(nums, 2):
        f.write(str(a))
        f.write('\n')
        f.write(str(b))
        f.write('\n')

time.sleep(5)
for i in range(9900):
    print(i)
    exec(open('day18/day18copy.py').read())
    # time.sleep(0.02)