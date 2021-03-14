import re

# Read input
inFile = open("input.txt", "r")
line = inFile.readline()
bagRules = {}
count = 0

while line != "":
    line = line.strip()
    bagType = line.split("contain")[0].strip().replace(" bags", "")
    line = line.split("contain")[1].strip().strip(".").replace(" bags", "").replace(" bag", "")
    rules = line.split(", ")
    if "no other" not in rules:
        bagRules[bagType] = rules
    else:
        bagRules[bagType] = []
    line = inFile.readline()

# Part 1
def findContains(bagType, usedBags):
    count = 0
    for bag in bagRules:
        if bag not in usedBags:
            for bagRule in bagRules[bag]:
                if re.search(".+"+bagType, bagRule):
                    count += 1
                    usedBags.append(bag)
                    count += findContains(bag, usedBags)
    return count

# Part 2
def countBags(bagType):
    count = 0
    for bag in bagRules[bagType]:
        bagMultiply = bag.split(" ")[0]
        count += max(int(bagMultiply),(int(bagMultiply) * countBags(bag[len(bagMultiply)+1:])+int(bagMultiply)))
    return count

if __name__ == "__main__":
    print("Part 1:", findContains("shiny gold", []))
    print("Part 2:", countBags("shiny gold"))