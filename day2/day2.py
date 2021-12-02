with open("day2/input.txt", 'r') as f:
    nums = [line.split() for line in f.readlines()]

def upatePos(dir,v, x, y, aim):
    if dir == "forward":
        return x+v, y+(aim*v), aim
    elif dir == "down":
        return x, y, aim+v
    elif dir == "up":
        return x, y, aim-v
    
x,y, aim=0,0,0
for dir, v in nums:
    x, y, aim = upatePos(dir, int(v), x, y, aim)
    print(x,y,aim)

print(x,y, x*y)