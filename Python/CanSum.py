def canSum(Sum, num, memo = {}):
    if Sum in memo:
        return memo[Sum]
    if Sum == 0:
        return []
    if Sum < 0:
        return None
    for number in num:
        remainder = Sum - number
        remainderResult = canSum(remainder,num,memo)
        if remainderResult != None:
            remainderResult.append(number)
            memo[Sum] = remainderResult.copy()
            return memo[Sum]
    
    memo[Sum] = None
    return None
            
            
print(canSum(10,[2,3,5]))