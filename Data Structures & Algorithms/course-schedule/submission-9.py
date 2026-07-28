class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # graph Q essentially checking if any loops

        #1 => 0 if 0 in children, return false

        preMap = {i:[] for i in range(numCourses)} # child : it's parents => a prereq lsit (rather than its children)

        visited = set() # courses already visited in on a dfs of the prereqs
        # if we see a node is already visited on a dfs, then we know theres a loop
        # essentially we start at a node and go up (visit all is parents)
        # if we see the node whilst going up  => Loop
        #
        # make the adj_list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        def dfs(cur_crs):

            if cur_crs in visited: # if we've seen before, then this cur_crs can't be completed
                return False

            if preMap[cur_crs] == []: # if crs has no pre_reqs (or we've cleaned them)
                return True   
                
            visited.add(cur_crs)

            for pre in preMap[cur_crs]:
                if not dfs(pre):
                    return False
                
            visited.remove(cur_crs)
                # we start at a node, then go upwards, after we've seen the node is not looped up top
                    # (it can be completed), we then remove it before we go to the next node
                    # because say this node a pre of another node, regardless of if we see it again, we already know we can do the course
                
            preMap[cur_crs] = [] # if we see it again, we know we can complete it
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

