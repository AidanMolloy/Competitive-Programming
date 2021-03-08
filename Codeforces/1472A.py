t = int(input())
for i in range(t):
    count = 1
    multiplier = 1
    w, h, n = map(int, input().split())
    while(True):
        if w%2 == 0:
            w /= 2
            count += 1 * multiplier
            multiplier *= 2
        elif h%2 == 0:
            h /= 2
            count += 1 * multiplier
            multiplier *= 2
        else:
            break
    if count >= n:
        print("YES")
    else:
        print("NO")