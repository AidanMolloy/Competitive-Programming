inFile = open("input.txt", "r")
inputList = []
line = inFile.readline()

while line != "":
    line = line.strip()
    inputList.append(line)
    line = inFile.readline()

## Part 1
def part1():
    for i in inputList:
        for j in inputList:
            if int(i)+int(j) == 2020:
                return(int(i)*int(j))

## Part 2
def part2():
    for i in inputList:
        for j in inputList:
            for k in inputList:
                if int(i)+int(j)+int(k) == 2020:
                    return(int(i)*int(j)*int(k))

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())