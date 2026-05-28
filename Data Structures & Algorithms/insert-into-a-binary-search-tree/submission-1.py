# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def trav(node):
            if not node:
                return
            if node.val>val:
                if not node.left:
                    node.left=TreeNode(val)
                trav(node.left)
            if node.val<val:
                if not node.right:
                    node.right=TreeNode(val)
                trav(node.right)
            

        trav(root)
        if not root:
            return TreeNode(val)
        return root