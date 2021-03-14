# Imports
import random

# Solution
def solution(A):
    # Sort the list to cluster racks together.
    A = sorted(A)
    largest = 0
    for i in range(len(A) - 1):
        # Look for the max difference between adjacent rack locations and set to largest.
        diff = max(A[i] - A[i + 1], A[i + 1] - A[i]) // 2
        if diff > largest:
            largest = diff
    # Return Answer
    return largest


def gen(size):
    return [random.randint(-1_000_000, 1_000_000) for i in range(size)]
    # return [0]

print(solution([5, 5]))
print(solution([10, 0, 8, 2, -1, 12, 11, 3]))
print(solution([]))
print(solution([2]))
print(solution([2,2,2,2]))
print(solution([1,10]))