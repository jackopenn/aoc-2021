with open("day13/input", 'r') as f:
    input = f.read().split('\n\n')


dots = [tuple(map(int, pair.split(','))) for pair in input[0].split('\n')]
insts = [tuple(inst.split()[-1].split('=')) for inst in input[1].split('\n')]

# print(input)
# print(dots)
# print(inst)

max_x, max_y = max([x for x, _ in dots]), max([y for _, y in dots])

# print(max_x, max_y)

paper = [['#' if (i,j) in dots else '.' for i in range(max_x+1)] for j in range(895)]

# for r in paper:
#     print(r)


def fold(paper, axis, value):
    print(axis, value)

    def merge(top, bot):
        
        return [['#' if top[y][x] == '#' or bot[y][x] == '#' else '.'for x in range(len(top[0]))] for y in range(len(top))]

    value = int(value)

    if axis == 'x':
        paper = list(zip(*reversed(paper)))

        top = paper[:value]
        bot = paper[value+1:]
        print("yoo1", len(top), len(bot))
        bot.reverse()


        paper = merge(top, bot)

        paper = list(zip(*reversed(paper)))
        paper = list(zip(*reversed(paper)))
        paper = list(zip(*reversed(paper)))


    else:

        top = paper[:value]
        bot = paper[value+1:]
        bot.reverse()
        print("yoo2", len(top), len(bot))
        #prob somze way to do zip
        paper = merge(top, bot)



    # for r in top:
    #     print(r)
    # print()
    # for r in bot:
    #     print(r)
    # print()
    # for r in paper:
    #     print(r)
    
    return paper

# fold(paper, *inst[0])

for inst in insts:
    print(len(paper), len(paper[0]))
    paper = fold(paper, *inst)
    print()


for r in paper:
    print(r)
dot_cnt = sum([ 1 for row in paper for elem in row if elem == '#'])

print(dot_cnt)