t = int(input())

for _ in range(t):
    count = 0
    n = int(input())
    arr = list(map(int,input().split()))
    i=0
    c0 = c1 = c2 = 0
    for i in arr:
        if i % 3 == 0:
            c0 += 1
        elif i % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    
    while(True):
        if c2 > c0:
            c2 -= 1
            c0 += 1
            count += 1
        elif c0 > c1:
            c0 -= 1
            c1 += 1
            count += 1
        elif c1 > c2:
            c1 -= 1
            c2 += 1
            count += 1
        else:
            break
    print(count)