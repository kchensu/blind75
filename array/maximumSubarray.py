def maximumSubarray(a):
    if len(a) == 0:
        return 0

    currMax = a[0]
    globalMax = a[0]

    for i in range(1, len(a)):
        currMax = max(a[i], currMax + a[i])
        if currMax > globalMax:
            globalMax = currMax
    return globalMax


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumSubarray(nums))
