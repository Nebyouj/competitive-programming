# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff = 0

        def hepler(root, minVal, maxVal):
            if not root:
                return

            self.diff = max(self.diff, max(abs(minVal - root.val), abs(maxVal - root.val)))
            maxVal = max(maxVal,  root.val)
            minVal = min(minVal, root.val)
            hepler(root.left, minVal, maxVal)
            hepler(root.right, minVal, maxVal)

        hepler(root, root.val, root.val)

        return self.diff
