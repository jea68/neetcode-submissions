class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median of both is just the middle value -> len(m+n)//2
        # build subarrays of both till the lenght of each matches the above and just take the value

        # start with the shorter list so that the bigger list just eats the remaining

        # A,B = nums1,nums2
        # half = (len(A) + len(B))//2

        # if len(A) > len(B):
        #     A,B = B,A # make A smaller

        # while True:
        #     l,r = 0, len(A)-1
        #     a_pointer = (l+r)//2 # middle value of A

        #     # take the rest of B
        #     b_pointer = half - a_pointer - 2 # take off two since both are zero indexed

        #     # now we have an ample sized subarray
        #     # question is if we want to take more from A or from B
        #     # if a_pointer + 1 < b_pointer then we are cooked, we want more from A -> shift a_pointer right
        #     # if b_pointer + 1 < a_pointer we want more from B -> shift a_pointer left

            
        #     a_value_1 = A[a_pointer + 1]  if a_pointer + 1 < len(A) else float('infinity') # if a_pointer + 1 does not exist, then we set it super high
        #     b_value_1 = B[b_pointer + 1]  if b_pointer + 1 < len(B) else float('infinity')
            
        #     a_value = A[a_pointer]  if a_pointer < 0 else -float('infinity')
        #     b_value = B[b_pointer]  if b_pointer < 0 else -float('infinity')

        #     if a_value_1 >= B[b_pointer] and b_value_1 >=  A[a_pointer]:
        #         if (len(A) + len(B)) %2 == 0: #even
        #             return (max(B[b_pointer], A[a_pointer]) + min(B[b_pointer +1], A[a_pointer+1]))/2
        #         else:
        #             return max(B[b_pointer], A[a_pointer])
        #     elif a_value_1 < b_value:
        #         l = a_pointer + 1
        #     else:
        #         r = a_pointer - 1
                

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
