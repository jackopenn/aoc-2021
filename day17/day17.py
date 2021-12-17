# x1, x2, y1, y2 = 20, 30, -10, -5
x1, x2, y1, y2 = 85, 145, -163, -108

x, y = 0, 0


def update(x, y, xv, yv):
    x += xv
    y += yv

    if xv > 0:
       xv -= 1
    elif xv < 0:
       xv += 1
    else:
       xv = 0
    yv -= 1
    return x, y, xv, yv


hit_cnt = 0
max_ys = []
for ix in range(1, x2+1):
    for iy in range(y1, abs(y1)):
        xv, yv = ix, iy
        x, y = 0, 0

        ys = []
        # print(xv,yv)
        while True:
            x,y,xv,yv = update(x,y,xv,yv)
            # print(x,y,xv,yv)
            ys.append(y)
            if x in list(range(x1,x2+1)) and y in list(range(y1,y2+1)):
                # print("hit", ix, iy)
                max_ys.append(max(ys))
                break
            elif x > x2 or y < y1:
                break 

# print(max_ys)
print(max(max_ys))
print(len(max_ys))