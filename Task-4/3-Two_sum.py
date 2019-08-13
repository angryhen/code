class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,item in enumerate(nums):
            tmp = target - item
            if tmp in hashmap:
                return [i,hashmap[tmp]]
            hashmap[item] = i
        return None
