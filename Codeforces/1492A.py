t = int(input())

for _ in range(t):
    count = 0
    p,a,b,c = map(int,input().split())
    new_a = a
    new_b = b
    new_c = c
    if new_a<p:
        new_a += a * ((p//a)-1)
        if new_a<p:
            new_a += a
    if new_b<p:
        new_b += b * ((p//b)-1)
        if new_b<p:
            new_b += b
    if new_c<p:
        new_c += c * ((p//c)-1)
        if new_c <p:
            new_c += c

    min_num = new_a - p
    if new_b-p < min_num:
        min_num = new_b-p
    if new_c-p < min_num:
        min_num = new_c-p
    
    
    print(min_num)