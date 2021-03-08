from sys import *
l = 1
r = 1000000
while (l != r):
    mid = (l+r+1) //2
    print(mid)
    stdout.flush()
    if input() == "<":
        r = mid - 1
    else:
        l = mid
print("!",l)
stdout.flush()