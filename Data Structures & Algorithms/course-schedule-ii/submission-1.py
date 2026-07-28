class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 1:
            return [0]
        # adj_list

        preMap = {i:[] for i in range(numCourses)} # node: its preReqs

        for crs,pre in prerequisites:
            preMap[crs].append(pre)


        res = []
        visited = set()
        
        def dfs(crs): # get to buttom of trees and then add

            if crs in visited:
                return False

            if crs not in preMap:
                return True            

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            res.append(crs) # added all its pres, so it can go now (pres => crs)
            preMap.pop(crs)
            visited.remove(crs)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
    
        return res
        
            


        