from collections import defaultdict

with open("day14/input_test", 'r') as f:
    input = f.read().split('\n\n')

poly = input[0].rstrip()
inserts = dict([tuple(pair.split(' -> ')) for pair in input[1].split('\n')])

counts = defaultdict(int)


# for pair in inserts.keys():

for a,b in zip(poly, poly[1:]):
    counts[a,b] += 1

print(counts)

steps = 40
for s in range(steps):
    print(s)

    new_counts = defaultdict(int)

    for a, b in counts.keys():
        print(a,b)
        m = inserts[a+b]
        print(m)
        print()
        new_counts[a, m] += counts[a, b]
        new_counts[m, b] += counts[a, b]
        new_counts[a,b] -= 0
    
    counts = new_counts
    print(counts)


counts_single = defaultdict(int)

for a, b in counts.keys():
    counts_single[a] += counts[a,b]
    counts_single[b] += counts[a,b]

from math import ceil

for a in counts_single.keys():
    counts_single[a] = ceil(counts_single[a] / 2)

print(counts_single)

print(max(counts_single.values()) - min(counts_single.values()))