class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with division
        # total product array o(n)
        # total / n -> value

        product_array = 0
        res = []
        zero_pos = []
        has_zero = False
        non_zero_length = 0

        for pos,i in enumerate(nums):
            if i == 0:
                has_zero = True
                zero_pos.append(pos)
                continue
            non_zero_length += 1
            if product_array == 0:
                product_array = 1 *i
            else:
                product_array = product_array *i
        if has_zero:
            res = [0]*len(nums)
            if len(nums) - non_zero_length >1:
                return res
            for i in zero_pos:
                res[i] = product_array
            return res
        
        for n in nums:
            res.append(int(product_array/n))
        return res

