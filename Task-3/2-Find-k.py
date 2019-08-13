def partition(nums, l, r):
    basic = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < basic:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


def find_k(nums, k):
    a = 0
    b = len(nums) - 1
    index = partition(nums, a, b)

    while index != len(nums) - k:
        if index >= len(nums) - k:
            index = partition(nums, a, index-1)
        else:
            index = partition(nums, index+1, b)
    return nums[index]
