# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag=True
        def trav(node,dpth):
            if not node:
                return 0
            dpth+=1
            ld=trav(node.left,dpth)
            rd=trav(node.right,dpth)
            if abs(ld-rd)>1:
                self.flag=False
            
            return max(ld,rd)+1
        trav(root,0)
        return self.flag
            
        