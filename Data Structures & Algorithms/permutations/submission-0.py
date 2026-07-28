class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:



        # iteratively

        perms = [[]]

        for n in nums:
            nextperm_row = []
            for perm in perms:
                for i in range(len(perm) +1):
                    temp = perm.copy()
                    temp.insert(i, n)
                    nextperm_row.append(temp)
                
                perms = nextperm_row
        return perms

        