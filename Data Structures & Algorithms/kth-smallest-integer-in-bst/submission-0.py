# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=1
        self.ans=0
        def trav(node):
            if not node:
                return 
            trav(node.left)
            if self.count==k:
                self.ans=node.val
            self.count+=1
            trav(node.right)
        trav(root)
        return self.ans


        