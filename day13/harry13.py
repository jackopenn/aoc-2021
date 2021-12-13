
from functools import reduce
import sys
import numpy as np


def print_paper(array):
    print(np.where(array, "#", "."))


with open('day13/input', "r") as input_file:
    input = input_file.read()

dot_str, fold_str = input.split("\n\n")

dots = [tuple(map(int, dot_s.split(","))) for dot_s in dot_str.split("\n")]

folds = [
    (fold_s[11:].split("=")[0], int(fold_s[11:].split("=")[1]))
    for fold_s in fold_str.split("\n")
    if fold_s != ""
]

x_coordinates = list(map(lambda x: x[0], dots))
y_coordinates = list(map(lambda y: y[1], dots))
paper = np.zeros(shape=(max(y_coordinates) + 1, max(x_coordinates) + 1)).astype(bool)

paper[y_coordinates, x_coordinates] = True


def fold_paper(paper, fold):
    if fold[0] == "x":
        fold_col = fold[1]
        paper = paper[:, :fold_col] | np.fliplr(paper[:, fold_col + 1 :])
    else:
        fold_row = fold[1]
        paper = paper[:fold_row, :] | np.flipud(paper[fold_row + 1 :, :])
    return paper


paper = reduce(fold_paper, folds, paper)
print_paper(paper)