class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        inf = 2147483647
        R,C = len(grid), len(grid[0])
        visit = set()

        q = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: # if its a treasure
                    q.append((r,c))
                    visit.add((r,c))

        
        # so we are creating a queue with only the treasure nodes
        # we then do a BFS starting at each treasure node going outwards
        # BFS is FIFO, we are expanding outwards from each node together
        #(rather than exhausting all paths from treasure 1, then treasure 2)
        # so essentially, we mark down:
        # all points which are dist 1 away from a treasure, then those dist 2 ..
        dist = 1
        while q:

            for i in range(len(q)):
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(R) and nc in range(C) and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        if grid[nr][nc] == 2147483647:
                            q.append([nr,nc])
                            grid[nr][nc] = dist
                
            dist += 1
        return grid



