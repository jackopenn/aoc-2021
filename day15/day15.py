import numpy as np
import cProfile
with open("day15/input", 'r') as f:
    nums = [list(map(int, list(line.rstrip()))) for line in f.readlines()]

# for r in nums:
#     print(r)

# print(len(nums), len(nums[0]))
def shift(qwerty, d):
    for dd in range(d):
        qwerty = [[(i+1) if i < 9 else 1 for i in row]for row in qwerty]
    return qwerty



# dub_nums = np.hstack((np.array(nums), np.array(shift(nums)))).tolist()

new_nums = nums
for i in range(1,5):
    new_nums = np.hstack((np.array(new_nums), np.array(shift(nums, i)))).tolist()


# for r in np.array(shift(new_nums, 1)).tolist():
#     print(r)

# print()
new_nums2 = new_nums
for i in range(1,6):
    new_nums2 = new_nums2 + np.array(shift(new_nums, i)).tolist()

# for r in new_nums2:
#     print(r)



# # def neighbours(i, j):
# #     neighbours = set()
# #     rows = len(nums)
# #     cols = len(nums[0]) if rows else 0
# #     for x in range(max(0, i - 1), min(rows, i + 2)):
# #         for y in range(max(0, j - 1), min(cols, j + 2)):
# #             if (x, y) != (i, j):
# #                 neighbours.add((x,y))

# #     return neighbours

print("built grid")

def dijkstra(graph, source, target):
    def neighbours(i, j):
        neighbours = set()
        if i != 0:
            neighbours.add((i-1,j))
        if j != 0: #left
            neighbours.add((i,j-1))
        if i != len(graph) -1:
            neighbours.add((i+1,j))
        if j != len(graph[0]) -1:
            neighbours.add((i,j+1))
        
        return neighbours


    dist = dict()
    prev = dict()
    Q = set()

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            dist[(i,j)] = float('inf')
            prev[(i, j)] = None
            Q.add((i, j))

    dist[source] = 0


    while Q:

        # u = min(dist, key=dist.get)
        u = None
        for q in Q:
            if u == None:
                u = q
            elif dist[q] < dist[u]:
                u = q

        # print(u)
        Q.remove(u)
        
        if u == target:
            # print(dist)
            # print(prev)
            s = []
            if prev[u] != None or u == source:
                while u:
                    s.append(u)
                    u = prev[u]
            return dist[target], s


        for v in neighbours(*u):
            # print(v)
            i,j = v
            if v in Q:
                alt = dist[u] + graph[i][j]
                if alt < dist[v]:

                    dist[v] = alt
                    prev[v] = u
    
    return dist, prev


with cProfile.Profile() as pr:
    # print((len(nums)-1, len(nums[0])-1))
    dist, s = dijkstra(nums, (0,0), (len(nums)-1, len(nums[0])-1))

    print(dist)
    # s.reverse()
    # print(s)

pr.print_stats()


# # print((len(new_nums2)-1, len(new_nums2[0])-1))
# dist, s = dijkstra(new_nums2, (0,0), (len(new_nums2)-1, len(new_nums2[0])-1))

# print(dist)
# # s.reverse()
# # print(s)

# nums2 = new_nums2.copy()
# for i, j in s:
#     nums2[i][j] = 'X'
