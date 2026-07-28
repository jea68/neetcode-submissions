class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {len(nums) - 1: 0}

        for l in range(len(nums)-2, -1,-1):
            cache[l] = len(nums)

            for i in range(l+1, l + nums[l] +1):
                if i >= len(nums):
                    break
                cache[l] = min(cache[l], cache[i] + 1)
            
        return cache[0]