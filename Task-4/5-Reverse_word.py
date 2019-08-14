def Reverse_word(nums):
    nums = nums.strip()
    i = len(nums)-1 
    j = len(nums)
    res = ''
    while i > 0:
        if nums[i] == ' ':
            res += nums[i+1:j] + ' '
            while nums[i] == ' ':
                i -= 1
            j = i + 1
        i -= 1
    return res + nums[:j]
