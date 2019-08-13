class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if len(nums) == 0:
            return res
        queue = []
        for i, j in enumerate(nums):
            if i >= k and i-queue[0] >= k:
                queue.pop(0)
            while queue and j >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                res.append(nums[queue[0]])
        return res
