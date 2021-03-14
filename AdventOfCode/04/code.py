import re
# Read input
inFile = open("input.txt", "r")
lines = inFile.read()
passportDB = []

lines = lines.split("\n\n")
for line in lines:
    user = {}
    fields = line.replace("\n", " ").split(" ")
    for field in fields:
        if field != "":
            user[field.split(":")[0]] = field.split(":")[1]
    passportDB.append(user)

## Part 1
def part1():
    valid = 0
    requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for user in passportDB:
        for require in requirements:
            if require not in user:
                break
        else:
            valid += 1

    return valid

## Part 2
def part2():
    valid = 0
    for user in passportDB:
        if 'byr' in user.keys():
            year = int(user['byr'])
            if not(year >= 1920 and year <= 2002):
                continue
        else:
            continue

        if 'iyr' in user.keys():
            year = int(user['iyr'])
            if not (year >= 2010 and year <= 2020):
                continue
        else:
            continue

        if 'eyr' in user.keys():
            year = int(user['eyr'])
            if not (year >= 2020 and year <= 2030):
                continue
        else:
            continue

        if "hgt" in user:
            if "cm" in user["hgt"]:
                if not (int(user["hgt"][:-2]) >= 150 and int(user["hgt"][:-2]) <= 193):
                    continue
            elif "in" in user["hgt"]:
                if not (int(user["hgt"][:-2]) >= 59 and int(user["hgt"][:-2]) <= 76):
                    continue
            else:
                continue
        else:
            continue

        if 'hcl' in user.keys():
            value = user['hcl']

            regex = "^#(?:[0-9a-fA-F]{6})$"
            p = re.compile(regex)
            match = re.search(p, value)
            if not match:
                continue
        else:
            continue

        if 'ecl' in user.keys():
            value = user['ecl']
            if not (value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth'):
                continue
        else:
            continue

        if 'pid' in user.keys():
            value = user['pid']
            if not (len(value) == 9 and value.isnumeric()):
                continue
        else:
            continue

        valid += 1

    return valid

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())
    pass