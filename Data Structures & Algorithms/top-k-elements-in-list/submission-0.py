class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        
        cache = {}# val:num occurences
        highest = 0
        for i in nums:
            cache[i] = 1 + cache.get(i,0)
        
        
        klist = [[] for i in range(max(cache.values()) +1)]

        for val, occ in cache.items():
            klist[occ].append(val)
        
        res = []
        for i in range(len(klist)-1,-1,-1):
            for j in klist[i]:
                res.append(j)
                k-=1
                if k == 0:
                    return res
