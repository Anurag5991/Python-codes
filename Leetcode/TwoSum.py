def twoSum(nums, target):

# Brute force method
#    for i in range(len(nums)-1):
#        for j in range(1,len(nums)):
#            if nums[i] + nums[j] == target:
#                return([i,j])
#
# memomization
    memo = {}
    for i in range(len(nums)):
        if (target - nums[i]) not in memo:
            memo[nums[i]] = i
        else:
            return [memo[target - nums[i]], i]


print(twoSum([2,5,7,11],18))