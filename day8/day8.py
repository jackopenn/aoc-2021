from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE

with open("day8/input", 'r') as f:
    lines = [list(map(lambda x: x.strip().split(), line.split('|'))) for line in f.readlines()]

# print(lines)

all = "abcdefg"
cnt= 0
nums = []
for l, r in lines:
    print(l, r)
    # poss = defaultdict(str)
    matches = defaultdict(set)
    while len(matches.keys()) != 10:
        for w in l:
            # w = 1,4,7,8
            if len(w) == 2:
                matches[1] = set(w)
            elif len(w) == 4:
                matches[4] = set(w)
            elif len(w) == 3:
                matches[7] = set(w)
            elif len(w) == 7:
                matches[8] = set(w)

            #w = 9,0,6
            elif len(w) == 6:
                if matches[4].issubset(set(w)):
                    matches[9] = set(w)
                elif matches[1].issubset(set(w)):
                    matches[0] = set(w)
                else:
                    matches[6] = set(w)
            
            else: #length = 5
                if matches[7].issubset(set(w)):
                    matches[3] = set(w)
                elif set(w).issubset(matches[9]):
                    matches[5] = set(w)
                else:
                    matches[2] = set(w)
        
        # #w = 2
        # elif len(w) == 5 and matches[8].difference(matches[9]) in set(w):
        #     matches[2] = set(w)
        

    
    # for k, v in matches.items():
    #     print(k, v)
    result = ""
    for w in r:
        for n, w_ in matches.items():
            if set(w) == w_:
                result += str(n)
    
    print(result)
    nums.append(int(result))

print(sum(nums))
    # print(r)
    # for w in r:
    #     print(w)
    #     match len(w):
    #         case 2:
    #             poss[1] = w
    #         case 4:
    #             poss[4] = w
    #         case 3:
    #             poss[7] = w
    #         case 7:
    #             poss[8] = w

        
    # for w in l:
    #     # w = 1,4,7,8
    #     if len(w) == 2:
    #         matches[w] = 1
    #     elif len(w) == 4:
    #         matches[2] = 4
    #     elif len(w) == 3:
    #         matches[w] = 7
    #     elif len(w) == 7:
    #         matches[w] = 8
    #     #w = 9
    #     elif len(w) == 6 and set(set(poss[4])).issubset(w):
    #         matches[w] == 9
        
        

        

            
        # if len(w) in {7,4,3,2}:
        #     cnt += 1
    
#     print(poss)
#     print(matches)


# print(cnt)