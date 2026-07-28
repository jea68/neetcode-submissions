class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r = 0, len(s) -1

        while l < r:
            if not self.isletter(s[l]):
                l += 1
                continue
            if not self.isletter(s[r]):
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -=1
            
        return True
            
        


    
    def isletter(self, x):
        x = x.lower()
        print(x)
        if (ord(x) >= ord("a") and ord(x) <= ord("z")) or  ord("0") <= ord(x) <= ord("9"):
            return True
        return False

