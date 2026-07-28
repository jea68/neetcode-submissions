class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # nodes labelled 0 to n-1
        if n ==1 and not edges:
            return True
        

        adj_list = {}

        for i,j in edges:
            if i not in adj_list:
                adj_list[i] = []
            if j not in adj_list:
                adj_list[j] = []
            adj_list[i].append(j)
            adj_list[j].append(i)
            

        visited = set()

        def dfs(cur, prev):

            if cur in visited:
                return False
            
            visited.add(cur)



            for j in adj_list[cur]:
                if j == prev: # undirected graph so one child will be the prev
                    continue
                if not dfs(j, cur):
                    return False
            
            return True
        return dfs(0,-1) and n == len(visited)

# time : O(E+V) => only go to each node once
        