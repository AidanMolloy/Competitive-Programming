## Part 1
def part1():
    inFile = open("input.txt", "r")
    line = inFile.readline()
    count = 0
    while line != "":
        line = line.strip().split()
        minMix = line[0].split("-")
        if int(minMix[0]) <= line[2].count(line[1].strip(":")) and int(minMix[1]) >= line[2].count(line[1].strip(":")):
            count += 1
        line = inFile.readline()

    return count

## Part 2
def part2():
    inFile = open("input.txt", "r")
    line = inFile.readline()
    count = 0
    while line != "":
        line = line.strip().split()
        firstPos, secondPos = map(int, line[0].split("-"))
        first = False
        second = False

        if line[2][firstPos-1] == line[1].strip(":"):
            first = True
            
        if line[2][secondPos-1] == line[1].strip(":"):
            second = True

        if bool(first) != bool(second):
            count +=1
        
        line = inFile.readline()

    return count

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())