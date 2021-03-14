def solution(N, A):
    counters = [0] * N
    m = 0
    last_m = 0
    n1 = N+1
    for i in A:
        if i < n1:
            if counters[i-1] < last_m:
                counters[i-1] = last_m

            counters[i-1]+=1

            if counters[i-1] > m:
                m = counters[i-1]
        else:
            last_m = m

    for i in range(len(counters)):
        if counters[i] < last_m:
            counters[i] = last_m

    return counters