#OddOccurencesInArray // LargestSequenceGap

def solution(A):
    dict = {}
    for i in A:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict:
        if dict[i] % 2 == 1:
            return i

print(solution([5,5,6,6,7]))