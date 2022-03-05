from collections import defaultdict
import numpy as np

# amount = 11
# coins = [1, 2, 5]

# dp = [float('inf')]*(amount + 1)
# dp[0] = 0
# print(dp)
# for a in range(1, amount + 1):
#     for c in coins:
#         if a - c >= 0:
#             dp[a] = min(dp[a], 1 + dp[a - c])

# print(dp)


###  Count the number of bits ###


def count_bits(x):
    num_bits = 0
    while(x):
        num_bits = num_bits + (x & 1)
        x = x >> 1
    return num_bits


def parity(x):
    res = 0
    while(x):
        res = res ^ (x & 1)
        x = x >> 1
    return res


def parity2(x):
    res = 0
    while(x):
        res = res ^ 1
        x = x & (x - 1)
    return res


def parity3(x):
    x = x ^ x >> 32
    x = x ^ x >> 16
    x = x ^ x >> 8
    x = x ^ x >> 4
    x = x ^ x >> 2
    x = x ^ x >> 1
    return x & 0x1


def partition2(pivot, a):
    left = 0
    right = len(a) - 1
    p = a[pivot]
    for i in range(len(a)):
        if a[i] < p:
            a[i], a[left] = a[left], a[i]
            left += 1

    for j in reversed(range(len(a))):
        if a[j] < p:
            break
        elif a[j] > p:
            a[j], a[right] = a[right], a[j]
            right -= 1
    return a


def partition3(pivot, a):
    p = a[pivot]
    left, middle, right = 0, 0, len(a)
    while(middle < right):
        if a[middle] < p:
            a[left], a[middle] = a[middle], a[left]
            left += 1
            middle += 1
        elif a[middle] == p:
            middle += 1
        else:
            right -= 1
            a[middle], a[right] = a[right], a[middle]
    return a


# a = [8, 3, 5, 1, 10]
# b = partition2(2, a)
# c = partition3(2, a)
# print(b)
# print(c)
# 3 1 5 10 8
# newarray=sorted(two_dim_array, key=lambda x:(x[1],x[0]))

# a = [[3, 2], [2, 2], [1, 1]]
# b = sorted(a, key=lambda x: (x[1], x[0]), reverse=True)
# print(b)


def plusOne(digits):

    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] = digits[i] + 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    print(digits)
    return digits


def plus_one(a):
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i-1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a


def plus_one1(a):
    for i in reversed(range(len(a))):
        if a[i] != 9:
            a[i] += 1
            return a
        else:
            a[i] = 0
    a.insert(0, 1)
    return a


def multiply(num1, num2):
    res = [0]*(len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i+j+1] = res[i+j+1] + num1[i]*num2[j]
            res[i+j] = res[i+j] + res[i+j+1]//10
            res[i+j+1] = res[i+j+1] % 10
    return res


def multiply2(num1, num2):
    if 0 in [num1, num2]:
        return 0

    res = [0]*(len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            digit = num1[i] * num2[j]
            res[i + j] = res[i+j] + digit
            res[i + j + 1] = res[i+j+1] + res[i + j + 1] // 10
            res[i + j] = res[i + j] % 10
    return res


# a = [3, 2, 3, 3, 1, 1]
# b = [[x, a.count(x)] for x in set(a)]
# b = sorted(b, key=lambda x: -x[1])
# c = []
d = [1, 2, 9]
e = [1, 1]
f = [1, 1, 2]

# for num in set(a):
#     c.append([num, a.count(num)])   # O(n)

# c.sort(key=lambda x: -x[1])  # O(nlogn)
# print(plus_one(d))
print(plus_one1(d))
print(multiply(e, f))
print(multiply2(e, f))
