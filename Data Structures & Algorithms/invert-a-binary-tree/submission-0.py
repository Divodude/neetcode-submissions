# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapp(root):
            if not root:
                return None
            
            root.left,root.right=root.right,root.left
            swapp(root.left)
            swapp(root.right)
        swapp(root)
        return root

        