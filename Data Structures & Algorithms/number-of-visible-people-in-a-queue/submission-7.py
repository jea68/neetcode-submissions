class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # only to the right
        # all values unique
        res = [0]*len(heights)
        stack = [] # stack of positions

        for pos,val in enumerate(heights):
            # as you get to a pos, if it's greater than top of stack. Then top of stack can see everything else thats been popped + that new one
            while stack and heights[stack[-1]] < val:
                res[stack.pop()] +=1 # whatever it could have seen before, add 1

            if stack: # if shorter, then it can see the new additon
                res[stack[-1]] += 1

            stack.append(pos)
        return res
            


