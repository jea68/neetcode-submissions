class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set([])
        res = 0

        l,r = 0,0
        while r <= len(s)-1:
            while s[r] in window and l<=r:
                window.remove(s[l])
                l+=1
            
            window.add(s[r])
            r+=1
            res = max(res, r-l)
            
        
        return res
            




        