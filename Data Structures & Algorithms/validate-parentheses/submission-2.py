class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapper = {"[":"]", "{":"}", "(":")"}

        for i in s:
            if i in mapper:
                stack.append(i)
            elif stack and mapper[stack[-1]] == i:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        