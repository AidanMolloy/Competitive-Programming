# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    last = 0
    for i in range(len(A)):
        if A[i] - last != 1:
            return A[i]-1
        last = A[i]
    return len(A)+1

print(solution([2,3,1,5]))