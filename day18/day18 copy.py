from __future__ import annotations
from dataclasses import dataclass
from typing import List, TypeVar
from collections import deque
import pprint
import random
from math import floor, ceil
from functools import reduce
import sys

sys.setrecursionlimit(10000)

pp = pprint.PrettyPrinter()



@dataclass(unsafe_hash=True)
class Number():
    id: float = None
    value: int = None
    left: Number = None
    right: Number = None




with open("day18/input_test", 'r') as f:
    nums = [eval(line) for line in f.readlines()]

def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(' ' * 6 * level + '->', node.value)
        printTree(node.left, level + 1)

def input_2_tree(nums):
    if isinstance(nums[0], int) and isinstance(nums[1], int):
        return Number(
            left=Number(value=nums[0], id=random.random()),
            right=Number(value=nums[1], id=random.random()),
            id=random.random()
        )
    elif isinstance(nums[0], int) and isinstance(nums[1], List):
       return Number(
            left=Number(value=nums[0], id=random.random()),
            right=input_2_tree(nums[1]),
            id=random.random()
        )
    elif isinstance(nums[0], List) and isinstance(nums[1], int):
        return Number(
            left=input_2_tree(nums[0]),
            right=Number(value=nums[1], id=random.random())
        )
    else:
        return Number(
            left=input_2_tree(nums[0]),
            right=input_2_tree(nums[1])
        )

def tree_2_input(number):
    if number:
        if number.value:
            return number.value
        if number.left:
            return [tree_2_input(number.left), tree_2_input(number.right)]
        return 0
    

def get_leftmost_lvl_4(number):
    lvl_4 = []
    def bfs(number, level=0):

        if level == 4 and number.value == None:
            lvl_4.append(number)
        if number.left:
            bfs(number.left, level+1)
            bfs(number.right, level+1)
    bfs(number)
    if len(lvl_4) > 0:
        return lvl_4[0]
    else:
        return None

def number_gr_10(number):
    gr_10s = []
    def bfs(number):
        if number:
            if number.value:
                if number.value >= 10:
                    gr_10s.append(number)

            bfs(number.left)
            bfs(number.right)
    
    bfs(number)
    if len(gr_10s) > 0:
        return gr_10s[0]
    else:
        return None
        

def get_parent(number, to_explode):
    if number.left:
        if number.left == to_explode or number.right == to_explode:
            return number

        return get_parent(number.left, to_explode) or get_parent(number.right, to_explode)
    
    return None


def get_left_right(number, to_explode):
    left, right = None, None
    l = []
    def leafs(number):
        if not number:
            return 
        
        if not number.left and not number.right:
            l.append(number)
            return

        
        if number.left:
            leafs(number.left)
            leafs(number.right)
    
    leafs(number)

    if l.index(to_explode.left) != 0:
        left = l[l.index(to_explode.left) - 1]
    if l.index(to_explode.right) != len(l)-1:
        right = l[l.index(to_explode.right) + 1]
    return left, right

def explode(number, to_explode):
    left, right = get_left_right(number, to_explode)

    def traverse(tree):
        if tree:
            if right and tree == right:
                parent = get_parent(number, right)
                if parent.left and parent.left == right:
                    parent.left = Number(
                        id=tree.id,
                        value=tree.value + to_explode.right.value
                    )
                if parent.right and parent.right == right:
                    parent.right = Number(
                        id=tree.id,
                        value=tree.value + to_explode.right.value
                    )
            
            if left and tree == left:
                parent = get_parent(number, left)
                # parent.left = Number(
                #     id=tree.id,
                #     value=tree.value + to_explode.left.value
                # )
                if parent.left and parent.left == left:
                    parent.left = Number(
                        id=tree.id,
                        value=tree.value + to_explode.left.value
                    )
                if parent.right and parent.right == left:
                    parent.right = Number(
                        id=tree.id,
                        value=tree.value + to_explode.left.value
                    )
            if tree == to_explode:
                parent = get_parent(number, to_explode)
                if parent.left and parent.left == to_explode:
                    parent.left = Number(
                        id=to_explode.id,
                        value=0
                    )
                if parent.right and parent.right == to_explode:
                    parent.right = Number(
                        id=to_explode.id,
                        value=0
                    )


        if tree.left:
            traverse(tree.left)
            traverse(tree.right)
    

    traverse(number)

    return number
    
def split(number, to_split):
    def traverse(tree):
        if tree == to_split:
            parent = get_parent(number, to_split)
            if parent.left == to_split:
                parent.left = Number(
                    id=to_split.id,
                    left=Number(
                        id=random.random(),
                        value=floor(to_split.value / 2)
                    ),
                    right=Number(
                        id=random.random(),
                        value=ceil(to_split.value / 2)
                    )
                )
            if parent.right == to_split:
                parent.right = Number(
                    id=to_split.id,
                    left=Number(
                        id=random.random(),
                        value=floor(to_split.value / 2)
                    ),
                    right=Number(
                        id=random.random(),
                        value=ceil(to_split.value / 2)
                    )
                )
        if tree.left:
            traverse(tree.left)
            traverse(tree.right)
    
    traverse(number)
    return number

def reduce_(number):

    # printTree(number)
    # print("0-----------")
    new_number = number
    to_explode = get_leftmost_lvl_4(number)
    to_split = number_gr_10(number)
    # print(to_explode, to_split)
    changed = False
    if to_explode is not None:
        # print("EXPLODE")
        new_number = explode(number, to_explode)
        changed = True
    
    if to_split is not None and changed == False:
        # print("SPLIT")
        changed = True
        new_number = split(number, to_split)
    
    if changed:
        return reduce_(new_number)
    else:
        return new_number


def do_add(left, right):
    return reduce_(Number(
        id=random.random(),
        left=left,
        right=right
    ))



# tree = input_2_tree([[[[[9,8],1],2],3],4])
# tree_result = input_2_tree([[[[0,9],2],3],4])

# tree = input_2_tree([7,[6,[5,[4,[3,2]]]]])
# tree_result = input_2_tree([7,[6,[5,[7,0]]]])

# tree = input_2_tree([[6,[5,[4,[3,2]]]],1])
# tree_result = input_2_tree([[6,[5,[7,0]]],3])

# tree = input_2_tree([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
# tree_result = input_2_tree([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])

# tree = input_2_tree([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
# tree_result = input_2_tree([[3,[2,[8,0]]],[9,[5,[7,0]]]])


#SPLIT
# tree = input_2_tree([[[[0,7],4],[15,[0,13]]],[1,1]])
# tree_result = input_2_tree([[[[0,7],4],[[7,8],[0,13]]],[1,1]])

# tree = input_2_tree([[[[0,7],4],[[7,8],[0,13]]],[1,1]])
# tree_result = input_2_tree([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])

#ADD
# left = input_2_tree([[[[4,3],4],4],[7,[[8,4],9]]])
# right = input_2_tree([1,1])
# tree_result = input_2_tree([[[[0,7],4],[[7,8],[6,0]]],[8,1]])

# # pp.pprint(tree)
# printTree(tree)

# to_explode = get_leftmost_lvl_4(tree)
# print("to explode")
# print(to_explode)
# print("----")

# left, right = get_left_right(tree, to_explode)
# print(left)
# print(right)
# print("----")


# new_tree = explode(tree, to_explode)
# printTree(new_tree)
# print("---")
# # printTree(tree_result)


# print("-----")
# gr_10 = number_gr_10(tree)
# print(gr_10)
# print("----")
# # print(get_parent(tree, gr_10))
# new_tree = split(tree, gr_10)
# printTree(new_tree)
# print("---")
# # printTree(tree_result)


# printTree(left)
# print()
# printTree(right)
# print()
# print("ADD")
# printTree(add(left, right))
# print("-----")
# print("true")
# printTree(tree_result)
# import cProfile
# with open("day18/input_test", 'r') as f:
#     nums = [eval(line) for line in f.readlines()]

# for num in nums:
#     print(num)


# def my_reduce(func, seq):
#     first = seq[0]
#     for i in seq[1:]:
#         print(tree_2_input(first))
#         print(tree_2_input(i))
#         print()
#         first = func(first, i)
#     return first


# with cProfile.Profile() as pr:
#     result = my_reduce(do_add, list(map(input_2_tree, nums)))
#     print()
#     print(tree_2_input(result))

# pr.print_stats()


with open("day18/input_test", 'r') as f:
    nums = [eval(line) for line in f.readlines()]

    to_write = do_add(input_2_tree(nums[0]), input_2_tree(nums[1]))

with open("day18/input_test", 'w') as f:
    # f.write(str(tree_2_input(to_write)))
    # f.write('\n')

    for num in nums[2:]:
        f.write(str(num))
        f.write('\n')

def calc_mag(tree):
    if tree:
        if tree.value:
            return tree.value
        if tree.left:
            return 3 * calc_mag(tree.left) + 2 * calc_mag(tree.right)
    return 0

print(calc_mag(to_write))