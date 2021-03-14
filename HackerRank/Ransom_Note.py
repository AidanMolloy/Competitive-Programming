# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazineLetters = {}
    for i in magazine:
        if magazineLetters.get(i) != None:
            magazineLetters[i] += 1
        else:
            magazineLetters[i] = 1

    for j in note:
        if magazineLetters.get(j) is None or magazineLetters[j] == 0:
            print("No")
            return False
        else:
            magazineLetters[j] -= 1
        
    print("Yes")
