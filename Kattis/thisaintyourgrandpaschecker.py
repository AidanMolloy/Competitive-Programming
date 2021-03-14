n = int(input())
grid =[]
for i in range(n):
    row = input()
    grid.insert(i,[])
    for j in range(len(row)):
        grid[i].insert(j, row[j])

output = 1
for i in range(n):
    rowCount = 0
    BinARow = 0
    WinARow = 0
    for j in range(n):
        if grid[i][j] == "B":
            rowCount +=1
            BinARow +=1
            WinARow = 0
        else:
            WinARow +=1
            BinARow = 0
        if BinARow == 3 or WinARow == 3:
            output = 0
    if rowCount != n / 2:
        output = 0

for i in range(n):
    rowCount = 0
    BinARow = 0
    WinARow = 0
    for j in range(n):
        if grid[j][i] == "B":
            rowCount +=1
            BinARow +=1
            WinARow = 0
        else:
            WinARow +=1
            BinARow = 0
        if BinARow == 3 or WinARow == 3:
            output = 0
    if rowCount != n / 2:
        output = 0

print(output)
