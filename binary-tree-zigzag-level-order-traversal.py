# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def getNode(root, h , store):
            if not root:
                return 
            if h == 0:
                store.append(root.val)

            getNode(root.left, h - 1, store)
            getNode(root.right, h - 1, store)

            return store

        def height(root):
            if not root:
                return 0
            
            return 1 + max(height(root.left), height(root.right))

        nodes = []
        for i in range(height(root)):
            levelNodes = getNode(root,i,[])
            if i & 1 == 0:
                nodes.append(levelNodes)
            else:
                nodes.append(levelNodes[::-1])

        return nodes
