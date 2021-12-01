with open("day1/input.txt") as file:
    nums = [int(line) for line in file.readlines()]


nums = [sum(nums[i-2:i+1]) for i in range(2, len(nums))]

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

print(count)
