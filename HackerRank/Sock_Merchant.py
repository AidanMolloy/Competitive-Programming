# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    socks = {}
    
    for i in ar:
            if i in socks:
                socks[i]+=1
            else:
                socks[i] = 1

    for j in socks:
        pairs += math.floor(socks[j]/2)
    return pairs
