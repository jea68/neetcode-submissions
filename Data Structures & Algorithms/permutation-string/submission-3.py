class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1_hash = {}
        s2_hash = {}
        for i in s1:
            s1_hash[i] = 1 + s1_hash.get(i,0)



        l,r = 0,0

        for r in range(len(s2)):
            print(r)
            if s2[r] not in s1_hash:
                l = r+1
                s2_hash = {}
                continue
            
            s2_hash[s2[r]] = 1 + s2_hash.get(s2[r],0)
            print(s2_hash)
            if s2_hash == s1_hash:
                return True
            
            if r - l + 1 == len(s1):
                s2_hash[s2[l]] -= 1
                l+=1
        return False

                   