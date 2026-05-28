# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = float("-inf")

        def trav(node):

            if not node:
                return 0

            l = max(0, trav(node.left))
            r = max(0, trav(node.right))

            self.ans = max(self.ans, l + r + node.val)

            return max(l, r) + node.val

        trav(root)

        return self.ans