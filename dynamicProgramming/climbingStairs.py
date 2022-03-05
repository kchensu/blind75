def climbingStairs(n, memo={1: 1, 2: 2}):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = climbingStairs(n-1, memo) + climbingStairs(n-2, memo)
    return memo[n]


print(climbingStairs(5))
