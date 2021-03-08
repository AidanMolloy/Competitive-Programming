t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    new_arr = [arr[0]] * n
    for i in range(1,n):
        new_arr[i] = new_arr[i-1] + arr[i]
    min_needed = 0
    for j in range(n):
        min_needed += j
        if not new_arr[j] >= min_needed:
            print("NO")
            break
    else:
        print("YES")