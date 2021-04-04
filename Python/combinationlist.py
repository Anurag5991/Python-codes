def combinationList(target, numbers):
    return combinations(target, numbers, 0, [])


def combinations(target, numbers, index, sub_list):
    
    if target == 0:
        print(sub_list)
        return 

        
    if target < 0:
        return
    for i in range(index, len(numbers)):
        sub_list.append(numbers[i])
        combinations(target - numbers[i], numbers, i, sub_list)
        sub_list.remove(numbers[i])
    
        
        

print(combinationList(7,[3,4,7]))