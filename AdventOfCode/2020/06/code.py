# Read input
inFile = open("input.txt", "r")
lines = inFile.read()
passportDB = []
count = 0

groups = lines.split("\n\n")

# Part 1
def part1():
    count = 0
    for group in groups:
        users = group.split("\n")
        yes = []
        for user in users:
            for letter in user:
                if letter not in yes:
                    yes.append(letter)
                    count += 1
    return count


# Part 2
def part2():
    count = 0
    for group in groups:
        users = group.split("\n")
        yes = {}
        for user in users:
            userLetters = []
            for letter in user:
                if letter not in userLetters:
                    userLetters.append(letter)
                    if letter in yes:
                        yes[letter] = yes[letter]+1
                    else:
                        yes[letter] = 1
        for letter in yes:
            if yes[letter] == len(users):
                count += 1
    return count

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())