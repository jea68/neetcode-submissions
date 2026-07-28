class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        # brute force it
        curSet = []
        res  = []

        def dfs(i, curSum, curSet):

            if curSum == target:
                res.append(curSet.copy())
                return

            if i == len(nums):
                return
            if curSum > target:
                return
            
            curSet.append(nums[i])
            dfs(i, curSum + nums[i], curSet )
            curSet.pop()
            dfs(i+1 , curSum, curSet )
            return
        dfs(0, 0, curSet)
        return res
        