with open("day3/input.txt", 'r') as f:
    nums = [line.rstrip() for line in f.readlines()]

# print(nums)
# print(nums[0])
# print(int(nums[0], 2))


# outs = []

# for i in range(len(nums[0])):
#     out = []
#     one = zero = 0
#     for num in nums:
#         if num[i] == '1':
#             one +=1 
#         else:
#             zero+=1
    
#     if one > zero:
#         out.append('1')
#     else:
#         out.append('0')

#     print(out)
#     outs.append("".join(out))

#     print(outs)
#     print(int("".join(outs), 2))



def getCommon(nums, i, maxx):
    zero = one = 0
    for num in nums:
        if num[i] == '0':
            zero += 1
        else:
            one +=1
    # print(one, zero)
    # if one >= zero:
    #     return '1'
    # else:
    #     return '0'
    if maxx:
        if one >= zero:
            return '1'
        else:
            return '0'
    else:
        if one >= zero:
            return '0'
        else:
            return '1'



i = 0
while len(nums) > 1:
    com = getCommon(nums, i, True)
    if com == '1':
        nums_new = list(filter(lambda x: x[i] == com, nums))
    else:
        nums_new = list(filter(lambda x: x[i] == com, nums))

    # print(nums)
    # print(com)
    # print(i)
    # print(nums_new)
    # print("")

    # if len(nums_new) == len(nums):
    i +=1


    nums = nums_new

    # print(nums)

print(nums)


print(int("".join(nums), 2))

with open("day3/input.txt", 'r') as f:
    nums = [line.rstrip() for line in f.readlines()]



i = 0
while len(nums) > 1:
    com = getCommon(nums, i, False)

    if com == '1':
        nums_new = list(filter(lambda x: x[i] == com, nums))
    else:
        nums_new = list(filter(lambda x: x[i] == com, nums))


    # print(nums)
    # print(com)
    # print(i)
    # print(nums_new)
    # print("")

    # if len(nums_new) == len(nums):
    i +=1


    nums = nums_new

    # print(nums)

print(nums)

print(int("".join(nums), 2))