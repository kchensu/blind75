def twoSum(a, t):
    h = {}
    for i, val in enumerate(a):
        if t - val in h:
            return [h[t-val], i]
        else:
            h[val] = i


a = [3, 2, 4]
t = 6
print(twoSum(a, t))
