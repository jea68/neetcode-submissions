# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = 0
        
        def maxdepth(newroot):
            if not newroot:
                return 0
            
            left = maxdepth(newroot.left)
            right = maxdepth(newroot.right)

            self.res = max(self.res,left+right)
            return 1 + max(left, right)
        
        maxdepth(root)
        return self.res

        res = 0
        res_left =  0 if not root.left else maxdepth(root.left)
        res_right =  0 if not root.right else maxdepth(root.right)

        res = max(res_left+res_right,self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right) )

        return res

        
        