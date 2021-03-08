n=int(input())
for i in range(n):
    t=int(input())
    if(t==1 or t==2):
        print(0)
    elif(t%2==0):
        print(t//2-1)
    else:
        print(t//2)