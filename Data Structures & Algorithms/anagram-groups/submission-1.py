class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == [""]:
            return [[""]]

        # 26 length tu as set
        
        cache = {} # 26 code (tuple as its unchangeble) : list

        for word in strs:
            code26 = [0]* 26
            for i in word:
                pos = ord(i) - ord("a")
                code26[pos] += 1
            key = tuple(code26)
            if key in cache:
                cache[key].append(word)
            else:
                cache[tuple(code26)] = [word]
        return list(cache.values())

        