t = int(input())
for i in range(t):
    n = int(input())
    nums = input().split()
    Alice = Bob = 0
    numsOne = nums.count("1")
    numsTwo = nums.count("2")
    if numsTwo % 2 != 0:
        Alice += 2
    while(numsOne > 0):
        if Alice > Bob:
            Bob += 1
        else:
            Alice += 1
        numsOne -= 1
    if Alice == Bob:
        print("YES")
    else:
        print("NO")