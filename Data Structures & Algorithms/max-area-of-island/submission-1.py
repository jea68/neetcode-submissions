class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set([])
        res = []


        def dfs(r,c): # recursively go through

            if (r,c) in visited:
                return
            if c not in range(0,C) or r not in range(0,R):
                return 
            if grid[r][c] == 0:
                return
            
            visited.add((r,c))
            res[-1] += 1

            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            for dr,dc in directions:

                r1 = r + dr
                c1 = c + dc
                dfs(r1,c1)
            return

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res.append(0)
                    dfs(r,c)
                    
        print(res)
        return max(res) if res else 0
        