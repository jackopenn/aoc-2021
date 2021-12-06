from collections import defaultdict

with open("day6/input", 'r') as f:
    nums_ = [int(num) for num in f.readline().rstrip().split(',')]

print(nums_)

nums = defaultdict(int)
for num in nums_:
    nums[num] += 1


print(nums)
# for i in range(256):
#     print(i)
#     new_nums = []
#     for num in nums:
#         if num-1 == -1:
#             new_nums.append(6)
#             new_nums.append(8)
#         else:
#             new_nums.append(num-1)
            
#     nums = new_nums
#     # print(i, nums)

# print(len(nums))

for i in range (256):
    new_nums = defaultdict(int)
    for day, cnt in nums.items():
        # print("day, cnt", day, cnt)
        if day == 0:
            new_nums[6] += cnt
            new_nums[8] += cnt
        else:
            new_nums[day-1] += cnt
    
    print(i, new_nums)
    print("")
    
    nums = new_nums

print(sum(nums.values()))
