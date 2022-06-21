def containsDuplicate(nums):
    
    res = set()
    for i in nums:
        if i in res:
            return True
        res.add(i)
    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

