## Part 1

def readMap():
    inFile = open("input.txt", "r")
    line = inFile.readline().strip("\n")
    puzzleMap = []
    while line != "":
        newLine = []
        for char in line:
            newLine.append(char)
        puzzleMap.append(newLine)
        line = inFile.readline().strip("\n")

    return puzzleMap


def part1(puzzleMap):
    
    treeCount = col = row = 0
    while (row < len(puzzleMap)):
        cursor = puzzleMap[row][col]
        if cursor == "#":
            treeCount += 1
        if len(puzzleMap[0])-1 > col + 3:
            col += 3
        else:
            col = (col + 3) - len(puzzleMap[0])
        row += 1
        
    return treeCount

def part2(puzzleMap):
    
    return(slopeTraversal(1, 1, puzzleMap))* (slopeTraversal(3, 1, puzzleMap)) * (slopeTraversal(5, 1, puzzleMap)) * (slopeTraversal(7, 1, puzzleMap)) * (slopeTraversal(1, 2, puzzleMap))

def slopeTraversal(right, down, puzzleMap):
    
    treeCount = col = row = 0
    while (row < len(puzzleMap)):
        cursor = puzzleMap[row][col]
        if cursor == "#":
            treeCount += 1
        if len(puzzleMap[0])-1 > col + right:
            col += right
        else:
            col = (col + right) - len(puzzleMap[0])
        row += down
        
    return treeCount

if __name__ == "__main__":
    print("Part 1: ", part1(readMap()))
    print("Part 2: ", part2(readMap()))