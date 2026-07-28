class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l,r = 0, len(heights)-1

        res = 0
        while r >l:
            h = min(heights[r],heights[l])

            curr = h * (r - l)

            res = max(res, curr)

            if heights[l] < heights[r]:
                l += 1
            else:

                r -= 1
        return res


        