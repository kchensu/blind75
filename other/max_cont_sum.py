# def max_sum(a, k):
#     res = 0
#     res = sum(a[:k])
#     curr = res # 17
#     for i in range(k, len(a)):
#         curr = curr + a[i] - a[i-k]
#         res = max(res, curr)
#     return res
import itertools


def maximum_subarray(a):
    min_sum, max_sum = 0, 0
    for i in itertools.accumulate(a):
        min_sum = min(min_sum, i)
        max_sum = max(max_sum, i - min_sum)
    return max_sum


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(global_max, current_max)
        # if current_max > global_max:
        #     global_max = current_max
    return global_max


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
# print(max_sum(arr, k))
print(maximum_subarray(arr))
print(maxSubArray(arr))
