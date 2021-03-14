#BinaryGap // MinDistinct

def solution(N):
    binary = bin(N)[2:]
    longest = 0
    count = -1
    for i in binary:
        if count != -1:
            if i == '0':
                count += 1
        if i == '1':
            longest = max(longest, count)
            count = 0

    return longest

print(solution(1041))