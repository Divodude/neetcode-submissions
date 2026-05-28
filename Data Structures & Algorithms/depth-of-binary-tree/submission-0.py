# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node,dpth):
            if not node:
                return dpth 
            dpth+=1
            ld=depth(node.left,dpth)
            rd=depth(node.right,dpth)
            return max(ld,rd)
        return depth(root,0)

        