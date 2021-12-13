with open("day13/input", 'r') as f:
    input = f.read().split('\n\n')


dots = [tuple(map(int, pair.split(','))) for pair in input[0].split('\n')]
insts = [tuple(inst.split()[-1].split('=')) for inst in input[1].split('\n')]

max_x, max_y = max([x for x, _ in dots]), max([y for _, y in dots])

# print(max_x, max_y)

paper = [['#' if (i,j) in dots else '.' for i in range(max_x+1)] for j in range(895)]


def fold(paper, axis, value):

    def merge(paper, value):

        new_paper = []
        i = 1
        while i != value + 1:
            # print(i)
            # print(paper[value-i])
            # print(paper[value+i])
            # print()
            new_paper.append(
                list(map(lambda x: '#' if x[0] == '#' or x[1] == '#' else '.',zip(paper[value-i], paper[value+i])))
                # list(zip(paper[value-i], paper[value+i]))
            )
            i += 1
    
        new_paper.reverse()
        return new_paper

    value = int(value)

    if axis == 'x':
        paper = list(zip(*reversed(paper)))

        paper = merge(paper, value)

        paper = list(zip(*reversed(paper)))
        paper = list(zip(*reversed(paper)))
        paper = list(zip(*reversed(paper)))

    else:
        paper = merge(paper, value)

    return paper

for inst in insts:
    print(len(paper), len(paper[0]))
    print(inst)
    paper = fold(paper, *inst)
    print()

for r in paper:
    print(r)