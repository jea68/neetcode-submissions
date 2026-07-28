class Solution:
    def canJump(self, nums: List[int]) -> bool:


        cache  = {len(nums) - 1: True} # pos : can it reach end
        l  = len(nums)-2

        while l >= 0:
            cache[l] = False
            for i in range(1, nums[l]+1):
                if cache[l+i]:
                    cache[l] = True
                    break
            l -=1

        return cache[0]
                

        