def diagonalDifference(arr):
    firstdiag = 0
    second = 0
    a = len(arr)
    for i in range(a):
        firstdiag += arr[i][i]
        second += arr[i][a-i-1]
    return abs(firstdiag - second)
