with open("day10/input", 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

# for line in lines:
#     print(line)



pairs = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '<': '>',
    '>': '<'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def check_line(line):
    stack = []
    for c in line:
        # print(c, stack)
        if c in {'(', '{', '[', '<'}:
            stack.append(c)
        else:
            if stack[-1] == pairs[c]:
                stack.pop()
            else:
                return c
    
    return True


errors = []
clean = []
for line in lines:
    v = check_line(line)
    if v != True:
        errors.append(v)
    else:
        clean.append(line)

print(errors)
print(sum([points[error] for error in errors]))





def return_missing(line):
    stack = []
    for c in line:
        # print(c, stack)
        if c in {'(', '{', '[', '<'}:
            stack.append(c)
        else:
            if stack[-1] == pairs[c]:
                stack.pop()
        

    
    return [pairs[s] for s in stack]


points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for line in clean:
    missing = return_missing(line)
    missing.reverse()

    print(missing)
    score = 0
    for m in missing:
        score = (score * 5) + points2[m]
    scores.append(score)


print(scores)
scores.sort()

print(scores[len(scores)//2])

# print(check_line('[{[{({}]{}}([{[{{{}}([]'))