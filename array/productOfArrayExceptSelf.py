import numpy as np


def productOfArrayExceptSelf(a):
    left = [0]*len(a)
    right = [0]*len(a)
    pre = 1
    pos = 1

    for i in range(len(a)):
        left[i] = pre
        pre = pre*a[i]

    for j in reversed(range(len(a))):
        left[j] = pos*left[j]
        pos = pos*a[j]

    return left


nums = [1, 2, 3, 4]
print(productOfArrayExceptSelf(nums))
