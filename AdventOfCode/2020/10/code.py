# Read input
inFile = open("input.txt", "r")
line = inFile.readline()
adapters = [0]

while line != "":
    line = int(line.strip())
    adapters.append(line)
    line = inFile.readline()

adapters.append(max(adapters)+3)
adapters = sorted(adapters)

# Part 1
def part1():
    one = three = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] == 1:
            one += 1
        elif adapters[i] - adapters[i-1] == 3:
            three += 1
    return one * three

# Part 2
memo = {}
def part2(i):
    if i == len(adapters)-1:
        return 1
    if i in memo:
        return memo[i]
    ans = 0
    for j in range(i+1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            ans += part2(j)
    memo[i] = ans
    return ans

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2(0))