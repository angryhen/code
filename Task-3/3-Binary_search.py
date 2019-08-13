# 二分查找
def Binary_search(nums, k):
    left = 0
    right = len(nums)-1
    index = (right + left) // 2
    while nums[index] != k:
        if k < nums[index]:
            right = index - 1
        else:
            left = index + 1
        index = (right + left) // 2
    return index
