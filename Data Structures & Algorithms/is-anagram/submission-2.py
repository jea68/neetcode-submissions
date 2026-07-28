class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base_s  = {}
        base_t = {}
        for letter in s:
            base_s[letter] = 1 + base_s.get(letter,0)

        for letter in t:
            base_t[letter] = 1 + base_t.get(letter,0)

        return base_s == base_t


        