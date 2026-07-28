class Solution:
    def jump(self, nums: List[int]) -> int:
## Greedily do the max jump
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res


        cache = {len(nums) - 1: 0}

        for l in range(len(nums)-2, -1,-1):
            cache[l] = len(nums)

            for i in range(l+1, l + nums[l] +1):
                if i >= len(nums):
                    break
                cache[l] = min(cache[l], cache[i] + 1)
            
        return cache[0]