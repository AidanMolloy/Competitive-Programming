def solution(A, K):
    if len(A) == 0 or K == 0:
        return A
    if K % len(A) == 0:
        rotations = 1
    else:
        rotations = K % len(A)
    old = A
    new = [0]*len(A)
    for i in range(K):
        new[0]=old[-1]
        new[1:] = old[:-1]
        old = new.copy()
    return new

print(solution([1,2], 3))