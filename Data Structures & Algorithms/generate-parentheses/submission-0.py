class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(closed, opened, curr):

            if opened == n and closed == n:
                res.append(curr)
                return
            
            if opened <= n:
                dfs(closed, opened + 1, curr + "(")

            if opened > closed and closed <= n:
                dfs(closed + 1, opened, curr + ")")
            return
        dfs(0,0,"")
        return res

