class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set([])
        res = 0
        


        def dfs(r,c): # recursively go through

            if (r,c) in visited:
                return 0
            if c not in range(0,C) or r not in range(0,R):
                return 0
            if grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r + 1,c) + dfs(r -1,c) + dfs(r ,c+1) + dfs(r ,c - 1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res = max(res, dfs(r,c))
                    
        
        return res
        