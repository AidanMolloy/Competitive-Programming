# Imports
import random

# Solution
def solution(A, K):
    if len(A) < K:
        return -1
    # Sort A high to low
    A = sorted(A, reverse=True)
    even = []
    odd = []
    # Divide values into a odd and even list
    for index in range(len(A)):
        if A[index] % 2 == 0:
            even.append(A[index])
        else:
            odd.append(A[index])

    total_sum = 0
    even_index = odd_index = 0
    # While there are still K elements to be added to total sum
    while K > 0:
        # If only one element left pick biggest even number
        if K == 1:
            if even_index <= len(even) - 1:
                total_sum += even[even_index]
                even_index += 1
                K -= 1
            else:
                return -1
        else:
            # If there's less than 2 odd numbers left, add even number
            if odd_index >= len(odd) - 1:
                total_sum += even[even_index] + even[even_index + 1]
                even_index += 2
            # If there's less than 2 even numbers left, add odd number
            elif even_index >= len(even) - 1:
                total_sum += odd[odd_index] + odd[odd_index + 1]
                odd_index += 2
            # If the 2 biggest Even are greater than 2 biggest odd, add 2 biggest even
            elif even[even_index] + even[even_index + 1] > odd[odd_index] + odd[odd_index + 1]:
                total_sum += even[even_index] + even[even_index + 1]
                even_index += 2
            # Otherwise add 2 biggest odd
            else:
                total_sum += odd[odd_index] + odd[odd_index + 1]
                odd_index += 2
        K -= 2

    # Return Answer
    return total_sum


def gen(size):
    a = random.randint(size, size * 2)

    d = [random.randint(1, 10000) for i in range(size * 2)]
    return (d, a)

print(solution([4,9,8,2,6], 3))
print(solution([5,6,3,4,2], 5))
print(solution([7,7,7,7,7], 1))
print(solution([1000], 2))
print(solution([2,3,3,5,5], 3))
print(solution([], 3))
print(solution([1,2,3,4,5], 5))