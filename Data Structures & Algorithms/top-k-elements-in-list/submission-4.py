class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        freq  = [[] for i in range(len(nums)+1)]
        for i in nums:
            bucket[i] = 1 + bucket.get(i,0)
        for c,n in bucket.items():
            freq[n].append(c)
        res = []
        for i in range(len(nums), -1, -1):
            for m in freq[i]:
                res.append(m)
                if len(res) == k:
                    return res
        

        return res
