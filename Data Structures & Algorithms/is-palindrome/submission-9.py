class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l<r:
            if self.get_value(s[l]) ==False:
                l+=1
            elif self.get_value(s[r]) ==False:
                r-=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l+=1
                r-=1
        return True
            
    
    def get_value(self, s):
        char = s.lower()
        if (ord(char) <= ord('z') and ord(char) >= ord('a')) or (ord(char) <= ord('9') and ord(char) >= ord('0')):
            return True
        return False