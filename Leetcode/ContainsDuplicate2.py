def containsNearbyDuplicate(nums, k):
    dic = dict()
    for i,n in enumerate(nums):
        if n in dic and abs(i - dic[n] <= k):
            return True
        dic[n] = i
    return False

print(containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0], 1))