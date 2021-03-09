mirrored = [-1] * 10
mirrored[0] = 0
mirrored[1] = 1
mirrored[2] = 5
mirrored[5] = 2
mirrored[8] = 8

def isValid(hour, minute, h, m):
    h2 = hour%10                    #2
    h1 = (hour-h2)//10              #1
    m2 = minute%10                  #0
    m1 = (minute-m2)//10            #5
    if mirrored[h2] != -1 and mirrored[h1] != -1 and mirrored[m2] != -1 and mirrored[m1] != -1:
        current_h = mirrored[m2]*10 + mirrored[m1]
        current_m = mirrored[h2]*10 + mirrored[h1]
        if current_h < h and current_m < m:
            return True
    else:
        return False

T = int(input())
for _ in range(T):
    h, m = map(int, input().strip().split())
    time = input()
    current_h = int(time[:2])
    current_m = int(time[3:])
    while(True):
        if isValid(current_h, current_m, h, m):
            ans = ""
            if current_h < 10:
                ans += "0"
            ans += str(current_h)
            ans += ":"
            if current_m < 10:
                ans += "0"
            ans += str(current_m)
            print(ans)
            break
        
        if current_m < m-1:
            current_m += 1
        else:
            if current_h < h-1:
                current_h += 1
                current_m = 0
            else:
                current_h = 0
                current_m = 0