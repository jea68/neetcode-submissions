class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        compare = {}
        for i in s1:
            compare[i] = 1 + compare.get(i,0)

        l,r = 0,0
        window = {}
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r],0)
            if window == compare:
                return True

            print(window)
            print(compare)
            while r - l +1 >= len(s1):
                window[s2[l]] -=1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l+=1
                
            
        return False

        