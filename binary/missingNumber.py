def missingNumber(a):
    nums = list(range(0, len(a) + 1))
    return sum(nums) - sum(a)


nums = [3, 0, 1]
print(missingNumber(nums))
