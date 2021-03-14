# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    valleyCount = 0
    inValley = False
    for i in s:
        if i == "U":
            altitude += 1
            if inValley:
                if altitude == 0:
                    inValley = False
                    valleyCount += 1
        else:
            altitude -= 1
            if not inValley:
                if altitude < 0:
                    inValley = True

    return valleyCount
