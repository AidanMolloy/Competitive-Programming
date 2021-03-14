# Read input
inFile = open("input.txt", "r")
goal = int(inFile.readline().strip())
busID = inFile.readline().split(",")

# Part 1
def part1():
    bestBus = 0
    bestWaitingTime = -1
    for bus in busID:
        if bus != "x":
            if goal % int(bus) != 0:
                availableFrom = goal / int(bus)
                comesAt = (goal // int(bus)) +1
                waitingTime = (comesAt-availableFrom) * float(bus)
                if bestWaitingTime == -1 or waitingTime < bestWaitingTime:
                    bestWaitingTime = waitingTime
                    bestBus = bus
            else:
                return 0 # waiting zero minutes
    return int(int(bestBus) * bestWaitingTime)

# Part 2
def part2(busID, timings):
    count = 0
    for bus in busID:
        if bus == "x":
            count += 1
        else:
            timings.append(count)
            count += 1
    busID = list(filter(("x").__ne__, busID))
    timestamp = 1
    addition = int(max(busID)) + 60
    while(True):
        for i in range(len(busID)):
            goal = int(busID[i]) + int(timings[i])
            if timestamp != goal:
                break
        else:
            return timestamp
        timestamp += addition
        if timestamp % 10000000 == 0:
            print(timestamp)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2(busID, []))