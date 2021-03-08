t = int(input())

for _ in range(t):
    count = 0
    n = int(input())
    arr = list(map(int,input().split()))
    i=0
    while n-1 > i:
        if arr[i] > (arr[i+1]*2):
            if arr[i] % 2 == 1:
                arr.insert(i+1, arr[i]//2+1)
            else:
                arr.insert(i+1, arr[i]//2)
            count += 1
            n+=1
            i+=1
        elif (arr[i]*2) < arr[i+1]:
            arr.insert(i+1, arr[i]*2)
            count += 1
            n+=1
            i+=1
        else:
            i+=1
    print(count)
