def Permutations(nums):
    n = len(nums)
    if n == 0:
        return []
    used = [False] * n
    res = []
    hs(nums, 0, [], used, res)
    return res
    
def hs(nums, index, pre, used, res):
    if index == len(nums):
        res.append(pre.copy())
        return 
    
    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            pre.append(nums[i])
            
            hs(nums, index+1, pre, used, res)
            
            used[i] = False
            pre.pop()
            
Permutations([1,2,3])
