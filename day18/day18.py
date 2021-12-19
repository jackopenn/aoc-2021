from dataclasses import dataclass
from typing import List, TypeVar
from collections import deque
import pprint
import random

pp = pprint.PrettyPrinter()



@dataclass(unsafe_hash=True)
class Number():
    left: List | int
    right: List | int




with open("day18/input_test", 'r') as f:
    nums = [eval(line) for line in f.readlines()]

# print(nums)

# for row in nums:
#     # print(type(row))
#     print(row)

def build_tree(nums):
    if isinstance(nums[0], int) and isinstance(nums[1], int):
        return Number(nums[0], nums[1])
    elif isinstance(nums[0], int) and isinstance(nums[1], List):
        return Number(nums[0], build_tree(nums[1]))
    elif isinstance(nums[0], List) and isinstance(nums[1], int):
        return Number(build_tree(nums[0]), nums[1])
    else:
        return Number(build_tree(nums[0]), build_tree(nums[1]))

def number_to_explode(number):
    def bfs_r(number, level=0):
        if level == 4:
            lvl_4.append(number)
        
        if isinstance(number.left, Number):
            bfs_r(number.left, level + 1)
        if isinstance(number.right, Number):
            bfs_r(number.right, level + 1)
        return
    
    lvl_4 = []
    bfs_r(number)

    if len(lvl_4) > 0:
        return lvl_4[0]
    else:
        return None

def reduce(number):

    def explode(number):
        return 1
    
    def split(number):
        return 1


tree = build_tree([[[[[9,8],1],2],3],4])

def explode(number, number_to_explode):
    preorder = []
    def preorder_search(number):

        preorder.append(number)
        if isinstance(number.left, Number):
            preorder_search(number.left)
        
        if isinstance(number.right, Number):
            preorder_search(number.right)

    preorder_search(number)
    return preorder
        


lvl_4_num = number_to_explode(tree)
print(lvl_4_num)

order = explode(tree, lvl_4_num)
print()
for o in order:
    print(o)