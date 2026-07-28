class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dataset = set([])

        for i in nums:
            if i in dataset:
                return True
            dataset.add(i)
        return False
