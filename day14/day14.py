with open("day14/input", 'r') as f:
    input = f.read().split('\n\n')

poly = input[0].rstrip()
inserts = dict([tuple(pair.split(' -> ')) for pair in input[1].split('\n')])



# print(poly)

# print(inserts)
# to_insert = []
# for a,b in zip(poly, poly[1:]):
#     if (a+b) in inserts.keys():
#         to_insert.append(inserts[a+b])
#     else:
#         to_insert.append('-')

# print(poly)
# print(to_insert)



steps = 40
for s in range(steps):
    print(s)
    result=[]
    to_insert = []

    for a,b in zip(poly, poly[1:]):
        if (a+b) in inserts.keys():
            to_insert.append(inserts[a+b])
        else:
            to_insert.append('-')

    for idx in range(len(poly)):
        result.append(poly[idx])

        try:
            result.append(to_insert[idx])
        except:
            pass

    poly = result
    # print(result)


    from collections import Counter

    counter = Counter(result)

    print(counter)

print(max(counter.values()) - min(counter.values()))