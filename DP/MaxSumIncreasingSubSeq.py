from collections import deque
def maxSumIncreasingSubsequence(array):
    sums = array[:]
    seq = [None for _ in range(len(array))]
    maxIdx = 0
    for i in range(len(array)):
        curr_sum = array[i]
        for j in range(0,i):
            if array[j] < array[i] and sums[j] + sums[i] > curr_sum:
                curr_sum = sums[j] + sums[i]
                seq[i] = j
        sums[i] = curr_sum
        if sums[i] >= sums[maxIdx]:
            maxIdx = i

    max_sum = sums[maxIdx]
    result = []
    result.append(max_sum)

    indexList = deque()
    indexList.appendleft(array[maxIdx])

    while seq[maxIdx] != None:
        maxIdx = seq[maxIdx]
        indexList.appendleft(array[maxIdx])

        
    result.append(list(indexList))
    return result

print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))