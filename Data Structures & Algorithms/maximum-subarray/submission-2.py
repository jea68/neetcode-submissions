class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum


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
        

        