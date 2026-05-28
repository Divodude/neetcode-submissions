# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(node1,node2):
            if not node1 and  not node2:
                return True
            if not node1 or not node2:
                return False
            
     
            l=trav(node1.left,node2.left)
            r=trav(node1.right,node2.right)
            return node1.val==node2.val and  l and r 
        return trav(p,q)
        