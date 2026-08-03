class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = {}
        res = 0

        l = 0
        for r in range(len(s)):
            if s[r] in window:
                l = max(window[s[r]] +1, l) # if l is past it then no need to update
            window[s[r]] = r
            
    
            res = max(res, r-l+1)
            
        
        return res
            




        