class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        maxf = 0
        count = {}
        res = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r],0)
            # the Maxf becomes the foundation letter

            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                maxf = max(maxf, count[max(count)])
                l += 1
            res = max(res, r-l+1)
        return res
        
