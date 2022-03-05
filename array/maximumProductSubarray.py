def maximumProductSubarray(a):
    res = max(a)
    currMin, currMax = 1, 1
    for num in a:
        temp = currMax*num
        currMax = max(temp, num*currMin, num)
        currMin = min(temp, num*currMin, num)
        res = max(res, currMax)
    return res


nums = [-2, 3, -4]
print(maximumProductSubarray(nums))
