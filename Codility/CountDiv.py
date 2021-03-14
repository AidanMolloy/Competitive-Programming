def solution(A, B, K):
    min_val = ((A+K-1) // K) *K

    if min_val > B:
        return 0

    return ((B-min_val) // K) +1

print(solution(1,50,11))