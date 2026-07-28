class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        #########
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

               


        