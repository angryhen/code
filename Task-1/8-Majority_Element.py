class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = dict()
        max_id = nums[0]
        max_num = 0
        for i in range(len(nums)):
            if nums[i] in N:
                N[nums[i]] += 1
                if max_num < N[nums[i]]:
                    max_num = N[nums[i]]
                    max_id = nums[i]
            else:
                N[nums[i]] = 1
        return max_id
                
