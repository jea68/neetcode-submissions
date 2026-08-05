class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        temp = []

        def subset(i):

            if i>= len(nums):
                res.append(temp.copy())
                return
            
            temp.append(nums[i])
            subset(i+1)
            temp.pop()
            subset(i+1)

        subset(0)
        return res

        