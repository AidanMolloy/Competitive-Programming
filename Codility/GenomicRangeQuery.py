# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    res = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            res.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            res.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            res.append(3)
        else:
            res.append(4)
    return res
    
print(solution('A', [0], [0]))
