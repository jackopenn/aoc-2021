with open("day9/input", 'r') as f:
    grid = [list(map(int,list(line.rstrip()))) for line in f.readlines()]

# print(nums)
# for r in grid:
#     print(r)


def get_low(i, j, min_=999999):
    options =[]
    #top
    if i != 0:
        options.append((i-1, j,grid[i-1][j]))
    if j != 0: #left
        options.append((i,j-1, grid[i][j-1]))
    if i != len(grid) -1:
        options.append((i+1,j, grid[i+1][j]))
    if j != len(grid[0]) -1:
        options.append((i,j+1, grid[i][j+1]))

    if options != []:
        choice = min(options, key=lambda x: x[2])

    if min_ <= choice[2]:
        # print(min_, i ,j)
        return min_, i, j
    else:
        return get_low(*choice)
        # print(choice)


mins = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # print(min_, i, j)
        mins.add(get_low(i, j))



# print(mins)
print(sum([x[0]+1 for x in mins]))



# def get_basin_size(i,j, size=0):

#     print(i, j, size)
#     if grid[i][j] == 9:
#         return 1

#     if i != 0:
#         size += get_basin_size(i-1,j)
#     if j != 0: #left
#         size += get_basin_size(i,j-1)
#     if i != len(grid) -1:
#         size += get_basin_size(i+1,j)
#     if j != len(grid[0]) -1:
#         size += get_basin_size(i,j+1)
    
#     return size+1



# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0) 
#     print (s, end = " ") 

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# bfs(visited, graph, 'A')


def get_neighbours(i, j):
    neighbours = set()
    if i != 0:
        neighbours.add((i-1,j))
    if j != 0: #left
        neighbours.add((i,j-1))
    if i != len(grid) -1:
        neighbours.add((i+1,j))
    if j != len(grid[0]) -1:
        neighbours.add((i,j+1))
    
    return neighbours

basin_sizes = []
for _, i, j in mins:

    visited = [(i,j)]
    queue = [(i,j)]
    size = 1

    while queue:
        x,y = queue.pop()

        for a,b in get_neighbours(x, y):
            if grid[a][b] != 9 and (a,b) not in visited:
                visited.append((a,b))
                queue.append((a,b))
                size += 1

    basin_sizes.append(size)


from functools import reduce

basin_sizes.sort(reverse=True)

print(reduce(lambda a,c: a*c , basin_sizes[:3]))


# top_3 = reduce()



