with open("day7/input", 'r') as f:
    poss = [int(num) for num in f.readline().rstrip().split(',')]

print(poss)

min_, max_ = min(poss), max(poss)

min_fuel = 999999999999
for pos in range(min_, max_):
    # print(pos)
    # fuel = sum([abs(pos-p)for p in poss])
    sum_=0
    for p in poss:
        d = abs(pos-p)
        sum_ += d*(d+1)//2
    fuel = sum_
    min_fuel = min(fuel, min_fuel)

print(min_fuel)
