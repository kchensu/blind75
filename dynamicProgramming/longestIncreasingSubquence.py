def longestIncreasingSubsequence(a):
    res = [1]*len(a)
    for r in reversed(range(len(a))):
        for l in range(r + 1, len(a)):
            if a[r] < a[l]:
                res[r] = max(res[r], 1 + res[l])
    return max(res)


a = [10, 9, 2, 5, 3, 7, 101, 18]
print(longestIncreasingSubsequence(a))
