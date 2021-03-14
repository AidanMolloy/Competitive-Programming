# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest = -9*7
    for row in range(len(arr)-2):
        for column in range(len(arr)-2):
            total = arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row+1][column+1] + arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2]

            highest = max(total, highest)

    return highest
