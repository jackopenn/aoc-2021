from collections import defaultdict

with open("day12/input", 'r') as f:
    edges = [tuple(line.rstrip().split('-')) for line in f.readlines()]

# print(edges)

graph = defaultdict(set)

for s, e in edges:
    graph[s].add(e)
    graph[e].add(s)

for k, v in graph.items():
    print(k, v)
print()


def is_lower(s): return s.lower() == s




# visitid= set()
# visited = defaultdict(int)
# paths =[]

# visitid2 = defaultdict(int)


def dfs(v, visited, choice, path):
    path.append(v)

    if v == 'end':
        paths.append(path)
        return
    
    if is_lower(v):
        visited[v] += 1


    for n in graph[v]:
        if n not in visited:
            dfs(n, visited.copy(), choice, path.copy())
        elif n == choice and visited[choice] < 2:
            dfs(n, visited.copy(), choice, path.copy())




all_paths = []
for choice in graph.keys():
    if is_lower(choice) and choice != 'start' and choice != 'end':
        paths = []
        visited = defaultdict(int)

        dfs('start', visited, choice, [])

        all_paths.append(paths)


all_paths = [path for paths in all_paths for path in paths]

# print(all_paths)
all_paths = set(tuple(i) for i in all_paths)
print(len(all_paths))