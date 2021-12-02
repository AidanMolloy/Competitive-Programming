# Read input
inFile = open("input.txt", "r")
line = inFile.readline()
bootCode = []

while line != "":
    line = line.strip()
    bootCode.append(line)
    line = inFile.readline()

# Part 1
def part1(codeToRun):
    visitedInstructions = []
    accum = 0
    i = 0
    while True:
        if i in visitedInstructions:
            return accum
        elif i >= len(codeToRun):
            return accum
        visitedInstructions.append(i)
        inst, val = codeToRun[i].split(" ")
        if inst == "acc":
            accum += int(val)
            i += 1
        elif inst == "jmp":
            i += int(val)
        elif inst == "nop":
            i += 1

# Part 2
def findAccum(codeToRun):
    visitedInstructions = []
    accum = 0
    i = 0
    while True:
        if i in visitedInstructions:
            return False
        elif i >= len(codeToRun):
            return accum
        visitedInstructions.append(i)
        inst, val = codeToRun[i].split(" ")
        if inst == "acc":
            accum += int(val)
            i += 1
        elif inst == "jmp":
            i += int(val)
        elif inst == "nop":
            i += 1


def jumbleCode(inst, convert):
    newCode = bootCode[:]
    newCode[inst] = convert + bootCode[inst][3:]
    return newCode 

def checkValid():
    for line in range(len(bootCode)-1):
        inst, val = bootCode[line].split(" ")
        if inst == "jmp":
            jmpToNop = jumbleCode(line, "nop")
            if findAccum(jumbleCode(line, "nop")):
                return findAccum(jmpToNop)
        elif inst == "nop":
            nopToJmp = jumbleCode(line, "jmp")
            if findAccum(nopToJmp):
                return findAccum(nopToJmp)

if __name__ == "__main__":
    print("Part 1:", part1(bootCode))
    print("Part 2:", checkValid())