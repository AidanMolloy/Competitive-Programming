# Read input
inFile = open("input.txt", "r")
line = inFile.readline()
instructions = []

while line != "":
    line = line.strip()
    instructions.append(line)
    line = inFile.readline()

# Part 1
def part1():
    distTravelled = {"N": 0, "E": 0, "S": 0, "W": 0}
    directions = ["N", "E", "S", "W"]
    facing = "E"
    for instruct in instructions:
        if instruct[0] == "F":
            distTravelled[facing] += int(instruct[1:])
        elif instruct[0] == "R":
            turns = (int(instruct[1:]) / 90)
            current = directions.index(facing)
            while turns > 0:
                if current + 1 < len(directions):
                    current += 1
                else:
                    current = 0
                turns -= 1
            facing = directions[current]
        elif instruct[0] == "L":
            turns = (int(instruct[1:]) / 90)
            current = directions.index(facing)
            while turns > 0:
                if current - 1 >= 0:
                    current -= 1
                else:
                    current = len(directions)-1
                turns -= 1
            facing = directions[current]
        else:
            distTravelled[instruct[0]] += int(instruct[1:])

    return abs(distTravelled["N"] - distTravelled["S"]) + abs(distTravelled["E"] - distTravelled["W"])



# Part 2
def part2():
    distTravelled = {"N": 0, "E": 0, "S": 0, "W": 0}
    waypoint = {"N": 1, "E": 10, "S": 0, "W": 0}
    for instruct in instructions:
        if instruct[0] == "F":
            for direction in waypoint:
                distTravelled[direction] += (waypoint[direction] * int(instruct[1:]))
        elif instruct[0] == "R":
            turns = (int(instruct[1:]) / 90)
            while turns > 0:
                temp = waypoint["N"]
                waypoint["N"] = waypoint["W"]
                waypoint["W"] = waypoint["S"]
                waypoint["S"] = waypoint["E"]
                waypoint["E"] = temp
                turns -= 1
        elif instruct[0] == "L":
            turns = (int(instruct[1:]) / 90)
            while turns > 0:
                temp = waypoint["N"]
                waypoint["N"] = waypoint["E"]
                waypoint["E"] = waypoint["S"]
                waypoint["S"] = waypoint["W"]
                waypoint["W"] = temp
                turns -= 1
        else:
            waypoint[instruct[0]] += int(instruct[1:])

    return abs(distTravelled["N"] - distTravelled["S"]) + abs(distTravelled["E"] - distTravelled["W"])
if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())