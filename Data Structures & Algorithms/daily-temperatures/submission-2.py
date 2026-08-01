class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # brute force will be to search through everything -> o(n^2)
        # max(val and pos)

        # monotonic stack

        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackI,stackT = stack.pop()
                res[stackI] = i - stackI
            
            stack.append([i,t])
        return res
