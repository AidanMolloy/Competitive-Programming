import math
T = int(input())
for _ in range(T):
    n, k = map(int, input().strip().split())
    ans = []
    for i in range(k+1, n+1):
        ans.append(i)
    for i in range(math.floor((k+1)/2), k):
        ans.append(i)

    print(len(ans))
    print(" ".join(map(str, ans)))
