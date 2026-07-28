class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i # curr end pos

            while stack and stack[-1][1] > h: # if its greater than curr height, 
            #then that block can't extend further

                x,y = stack.pop()
                maxArea = max(maxArea, y * (i - x))
                start = x

            stack.append((start, h))
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
        

        