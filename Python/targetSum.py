def canSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum <= 0:
        return False
    for i in numbers:
        remainder = targetSum - i
        if canSum(remainder,numbers,memo) == True:
            memo[targetSum] = True
    memo[targetSum] = False
    return memo[targetSum]

print(canSum(300,[7,14]))
