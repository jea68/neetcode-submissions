class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap of anagrams

        list_of_sets = {}
        for word in strs:
            temp = [0]*26
            for letter in word:
                temp[ord(letter) - ord('a')]+=1
            if tuple(temp) in list_of_sets:
                list_of_sets[tuple(temp)].append(word)
            else:
                list_of_sets[tuple(temp)] = [word]
        
        return list(list_of_sets.values())