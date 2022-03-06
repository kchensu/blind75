def threeSum(a):
    res = []
    a.sort()
    for i, val in enumerate(a):
        if i > 0 and val == a[i-1]:
            continue

        l, r = i+1, len(a) - 1
        while l < r:
            threeS = val + a[l] + a[r]
            if threeS > 0:
                r -= 1
            elif threeS < 0:
                l += 1
            else:
                res.append([val, a[l], a[r]])
                l += 1
                while a[l] == a[l - 1] and l < r:
                    l += 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
