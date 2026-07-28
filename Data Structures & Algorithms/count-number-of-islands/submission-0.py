class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R = len(grid)
        C = len(grid[0])
        visited = set([])
        res = 0


        def dfs(r,c): # recursively go through

            if (r,c) in visited:
                return
            if c not in range(0,C) or r not in range(0,R):
                return 
            if grid[r][c] == "0":
                return
            
            visited.add((r,c))

            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            for dr,dc in directions:

                r1 = r + dr
                c1 = c + dc
                dfs(r1,c1)
            
            return
        print(R,C)
        for r in range(R):
            for c in range(C):
                #print(r,c)
                if grid[r][c] == "1" and (r,c) not in visited:
                    print(r,c)
                    res += 1
                    dfs(r,c)
                    
        
        return res
        