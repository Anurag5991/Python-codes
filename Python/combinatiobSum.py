def combinationSum(target, numbers):
    
    list1 = []
    if target == 0:
        return []
    if target < 0:
        return
    for x in numbers:
        remainder = target - x
        path = combinationSum(remainder,numbers)
        if path != None:
            path.append(x)
            combination = path.copy()
            list1.append(combination)
    return list1
            
    

print (combinationSum(8,[2,3,5]))