import numpy as np

with open("day19/input_test", 'r') as f:
    nums = [ np.array([np.array(list(map(int, coord.split(',')))) for coord in scanner.split('\n')[1:] ]) for scanner in f.read().split('\n\n')]

# for num in nums:
#     for coord in num:
#         print(coord)
#     print()

# print(type(nums))

