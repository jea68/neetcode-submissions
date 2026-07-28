class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]* len(temperatures)

        stack = [] # Decreasign stack

        for pos,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                x,y = stack.pop()
                res[x] = pos - x
            
            stack.append((pos, temp))
        return res



        