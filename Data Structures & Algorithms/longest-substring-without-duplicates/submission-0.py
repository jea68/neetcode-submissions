class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {} # val : pos
        l = 0
        res = 0
        for pos, val in enumerate(s):

            if val in cache:
                temp = cache[val]
                while l < temp + 1:
                    cache.pop(s[l])
                    l+= 1
            
            cache[val] = pos
            res = max(res, pos + 1 - l)
        
        return res

               


        