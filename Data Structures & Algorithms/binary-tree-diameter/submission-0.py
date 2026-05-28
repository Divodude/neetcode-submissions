# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=-1
        def trav(node,dpth):
            if not node: 
                return 0

            dpth+=1
            ld=trav(node.left,dpth)
            rd=trav(node.right,dpth) 
            self.ans=max(self.ans,ld+rd)
            return max(ld,rd)+1
        trav(root,0)
        return self.ans