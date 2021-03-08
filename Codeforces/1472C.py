t=int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    j = n-2
    while j >= 0:
        if j + l[j] < n:
            l[j] += l[j+l[j]]
        j-=1
    print(max(l))