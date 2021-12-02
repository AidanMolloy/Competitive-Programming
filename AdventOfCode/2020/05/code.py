# Read input
inFile = open("input.txt", "r")
line = inFile.readline()
boardingPasses = []
seatIDList = []

while line != "":
    line = line.strip()
    boardingPasses.append(line)
    line = inFile.readline()

for boarding in boardingPasses:
    low = 0
    high = 127
    for letter in boarding[:7]:
        if letter == "F":
            high = (low + high-1) / 2
        else:
            low = (low + high+1) / 2
    row = high
    low = 0
    high = 7
    for letter in boarding[-3:]:
        if letter == "L":
            high = (low + high-1) / 2
        else:
            low = (low + high+1) / 2
    seat = high
    seatID = (row * 8) + seat
    seatIDList.append(seatID)
seatIDList.sort()

## Part 1
def part1():
    return int(seatIDList[-1])

## Part 2
def part2():
    for i in range(1, len(seatIDList)-2):
        if (seatIDList[i]-seatIDList[i-1]) != 1:
            return int(seatIDList[i]-1)

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())