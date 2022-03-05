def productOfArrayExceptSelf(a):
    res = [0]*len(a)
    pre = 1
    pos = 1

    for i in range(len(a)):
        res[i] = pre
        pre = pre*a[i]
    print(res)

    for j in reversed(range(len(a))):
        res[j] = pos*res[j]
        pos = pos*a[j]
    return res


nums = [1, 2, 3, 4]
print(productOfArrayExceptSelf(nums))
