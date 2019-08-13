# 冒泡排序
def Bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                p = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = p
    return nums
    
# 选择排序
def Selection_sort(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(i+1,len(nums)):
            if nums[index] > nums[j]:
                index = j
        if index != i:
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp
    return nums
    
# 插入排序
def Insertion_sort(nums):
    for i in range(len(nums)-1):
        index = i
        tmp = nums[index+1]
        while (index >=0 and nums[index] > tmp):
            nums[index+1] = nums[index]
            index -= 1
        nums[index+1] = tmp
    return nums
    
# 快速排序
def partition(nums, l, r):
    basic = nums[r]
    i = l - 1
    for j in range(l,r):
        if nums[j] < basic:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1

def Quick_sort(nums, l, r):
    if l < r:
        index = partition(nums, l, r)
        Quick_sort(nums, l, index-1)
        Quick_sort(nums, index+1, r)
    return nums      
    
# 归并排序
def merge(l, r):
    res = []
    i = j = 0
    while i <len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    if i == len(l):
        res += r[j:]
    else:
        res += l[i:]
    return res
    
def Merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = Merge_sort(nums[:middle])
    right = Merge_sort(nums[middle:])
    return merge(left, right)
    
if __name__ == '__main__':
    nums = [2,5,1,5,8,6,9,3]
    Bubble_sort(nums)
    Selection_sort(nums)
    Insertion_sort(nums)
    Quick_sort(nums, 0, len(nums)-1)
    Merge_sort(nums)    
    
    
    
    
    
    
    
