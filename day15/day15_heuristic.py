import numpy as np
import heapq
import cProfile

with open("day15/input", 'r') as f:
    nums = [list(map(int, list(line.rstrip()))) for line in f.readlines()]

def shift(qwerty, d):
    for dd in range(d):
        qwerty = [[(i+1) if i < 9 else 1 for i in row]for row in qwerty]
    return qwerty

nums_row = nums
for i in range(1,5):
    nums_row = np.hstack((np.array(nums_row), np.array(shift(nums, i)))).tolist()


nums_big = nums_row
for i in range(1,5):
    nums_big = nums_big + np.array(shift(nums_row, i)).tolist()


print("built grid")


def astar(graph, source, target):
    def heuristic(i, j, x, y):
        return abs(i - x) + abs(j - y)


    def neighbours(i, j):
        neighbours = set()
        if i != 0:
            neighbours.add((i-1,j))
        if j != 0:
            neighbours.add((i,j-1))
        if i != len(graph) -1:
            neighbours.add((i+1,j))
        if j != len(graph[0]) -1:
            neighbours.add((i,j+1))
        
        return neighbours


    dist = dict()
    prev = dict()
    Q = []


    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            v = (i,j)
            dist[v] = float('inf')
            prev[v] = None

    dist[source] = 0
    heapq.heappush(Q,(source, dist[source]))
    while Q:

        u, dist_u = heapq.heappop(Q)

        if u == target:
            s = []
            if prev[u] != None or u == source:
                while u:
                    s.append(u)
                    u = prev[u]
            return dist[target], s


        for v in neighbours(*u):

            i,j = v

            alt = dist[u] + graph[i][j]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (v, dist[v] + heuristic(i, j, len(graph)-1, len(graph[0])-1)))

    return dist, prev


with cProfile.Profile() as pr:
        
    dist, s = astar(nums, (0,0), (len(nums)-1, len(nums[0])-1))
    print(dist)

    dist, s = astar(nums_big, (0,0), (len(nums_big)-1, len(nums_big[0])-1))
    print(dist)

pr.print_stats()