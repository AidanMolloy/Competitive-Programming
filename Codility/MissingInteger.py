# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    seen = [False] * len(A)
    for i in A:
        if 0 < i <= len(A):
            seen[i-1] = True

    for num in range(len(seen)):
        if seen[num] == False:
            return num+1
    
    return len(A)+1

print(solution([-1,2,-3]))