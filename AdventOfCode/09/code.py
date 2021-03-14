# Read input
inFile = open("input.txt", "r")
line = inFile.readline()
nums = []

while line != "":
    line = int(line.strip())
    nums.append(line)
    line = inFile.readline()

# Part 1
def checkPrev(i):
    for j in range(i-25, i):
        for k in range(j+1, i):
            if j != k:
                if nums[i] == nums[j] + nums[k]:
                    return True
    return False

def part1():
    for i in range(25, len(nums)):
        if not checkPrev(i):
            return nums[i] 

# Part 2
def part2():
    target = part1()
    for i in range(len(nums)):
        testSet = []
        j = 0
        while(sum(testSet) < target):
            testSet.append(nums[i+j])
            if sum(testSet) == target:
                return min(testSet) + max(testSet)
            j+=1

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())