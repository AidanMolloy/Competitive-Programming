# Imports
import random

# Solution
def solution(A):
    N = len(A)
    ways_to_cut_tree = 0
    valid = False

    # Check if it is already Aesthetically Pleasing
    for tree in range(1, N-1):
        if A[tree-1] < A[tree] and A[tree] > A[tree+1]:
            # Larger than left and right it's a peak
            valid = True
        elif A[tree-1] > A[tree] and A[tree] < A[tree+1]:
            # Smaller than left and right it's a dip
            valid = True
        else:
            # Not a peak or a dip, therefore aesthetically pleasing
            valid = False
            break

    # Already Aesthetically Pleasing
    if valid:
        return 0

    # Cut each tree and check if it makes it Aesthetically Pleasing 
    for i in range(N):
        temp_trees = A.copy()
        del temp_trees[i] # Remove Tree at index i
        valid = False
        for tree in range(1, N-2):
            if not valid and tree != 1:
                # If it has already checked at least one tree and it is invalid we cannot count this iteration
                break
            if temp_trees[tree - 1] < temp_trees[tree] and temp_trees[tree] > temp_trees[tree + 1]:
                # Larger than left and right it's a peak
                valid = True
            elif temp_trees[tree - 1] > temp_trees[tree] and temp_trees[tree] < temp_trees[tree + 1]:
                # Smaller than left and right it's a dip
                valid = True
            else:
                # Not a peak or a dip, therefore aesthetically pleasing
                valid = False

        if valid:
            ways_to_cut_tree += 1

    if ways_to_cut_tree == 0:
        # If you cannot make the tree Aesthetically Pleasing
        return -1

    # Return amount of ways to cut tree
    return ways_to_cut_tree

def gen(size):
    a = [random.randint(1, 1000) for i in range(4, size * 2)]
    return (a)

print(solution([1,2,3,4,5]))
print(solution([3,4,5,3,7]))
print(solution([1,3,1,2,1]))