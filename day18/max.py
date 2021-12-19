with open("day18/results", 'r') as f:
    nums = [int(line) for line in f.readlines()]

print(max(nums))