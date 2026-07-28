class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        r = 0
        res = nums[0]
        curr = 0

        while r < len(nums):

            curr += nums[r]

            res = max(curr, res)

            if curr < 0:
                curr = 0
            r +=1
        return res
        

        