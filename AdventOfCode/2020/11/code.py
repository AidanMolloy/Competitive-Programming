import copy
# Read input
inFile = open("input.txt", "r")
layout = []
line = inFile.readline()

while line != "":
    inner = []
    line = line.strip()
    for letter in line:
        inner.append(letter)
    layout.append(inner)
    line = inFile.readline()

# Part 1
def isNotAdjacent(layout, row, col, key):
    x = [-1, 0, 1]
    y = [-1, 0, 1]
    for i in x:
        for j in y:
            if not(i == j == 0):
                if row+i >= 0 and row+i < len(layout) and col+j >= 0 and col+j < len(layout[0]):
                    if layout[row+i][col+j] == key:
                        return False
    return True

def isAdjacent(layout, row, col, key):
    count = 0
    x = [-1, 0, 1]
    y = [-1, 0, 1]
    for i in x:
        for j in y:
            if not(i == j == 0):
                if row+i >= 0 and row+i < len(layout) and col+j >= 0 and col+j < len(layout[0]):
                    if layout[row+i][col+j] == key:
                        count += 1
    if count >= 4:
        return True
    return False

def part1(layout):
    while True:
        newLayout = copy.deepcopy(layout)
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == "L" and isNotAdjacent(layout, i, j, '#'):
                    newLayout[i][j] = "#"
                elif layout[i][j] == "#" and isAdjacent(layout, i, j, '#'):
                    newLayout[i][j] = "L"

        if layout == newLayout:
            count = 0
            for i in range(len(layout)):
                for j in range(len(layout[0])):
                    if layout[i][j] == "#":
                        count += 1
            return count
            
        layout = copy.deepcopy(newLayout)

# Part 2
def getValue(array2d, i, j):
    if (i < 0 or j < 0 or i >= len(array2d) or j >= len(array2d[0])):
        return ''
    else:
        return array2d[i][j]      

def occupiedSeatsVisible(array2d, i, j):
    around = ['?','?','?',
              '?',    '?',
              '?','?','?']
    radius = 1
    while around.count('?') > 0:
        if (around[0] == '?'): # top left
            t = getValue(array2d, i-radius, j-radius)
            if t in ['#','L','']: around[0] = t
        if (around[1] == '?'): # top
            t = getValue(array2d, i-radius, j)
            if t in ['#','L','']: around[1] = t
        if (around[2] == '?'): # top right
            t = getValue(array2d, i-radius, j+radius)
            if t in ['#','L','']: around[2] = t
        if (around[3] == '?'): # left
            t = getValue(array2d, i,        j-radius)
            if t in ['#','L','']: around[3] = t
        if (around[4] == '?'): # right
            t = getValue(array2d, i,        j+radius)
            if t in ['#','L','']: around[4] = t
        if (around[5] == '?'): # bottom left
            t = getValue(array2d, i+radius, j-radius)
            if t in ['#','L','']: around[5] = t
        if (around[6] == '?'): # bottom
            t = getValue(array2d, i+radius, j)
            if t in ['#','L','']: around[6] = t
        if (around[7] == '?'): # bottom right
            t = getValue(array2d, i+radius, j+radius)
            if t in ['#','L','']: around[7] = t
        # increase search radius
        radius += 1
    return around

def compare(array2d1,array2d2):
    for i in range(len(array2d1)):
        for j in range(len(array2d1[i])):
            if (array2d1[i][j] != array2d2[i][j]):
                return False
    return True

def part2():
    lines = layout
    modified = True
    cycles = 0
    while modified:
        cycles += 1
        linesNext = copy.deepcopy(lines)
        for i in range(len(linesNext)):
            for j in range(len(linesNext[0])):
                if (lines[i][j] in ['L','#']):
                    t = occupiedSeatsVisible(lines,i,j)
                    if (t.count('#') == 0):
                        linesNext[i][j] = '#'
                    elif (t.count('#') >= 5 and lines[i][j] in ['L','#']):
                        linesNext[i][j] = 'L'
        #printArray(cycles, lines)
        modified = not compare(lines, linesNext)
        lines = copy.deepcopy(linesNext)
    seats = 0
    for l in lines:
        seats += l.count('#')
    return seats

if __name__ == "__main__":
    print("Part 1:", part1(layout))
    print("Part 2:", part2())