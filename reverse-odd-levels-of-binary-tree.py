# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def reverse(left,right, h):
            if not left and not right:
                return 
            if h & 1 != 0:
                left.val, right.val = right.val, left.val 
                
            h += 1
            reverse(left.left,right.right, h)
            reverse(left.right, right.left, h)

        reverse(root.left,root.right, 1)

        return root
