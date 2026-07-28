class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cache = {}

        for i,j in enumerate(nums):
            
            if (target - j) in cache:
                return [cache[target-j], i]
            if j not in cache:
                cache[j] = i
        