def continousSubarraySum(n, k):
    remainder = {0: -1}
    total = 0

    for i, val in enumerate(n):
        total += val
        r = total % k
        if r not in remainder:
            remainder[r] = i

        elif i - remainder[r] == 2:
            return True
    return False


nums = [23, 2, 4, 6, 7]
k = 6
print(continousSubarraySum(nums, k))
