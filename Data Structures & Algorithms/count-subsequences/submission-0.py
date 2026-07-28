class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # similar to LCS but simple

        # t[j] => mandatory subsequence
        # s[i] => can either add, or not add
        # if s[i] == t[j] , can add (i+1, j+1) or not add (i+1,j)
        # if != must not add (i+1,j)

        if t == "":
            return 1
        if s=="":
            return 0
        cache = {}

        def dfs(i,j):

            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i] != t[j]:
                cache[(i,j)] = dfs(i+1, j)

                return cache[(i,j)]

            # now case where they equal

            # dont include i


            cache[(i,j)] = dfs(i+1,j)

            # include i

            cache[(i,j)] +=  dfs(i+1,j+1)

            return cache[(i,j)]
        return dfs(0,0)