def reverse(nums):
    i = 0
    j = len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums
    
reverse(['s','a','q','w'])
