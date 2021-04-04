def bestSum(targetSum, numbers):

   
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        
        if remainderCombination != None:
                        
            remainderCombination.append(num)
            combination = remainderCombination.copy()
            if (shortestCombination == None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination
                
    
    return shortestCombination
  
            
    
print(bestSum(10,[3,2]))
